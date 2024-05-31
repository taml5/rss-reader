"""Test suite for the interactor layer using a mock DAO. This suite requires an internet connection
to function properly."""
import unittest
from interactor import Interactor
from entities import Channel
from interfaces.dao import DataAccessObject

channels = [
    Channel(title='BBC News',
            url='https://www.bbc.co.uk/news',
            rss_url='https://feeds.bbci.co.uk/news/rss.xml',
            description='BBC News - News Front Page',
            stories=[]),
    Channel(title='BBC News',
            url='https://www.bbc.co.uk/news/world/asia',
            rss_url='https://feeds.bbci.co.uk/news/world/asia/rss.xml',
            description='BBC News - Asia',
            stories=[]),
    Channel(title='NYT > Technology',
            url='https://www.nytimes.com/section/technology',
            rss_url='https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
            description='',
            stories=[]),
]


class MockDAO(DataAccessObject):
    """A mock in-memory DAO.

    Attributes:
        channels: The in-memory representation of the database of channels as a dictionary,
                  consisting of the name as the key and the url as the value.
    """
    channels: dict[str, str]

    def __init__(self):
        self.channels = {
            "BBC Top Stories": "https://feeds.bbci.co.uk/news/rss.xml",
            "BBC Asia": "https://feeds.bbci.co.uk/news/world/asia/rss.xml",
            "NYTimes Tech": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
        }

    def get_urls(self) -> dict[str, str]:
        return self.channels

    def write_url(self, name: str, url: str) -> bool:
        if name in self.channels:
            return False

        self.channels[name] = url
        return True

    def remove_url(self, name: str) -> bool:
        if name not in self.channels:
            return False

        self.channels.pop(name)
        return True


class InteractorTestSuite(unittest.TestCase):
    def test_init_interactor(self):
        dao = MockDAO()
        Interactor(dao, channels, 5)

    def test_build(self):
        dao = MockDAO()
        interactor = Interactor(dao, channels, 5)
        interactor.build_channels()
        for channel in interactor.channels:
            self.assertNotEqual(len(channel.stories), 0)
            self.assertLessEqual(len(channel.stories), 5)

    def test_add(self):
        dao = MockDAO()
        interactor = Interactor(dao, channels, 5)
        interactor.add_channel("TechCrunch", "https://feeds.feedburner.com/TechCrunch/")
        self.assertIn("TechCrunch", dao.channels)
        self.assertEqual(len(interactor.channels), 4)
        self.assertEqual(interactor.channels[3].rss_url, "https://feeds.feedburner.com/TechCrunch/")


if __name__ == '__main__':
    unittest.main()
