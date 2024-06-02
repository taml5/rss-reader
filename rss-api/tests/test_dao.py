"""Test suite for the database access object."""
import unittest
import sqlite3
from sqliteDAO import SQLiteDAO


class DAOTestSuite(unittest.TestCase):

    def test_get_urls(self):
        dao = SQLiteDAO("test.db")
        urls = dao.get_urls()
        self.assertIn("BBC Top Stories", urls)
        self.assertIn("BBC Asia", urls)
        self.assertIn("NYTimes Tech", urls)

    def test_write_urls(self):
        dao = SQLiteDAO("test.db")
        dao.write_url("TechRadar", "https://www.techradar.com/feeds/tag/computing")
        urls = dao.get_urls()
        self.assertIn("TechRadar", urls)
        self.assertEqual(urls["TechRadar"], "https://www.techradar.com/feeds/tag/computing")

        database = sqlite3.connect("test.db")
        cursor = database.cursor()
        cursor.execute("""DELETE FROM "urls" WHERE name = 'TechRadar';""")
        database.commit()
        database.close()

    def test_remove_url(self):
        dao = SQLiteDAO("test.db")
        dao.remove_url("NYTimes Tech")

        urls = dao.get_urls()
        self.assertNotIn("NYTimes Tech", urls)

        database = sqlite3.connect("test.db")
        cursor = database.cursor()
        cursor.execute("""INSERT INTO "urls" (name, url)
                                      VALUES ('NYTimes Tech', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml');""")
        database.commit()
        database.close()


if __name__ == '__main__':
    unittest.main()
