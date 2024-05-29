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

    def __eq__(self, other):
        if self.guid is not None and other.guid is not None:
            return self.guid == other.guid
        else:
            return self.title == other.title or self.description == other.description


@dataclass
class Channel:
    """A dataclass representing a website from which RSS data is grabbed from.

    Attributes:
        title: The name of the channel.
        url: The URL to the HTML website corresponding to the channel.
        description: Phrase or sentence describing the channel.
    """
    title: str
    url: str
    description: str
    stories: list['Story']
