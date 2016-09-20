import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


class HmmerSearch(unittest.TestCase):
    hmmer_home_page = "http://www.ebi.ac.uk/Tools/hmmer/"

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_hmmer_home_page(self):
        driver = self.driver
        driver.get(self.hmmer_home_page)
        self.assertIn("HMMER", driver.title)

    def test_hmmer_search_example(self):
        browser = self.driver
        browser.get(self.hmmer_home_page)
        textarea = browser.find_element_by_id("seq")
        self.assertEqual("", textarea.text, "The textarea should be empty when landing in the homepage")
        browser.find_element_by_css_selector("#example").click()
        self.assertNotEqual("", textarea.text, "The textarea should NOT be empty after clicking the example link")
        self.click_link_and_wait(browser.find_element_by_id("subbutton"))
        title = browser.find_element_by_css_selector(".res_title h5")
        self.assertEqual("PHMMER Results", title.text, "The result title should be PHMMER Results")

    def tearDown(self):
        self.driver.close()

    def click_link_and_wait(self, link):
        link.click()

        def link_has_gone_stale():
            try:
                # poll the link with an arbitrary call
                link.find_elements_by_id('doesnt-matter')
                return False
            except StaleElementReferenceException:
                return True

        self.wait_for(link_has_gone_stale)

    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )


if __name__ == "__main__":
    unittest.main()
