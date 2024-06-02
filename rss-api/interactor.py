"""This module contains the main backend interactor."""
from interfaces.dao import DataAccessObject
from entities import Channel
from interfaces import parser
import requests


def build_RSS(records: dict[str, str]) -> list[Channel]:
    """Build a list of Channels from the database records.

    :param records: A dictionary of url names as keys, and the RSS url as the value.
    :returns: A list of Channels corresponding to each url.
    """
    channels = []

    for record in records:
        try:
            url = records[record]
            response = requests.get(url)
            text = response.text
            if not parser.isRSS(text):
                pass
            channels.append(parser.parse(text, record, url))
        except requests.RequestException as e:
            print(e.response)
            pass

    return channels


class Interactor:
    """The main back-end class responsible for handling use cases.

    Attributes:
        channelDAO: The database access object for storing RSS channel urls.
        channels: The list of currently tracked RSS Channels.
        max_stories: The maximum number of loaded stories per Channel.
    """
    channelDAO: DataAccessObject
    channels: list[Channel]
    max_stories: int

    def __init__(self, dao: DataAccessObject, channels: list[Channel], story_cap: int):
        self.channelDAO = dao
        self.channels = channels
        self.max_stories = story_cap

    def add_channel(self, name: str, url: str) -> bool:
        """Start tracking an RSS channel.

        :param name: The given name of the RSS channel.
        :param url: The RSS url for the channel.
        :return: Whether the operation was successful.
        """
        if not self.channelDAO.write_url(name, url):
            # log db failure
            return False
        try:
            response = requests.get(url)
            if not parser.isRSS(response.text):
                return False
            self.channels.append(parser.parse(response.text, name, url))
            return True
        except requests.RequestException as e:
            print(e)

    def remove_channel(self, name: str, url: str) -> bool:
        """Remove an RSS channel from being tracked, by deleting it from the database and the in-memory array.

        :param name: The given name of the channel.
        :param url: The RSS url of the channel.
        :return:  Whether the operation was successful.
        """
        for i in range(len(self.channels)):
            if self.channels[i].rss_url == url:
                if not self.channelDAO.remove_url(name):
                    return False

                self.channels.pop(i)
                return True

        raise Exception

    def build_channels(self) -> None:
        """Load the associated stories for each tracked channel."""
        for channel in self.channels:
            self.build_stories(channel)

    def build_stories(self, channel: Channel) -> None:
        """Load the associated stories for a channel.

        :param channel: The RSS Channel for which stories are to be loaded.
        """
        try:
            response = requests.get(channel.rss_url)
            channel.stories = parser.get_stories(response.text, self.max_stories)
        except requests.RequestException as e:
            print(e)
