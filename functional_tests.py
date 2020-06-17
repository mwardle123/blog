from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_cv_and_retrieve_it_later(self):
        # Checking out homepage
        self.browser.get('http://127.0.0.1:8000')

        # Check the homepage title
        self.assertIn('Matthew Wardle', self.browser.title)

        # Checking out the CV page
        self.browser.get('http://127.0.0.1:8000/cv')

        # Check the CV page title
        self.assertIn('CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)

        # Asked to enter a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a CV item'
        )

        # Type something into a text box
        inputbox.send_keys('Something')

        # When hitting enter, the page updates, and now the page lists the new something
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_cv_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Something' for row in rows),
            "New CV item did not appear in table"
        )

        # There is still a text box to add another item. Enter something else
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on the list

        # The site has generated a unique URL and it explains thos

        # Visit that URL to see CV is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

