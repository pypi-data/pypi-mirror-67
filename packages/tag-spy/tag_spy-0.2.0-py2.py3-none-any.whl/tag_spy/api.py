# Copyright 2020 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide public API functions for handling Docker image tags."""


import logging
from urllib.parse import urlsplit

from .filter_helpers import filter_latest_matching, get_latest_by_timestamp
from .registry_helpers import get_tags, get_token, verify_v2_capability


logger = logging.getLogger(__name__)


def get_latest_tag(
    image: str,
    tag_part: str,
    label: str,
    auth_url: str = "https://auth.docker.io/token",
    registry_url: str = "https://registry-1.docker.io",
    service: str = "registry.docker.io",
) -> str:
    """
    Parse the latest DD-DeCaF-specific tag of a Docker image from its registry.

    Args:
        image (str): The fully specified image name, for example, 'dddecaf/wsgi-base'.
        tag_part (str): The base part of the tag that you are interested in, for
            example, 'alpine' will match 'dddecaf/wsgi-base:alpine_2020-04-28_24fe0a0'.
        label (str): The image label that defines the build timestamp, for example,
            'dk.dtu.biosustain.wsgi-base.alpine.build.timestamp'.
        auth_url (str, optional): The URL from where to retrieve an access token for the
            registry (the default https://auth.docker.io/token corresponds to
            Docker Hub).
        registry_url (str, optional): The URL of the registry API
            (default https://registry-1.docker.io).
        service (str, optional): The URL of the service for which to request an access
            token (default registry.docker.io).

    Returns:
        str: The very latest Docker image tag in its entirety.

    Raises:
        RuntimeError: If there are unexpected complications with the tags of the
            specified image.
        urllib.error.URLError: In case of problems communicating with the registry.

    """
    parts = urlsplit(auth_url)
    token = get_token(parts, image, service)
    headers = {
        "Accept": "application/vnd.docker.distribution.manifest.v2+json",
        "Authorization": f"Bearer {token}",
    }
    parts = urlsplit(registry_url)
    verify_v2_capability(parts, headers)
    tags = get_tags(parts, headers, image)
    if len(tags) == 0:
        raise RuntimeError(f"The requested image {image} does not have any tags.")
    try:
        latest_tags = filter_latest_matching(tags, tag_part)
    except ValueError:
        raise RuntimeError(
            f"The requested image {image} does not have any tags corresponding to the "
            f"expected format {tag_part}_<date>_<commit>."
        )
    if len(latest_tags) > 1:
        latest = get_latest_by_timestamp(parts, headers, image, label, latest_tags)
    elif len(latest_tags) == 1:
        latest = latest_tags[0]
    else:
        raise RuntimeError(
            f"The requested image {image} does not have any tags corresponding to the "
            f"expected format {tag_part}_<date>_<commit>."
        )
    return str(latest)
