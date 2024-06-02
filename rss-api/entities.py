"""This module contains all the entities used by the RSS api."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Story:
    """A dataclass representing a single RSS element.

    Attributes:
        title: The title of the item.
        description: The item synopsis.
        link: The URL of the item.
        guid: A string that uniquely identifies the item.
    """
    title: str
    description: str
    link: Optional[str]
    guid: Optional[str]

    def serialise(self):
        """Return a dictionary representation of this Story."""
        return {
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'guid': self.guid
        }


@dataclass
class Channel:
    """A dataclass representing a website from which RSS data is grabbed from.

    Attributes:
        title: The name of the channel.
        url: The URL to the HTML website corresponding to the channel.
        rss_url: The RSS URL.
        description: Phrase or sentence describing the channel.
        stories: An ordered list of stories from this channel.
    """
    given_name: str
    title: str
    url: str
    rss_url: str
    description: str
    stories: list[Story]

    def serialize(self) -> dict:
        """Return a dictionary representation of this Channel."""
        return {
            'given_name': self.given_name,
            'title': self.title,
            'url': self.url,
            'rss_url': self.rss_url,
            'description': self.description,
            'stories': [story.serialise() for story in self.stories]
        }
