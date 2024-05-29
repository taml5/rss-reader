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
