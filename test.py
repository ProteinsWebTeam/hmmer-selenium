import unittest
from selenium import webdriver


class HmmerSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.ebi.ac.uk/Tools/hmmer/")
        self.assertIn("HMMER", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
