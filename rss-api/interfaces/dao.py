"""This module contains the abstract base class defining the data access interface."""
from abc import ABC


class DataAccessObject(ABC):
    """The data access object, used to access ."""

    def write_url(self, name: str, url: str) -> bool:
        """
        Write an RSS channel to the database.

        :param name: The name of the RSS channel to be written.
        :param url: The URL of the RSS channel.
        :return: Whether the insertion was successful or not.
        """
        raise NotImplementedError

    def remove_url(self, name: str) -> bool:
        """
        Remove an RSS channel from the database.

        :param name: The name of the RSS channel to be removed.
        :return: Whether the deletion was successful or not.
        """
        raise NotImplementedError

    def get_urls(self) -> dict[str, str]:
        """
        Return a dictionary of RSS urls.

        :return: A dictionary consisting of the name of an RSS channel as a key, and its url as the value.
        """
        raise NotImplementedError
