"""This module contains the RSS parser implemented using the ElementTree XML API, parsing
RSS files into the corresponding entities."""
import xml.etree.ElementTree as XMLTree
from entities import Channel, Story


def isRSS(content: str) -> bool:
    """Returns if a given XML document is an RSS document by checking if the root has the RSS tag.

    Preconditions:
     - root is the root of a valid XML document tree.
    """
    root = XMLTree.fromstring(content)
    return root.tag == 'rss'


def parse(content: str) -> Channel:
    """Parse a given RSS document into a Channel entity.

    Preconditions:
     - content is a valid XML document following the RSS specification
    """
    channel = XMLTree.fromstring(content)[0]
    title = channel.findtext("title")
    description = channel.findtext("description")
    link = channel.findtext("link")

    return Channel(title=title,
                   url=link,
                   description=description,
                   stories=[])


def get_stories(content: str, cap: int) -> list[Story]:
    """Given an RSS document, parse and return a list of its stories."""
    root = XMLTree.fromstring(content)[0]
    stories = []

    item_list = root.findall('item')
    for i in range(0, min(len(item_list), cap)):
        story = _parse_story(item_list[i])
        if story is not None:
            stories.append(story)

    return stories


def _parse_story(element: XMLTree.Element) -> Story | None:
    """Parse a given <item> element into a story. If the title or description is missing, return None instead."""
    title = element.findtext("title")
    description = element.findtext("description")
    link = element.findtext("link")
    guid = element.findtext("guid")

    if title is None or description is None:
        return None
    return Story(title=title,
                 description=description,
                 link=link,
                 guid=guid)
