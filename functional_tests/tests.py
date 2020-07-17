from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_cv_and_retrieve_it_later(self):
        # Checking out homepage
        self.browser.get(self.live_server_url)

        # Check the homepage title
        self.assertIn('Matthew Wardle', self.browser.title)

        # Checking out the CV page
        self.browser.get(self.live_server_url + '/cv')

        # Check the CV page title
        self.assertIn('Matthew Wardle CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Matthew Wardle CV', header_text)

        # Edit
        self.browser.get(self.live_server_url + '/cv/edit')

        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Edit CV', title_text)

        namebox = self.browser.find_element_by_name('name')
        self.assertEqual(
            namebox.get_attribute('placeholder'),
            ''
        )
        namebox.send_keys('Matthew Wardle')

        namebox = self.browser.find_element_by_name('addresses')
        namebox.send_keys('Matthew Wardle')

        namebox = self.browser.find_element_by_name('mobile_number')
        namebox.send_keys('Matthew Wardle')

        namebox = self.browser.find_element_by_name('email')
        namebox.send_keys('Matthew Wardle')

        namebox = self.browser.find_element_by_name('personal_profile')
        namebox.send_keys('Matthew Wardle')

        savebutton = self.browser.find_element_by_xpath("//button[@type='submit']")
        savebutton.click()

        self.assertIn('Matthew Wardle CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Matthew Wardle CV', header_text)

        testtext = self.browser.find_element_by_xpath("//p[b = 'Name:']").text
        name = testtext.split(":")[-1].strip()
        self.assertEqual('Matthew Wardle', name)

        
