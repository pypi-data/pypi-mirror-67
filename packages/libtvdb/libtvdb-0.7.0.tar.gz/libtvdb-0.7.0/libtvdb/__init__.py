"""libtvdb is a wrapper around the TVDB API (https://api.thetvdb.com/swagger).
"""

import json
from typing import Any, ClassVar, Dict, List, Optional
import urllib.parse

import deserialize
import requests

from libtvdb.exceptions import TVDBException, NotFoundException, TVDBAuthenticationException
from libtvdb.model.actor import Actor
from libtvdb.model.episode import Episode
from libtvdb.model.show import Show
from libtvdb.utilities import Log


class TVDBClient:
    """The main client wrapper around the TVDB API.

    Instantiate a new one of these to use a new authentication session.
    """

    class Constants:
        """Constants that are used elsewhere in the TVDBClient class."""

        AUTH_TIMEOUT: ClassVar[float] = 3
        MAX_AUTH_RETRY_COUNT: ClassVar[int] = 3

    _BASE_API: ClassVar[str] = "https://api.thetvdb.com"

    def __init__(self, *, api_key: str, user_key: str, user_name: str) -> None:
        """Create a new client wrapper.

        If any of the supplied parameters are None, they will be loaded from the
        keychain if possible. If not possible, an exception will be thrown.
        """

        if api_key is None:
            raise Exception("No API key was supplied")

        if user_key is None:
            raise Exception("No user key was supplied")

        if user_name is None:
            raise Exception("No user name was supplied")

        self.api_key = api_key
        self.user_key = user_key
        self.user_name = user_name
        self.auth_token = None

    # pylint: disable=no-self-use
    def _expand_url(self, path: str) -> str:
        """Take the path from a URL and expand it to the full API path."""
        return f"{TVDBClient._BASE_API}/{path}"

    # pylint: enable=no-self-use

    # pylint: disable=no-self-use
    def _construct_headers(self, *, additional_headers: Optional[Any] = None) -> Dict[str, str]:
        """Construct the headers used for all requests, inserting any additional headers as required."""

        headers = {"Accept": "application/json"}

        if self.auth_token is not None:
            headers["Authorization"] = f"Bearer {self.auth_token}"

        if additional_headers is None:
            return headers

        for header_name, header_value in additional_headers.items():
            headers[header_name] = header_value

        return headers

    # pylint: enable=no-self-use

    def authenticate(self):
        """Authenticate the client with the API.

        This will exit early if we are already authenticated. It does not need
        to be called. All calls requiring that the client is authenticated will
        call this.
        """

        if self.auth_token is not None:
            Log.debug("Already authenticated, skipping")
            return

        Log.info("Authenticating...")

        login_body = {
            "apikey": self.api_key,
            "userkey": self.user_key,
            "username": self.user_name,
        }

        for i in range(0, TVDBClient.Constants.MAX_AUTH_RETRY_COUNT):
            try:
                response = requests.post(
                    self._expand_url("login"),
                    json=login_body,
                    headers=self._construct_headers(),
                    timeout=TVDBClient.Constants.AUTH_TIMEOUT,
                )

                # Since we authenticated successfully, we can break out of the
                # retry loop
                break
            except requests.exceptions.Timeout:
                will_retry = i < (TVDBClient.Constants.MAX_AUTH_RETRY_COUNT - 1)
                if will_retry:
                    Log.warning("Authentication timed out, but will retry.")
                else:
                    Log.error("Authentication timed out maximum number of times.")
                    raise Exception("Authentication timed out maximum number of times.")

        if response.status_code < 200 or response.status_code >= 300:
            Log.error(f"Authentication failed withs status code: {response.status_code}")
            raise TVDBAuthenticationException(
                f"Authentication failed with status code: {response.status_code}"
            )

        content = response.json()
        token = content.get("token")

        if token is None:
            Log.error("Failed to get token from login request")
            raise TVDBAuthenticationException("Failed to get token from login request")

        self.auth_token = token

        Log.info("Authenticated successfully")

    def get(self, url_path: str, *, timeout: float) -> Any:
        """Search for shows matching the name supplied.

        If no matching show is found, a NotFoundException will be thrown.
        """

        if url_path is None or url_path == "":
            raise AttributeError("An invalid URL path was supplied")

        self.authenticate()

        Log.info(f"GET: {url_path}")

        response = requests.get(
            self._expand_url(url_path), headers=self._construct_headers(), timeout=timeout
        )

        TVDBClient._check_errors(response)

        content = response.json()

        data = content.get("data")

        if data is None:
            raise NotFoundException(f"Could not get data for path: {url_path}")

        return data

    def get_paged(self, url_path: str, *, timeout: float) -> List[Any]:
        """Get paged data."""

        if url_path is None or url_path == "":
            raise AttributeError("An invalid URL path was supplied")

        self.authenticate()

        page = 0

        all_results: List[Any] = []

        while True:

            if page != 0:
                url_path += f"?page={page}"

            Log.info(f"GET: {url_path}")

            response = requests.get(
                self._expand_url(url_path), headers=self._construct_headers(), timeout=timeout
            )

            TVDBClient._check_errors(response)

            content = response.json()

            data = content.get("data")

            if data is None:
                raise NotFoundException(f"Could not get data for path: {url_path}")

            all_results += data

            links = content.get("links")

            if links is None:
                break

            if links.get("next"):
                Log.debug("Fetching next page")
                page = links["next"]
            else:
                break

        return all_results

    def search_show(self, show_name: str, *, timeout: float = 10.0) -> List[Show]:
        """Search for shows matching the name supplied.

        If no matching show is found, a NotFoundException will be thrown.
        """

        if show_name is None or show_name == "":
            return []

        encoded_name = urllib.parse.quote(show_name)

        Log.info(f"Searching for show: {show_name}")

        shows_data = self.get(f"search/series?name={encoded_name}", timeout=timeout)

        shows = []

        for show_data in shows_data:
            show = deserialize.deserialize(Show, show_data)
            shows.append(show)

        return shows

    def show_info(self, show_identifier: int, *, timeout: float = 10.0) -> Optional[Show]:
        """Get the full information for the show with the given identifier."""

        Log.info(f"Fetching data for show: {show_identifier}")

        show_data = self.get(f"series/{show_identifier}", timeout=timeout)

        return deserialize.deserialize(Show, show_data)

    def actors_from_show_id(self, show_identifier: int, timeout: float = 10.0) -> List[Actor]:
        """Get the actors in the given show."""

        Log.info(f"Fetching actors for show id: {show_identifier}")

        actor_data = self.get(f"series/{show_identifier}/actors", timeout=timeout)

        actors: List[Actor] = []

        for actor_data_item in actor_data:
            actors.append(deserialize.deserialize(Actor, actor_data_item))

        return actors

    def actors_from_show(self, show: Show, timeout: float = 10.0) -> List[Actor]:
        """Get the actors in the given show."""
        return self.actors_from_show_id(show.identifier, timeout=timeout)

    def episodes_from_show_id(self, show_identifier: int, timeout: float = 10.0) -> List[Episode]:
        """Get the episodes in the given show."""

        Log.info(f"Fetching episodes for show id: {show_identifier}")

        episode_data = self.get_paged(f"series/{show_identifier}/episodes", timeout=timeout)

        episodes: List[Episode] = []

        for episode_data_item in episode_data:
            episodes.append(deserialize.deserialize(Episode, episode_data_item))

        return episodes

    def episodes_from_show(self, show: Show, timeout: float = 10.0) -> List[Episode]:
        """Get the episodes in the given show."""
        return self.episodes_from_show_id(show.identifier, timeout=timeout)

    def episode_by_id(self, episode_identifier: int, timeout: float = 10.0) -> Episode:
        """Get the episode information from its ID."""

        Log.info(f"Fetching info for episode id: {episode_identifier}")

        episode_data = self.get(f"episodes/{episode_identifier}", timeout=timeout)

        print(episode_data)

        return deserialize.deserialize(Episode, episode_data)

    @staticmethod
    def _check_errors(response: requests.Response) -> Any:
        """Check an API response for errors."""

        if response.status_code >= 200 and response.status_code < 300:
            return

        Log.error(f"Bad response code from API: {response.status_code}")

        # Try and read the JSON. If we don't have it, we return the generic
        # exception type
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise TVDBException(f"Could not decode error response: {response.text}")

        # Try and get the error message so we can use it
        error = data.get("Error")

        # If we don't have it, just return the generic exception type
        if error is None:
            raise TVDBException(f"Could not get error information: {response.text}")

        if error == "Resource not found":
            raise NotFoundException(f"Could not find resource: {response.url}")

        raise TVDBException(f"Unknown error: {response.text}")
