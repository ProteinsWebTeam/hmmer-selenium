import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )


def click_link_and_wait(link):
    link.click()

    def link_has_gone_stale():
        try:
            # poll the link with an arbitrary call
            link.find_elements_by_id('doesnt-matter')
            return False
        except StaleElementReferenceException:
            return True

    wait_for(link_has_gone_stale)


class HmmerWebTest(unittest.TestCase):
    hmmer_home_page = "http://wwwdev.ebi.ac.uk/Tools/hmmer/"

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
