from test import HmmerWebTest, click_link_and_wait
from selenium.common.exceptions import NoSuchElementException
# import time

class HmmerExampleTestCase(HmmerWebTest):
    def test_hmmer_search_example(self):
        browser = self.driver
        browser.get(self.hmmer_home_page)
        try:
            textarea = browser.find_element_by_id("textarea_seq")
        except NoSuchElementException:
            textarea = browser.find_element_by_id("seq")
        self.assertEqual("", textarea.text, "The textarea should be empty when landing in the homepage")
        browser.find_element_by_css_selector("#example").click()
        self.assertNotEqual("", textarea.text, "The textarea should NOT be empty after clicking the example link")

        try:
          browser.find_element_by_css_selector("#cookie-banner button").click()
        except: pass

        b = browser.find_element_by_id("subbutton")
        browser.execute_script("return arguments[0].scrollIntoView();", b)
        browser.execute_script("window.scrollBy(0, -150);")
        click_link_and_wait(b)

        title = browser.find_element_by_css_selector("div.row div.columns>h5")
        self.assertEqual("PHMMER Results", title.text, "The result title should be PHMMER Results")
