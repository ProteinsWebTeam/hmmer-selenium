from test import HmmerWebTest


class HmmerHomePageTestCase(HmmerWebTest):
    def test_hmmer_home_page(self):
        driver = self.driver
        driver.get(self.hmmer_home_page)
        self.assertIn("HMMER", driver.title)

