import unittest
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
        dao.write_url("https://www.techradar.com/feeds/tag/computing", "TechRadar")
        urls = dao.get_urls()
        self.assertIn("TechRadar", urls)
        self.assertEqual(urls["TechRadar"], "https://www.techradar.com/feeds/tag/computing")
        dao.cursor.execute("""DELETE FROM "urls" WHERE 'name' = 'TechRadar';""")

    def test_remove_url(self):
        dao = SQLiteDAO("test.db")
        dao.remove_url("NYTimes Tech")

        urls = dao.get_urls()
        self.assertNotIn("NYTimes Tech", urls)
        dao.cursor.execute("""INSERT INTO "urls" (name, url)
                              VALUES ('NYTimes Tech', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml')""")


if __name__ == '__main__':
    unittest.main()
