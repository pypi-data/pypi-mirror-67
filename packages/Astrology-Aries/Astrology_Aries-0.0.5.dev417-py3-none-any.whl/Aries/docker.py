import datetime
import requests
import re
import logging
from .web import WebAPI
logger = logging.getLogger(__name__)


class DockerAPI(WebAPI):
    def __init__(self, hostname):
        super().__init__("https://%s" % hostname)

    def check_v2_support(self):
        """Checks the API version by sending GET request to /v2/ endpoint.

        Returns: The version of the API. e.g. 2.0

        """
        response = self.get("/v2/")
        version = response.headers.get("Docker-Distribution-Api-Version", "").split("/")[-1]
        return version


class DockerImage:
    """
    Attributes:
        name: The docker image name, which may contain the hostname if it is not on DockerHub,
            and optionally the tag or digest.
            This is the same as the NAME[:TAG|@DIGEST] to be used in the docker pull command.
            e.g. ubuntu, tensorflow/tensorflow:2.2.0rc4-jupyter, mcr.microsoft.com/windows
            See Also: https://docs.docker.com/engine/reference/commandline/pull/
        hostname: The hostname of the Docker registry.
        path: The path of the docker image under the registry, without tag or digest.
        tag: The docker image tag, if included in the name.

    See Also:
        https://docs.docker.com/registry/spec/api/
        https://github.com/docker/distribution/blob/master/reference/reference.go
        https://docs.docker.com/engine/reference/commandline/pull/
        https://ops.tips/blog/inspecting-docker-image-without-pull/
    """

    DOCKER_IO_REGISTRY = "registry-1.docker.io"

    def __init__(self, name):
        self.name = name
        self.hostname, self.path, self.tag, self._digest = self.parse_name(self.name)
        self._manifest = None
        self._token = None
        self._token_expire_time = None

    @staticmethod
    def parse_name(name):
        """Parses docker image name, which can have the format as accepted by the docker pull command.

        Args:
            name (str): Docker image name, including tag or digest, i.e. NAME[:TAG|@DIGEST]

        Returns:
            A 4-tuple of hostname, path, tag and digest.
            hostname defaults to DOCKER_IO_REGISTRY
        """
        hostname, path = DockerImage.match_host(name)
        if not hostname:
            hostname = DockerImage.DOCKER_IO_REGISTRY

        # Try to match the digest followed by the image name.
        path, digest = DockerImage.match_digest(path)

        # There should be no tag if digest is followed by the image name.
        if digest:
            tag = None
        else:
            path, tag = DockerImage.match_tag(path)

        # Official images are identified with library/IMAGE_NAME
        if "/" not in path and hostname == DockerImage.DOCKER_IO_REGISTRY:
            path = "library/" + path

        return hostname, path, tag, digest

    @staticmethod
    def match_host(name):
        """Parses the docker image name, extracts the hostname and path (which may also include the tag/digest).
        """
        name_pattern = r"(?:((?:localhost)|(?:[^/]*\.[^/]*)|(?:[^/]*\:[^/]*))/)?(.+)"
        match = re.match(name_pattern, name)
        if not match:
            raise ValueError("Invalid image name: %s" % name)
        groups = match.groups()
        hostname = groups[0]
        path_with_tag = groups[1]
        return hostname, path_with_tag

    @staticmethod
    def match_tag(name):
        tag_pattern = r"(.+)\:([\w][\w.-]{0,127})"
        match = re.match(tag_pattern, name)
        if match:
            path = match.groups()[0]
            tag = match.groups()[1]
        else:
            path = name
            tag = "latest"
        return path, tag

    @staticmethod
    def match_digest(name):
        digest_pattern = r"(.+)\@([^/]*)"
        match = re.match(digest_pattern, name)
        if match:
            path = match.groups()[0]
            digest = match.groups()[1]
        else:
            path = name
            digest = None
        return path, digest

    @property
    def digest(self):
        """The digest of the docker image
        """
        if not self._digest:
            self._digest = self.get_manifest().headers.get("Docker-Content-Digest").strip()
        return self._digest

    @property
    def token(self):
        if self._token and self._token_expire_time and self._token_expire_time > datetime.datetime.now():
            return self._token
        self.get_token()
        return self._token

    def get_token(self):
        url = "https://auth.docker.io/token?scope=repository:%s:pull&service=registry.docker.io" % self.path
        r = requests.get(url).json()
        self._token = r.get("token")
        expire_sec = r.get("expires_in")
        if expire_sec and str(expire_sec).isdigit():
            self._token_expire_time = datetime.datetime.now() + datetime.timedelta(seconds=int(expire_sec))
        return self._token

    def send_get_request(self, url, headers=None):
        if headers is None:
            headers = {}
        # docker.io requires a token to access the API
        # Even though the token can be obtained without authorization
        if self.hostname == self.DOCKER_IO_REGISTRY and "Authorization" not in headers:
            headers["Authorization"] = "Bearer %s" % self.token
        response = requests.get(url, headers=headers)
        return response

    def get_manifest(self):
        """Gets the manifest HTTP response.
        """
        if not self._manifest:
            url = "https://%s/v2/%s/manifests/%s" % (self.hostname, self.path, self.tag)
            response = self.send_get_request(
                url,
                headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"}
            )
            if response.status_code != 200:
                raise ValueError(
                    "Request to %s failed with status code %s" % (url, response.status_code)
                )
            self._manifest = response
        return self._manifest

    def is_accessible(self):
        """Checks if the image is accessible.
        This method returns False if the existence cannot be determined.

        Returns:

        """
        try:
            self.get_manifest()
            return True
        except ValueError:
            return False

    def inspect(self):
        config_digest = self.get_manifest().json().get("config", {}).get("digest")
        url = "https://%s/v2/%s/blobs/%s" % (self.hostname, self.path, config_digest)
        return self.send_get_request(url).json()

    def get_size(self):
        """Gets the size of the docker image by adding the sizes of all layers.
        This method returns None if the size cannot be determined.
        """
        try:
            layers = self.get_manifest().json().get("layers")
            total_size = 0
            for layer in layers:
                total_size += layer.get("size", 0)
        except Exception as ex:
            logger.error("Cannot determine image size for %s: %s" % (self.name, str(ex)))
            import traceback
            traceback.print_exc()
            return None
        return total_size
