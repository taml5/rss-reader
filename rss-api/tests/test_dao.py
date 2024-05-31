"""Test suite for the database access object."""
import unittest
from sqliteDAO import SQLiteDAO


class TestDAO(SQLiteDAO):
    """A subclass of SQLiteDAO used for testing."""

    def cleanup(self):
        """Close the database connection."""
        self.database.close()


class DAOTestSuite(unittest.TestCase):

    def test_get_urls(self):
        dao = TestDAO("test.db")
        urls = dao.get_urls()
        self.assertIn("BBC Top Stories", urls)
        self.assertIn("BBC Asia", urls)
        self.assertIn("NYTimes Tech", urls)
        dao.cleanup()

    def test_write_urls(self):
        dao = TestDAO("test.db")
        dao.write_url("TechRadar", "https://www.techradar.com/feeds/tag/computing")
        urls = dao.get_urls()
        self.assertIn("TechRadar", urls)
        self.assertEqual(urls["TechRadar"], "https://www.techradar.com/feeds/tag/computing")
        dao.cursor.execute("""DELETE FROM "urls" WHERE 'name' = 'TechRadar';""")
        dao.cleanup()

    def test_remove_url(self):
        dao = TestDAO("test.db")
        dao.remove_url("NYTimes Tech")

        urls = dao.get_urls()
        self.assertNotIn("NYTimes Tech", urls)
        dao.cursor.execute("""INSERT INTO "urls" (name, url)
                              VALUES ('NYTimes Tech', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml')""")
        dao.cleanup()


if __name__ == '__main__':
    unittest.main()
