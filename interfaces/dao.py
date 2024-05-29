"""This module contains the abstract base class defining the data access interface."""
from abc import ABC


class DataAccessObject(ABC):
    """The data access object, used to access ."""

    def write_url(self, url: str, name: str) -> bool:
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

    def get_urls(self) -> set[tuple[str, str]]:
        """
        Return tuples consisting of the name of the RSS channel, and its url.

        :return: A set of 2-tuples. The first value is the name of the RSS channel, and the second is
                 the url of the channel.
        """
        raise NotImplementedError
