from test import HmmerWebTest, click_link_and_wait

class HmmerExampleTestCase(HmmerWebTest):
    def test_hmmer_search_example(self):
        browser = self.driver
        browser.get(self.hmmer_home_page)
        textarea = browser.find_element_by_id("seq")
        self.assertEqual("", textarea.text, "The textarea should be empty when landing in the homepage")
        browser.find_element_by_css_selector("#example").click()
        self.assertNotEqual("", textarea.text, "The textarea should NOT be empty after clicking the example link")

        browser.find_element_by_css_selector(".close-button").click()

        click_link_and_wait(browser.find_element_by_id("subbutton"))
        title = browser.find_element_by_css_selector("div.row div.columns>h5")
        self.assertEqual("PHMMER Results", title.text, "The result title should be PHMMER Results")
