from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_cv_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_cv_and_retrieve_it_later(self):
        # Checking out homepage
        self.browser.get(self.live_server_url)

        # Check the homepage title
        self.assertIn('Matthew Wardle', self.browser.title)

        # Checking out the CV page
        self.browser.get(self.live_server_url + '/cv')

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
        self.check_for_row_in_list_table('1: Something')
            
        # There is still a text box to add another item. Enter something else
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Something else')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on the list
        self.check_for_row_in_list_table('1: Something')
        self.check_for_row_in_list_table('2: Something else')

        # The site has generated a unique URL and it explains this

        # Visit that URL to see CV is still there.
