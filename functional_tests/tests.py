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
        self.assertIn('Matthew Wardle', self.browser.title)
        header_text = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertIn('Matthew Wardle', header_text)

        # Check the CV Edit page title
        self.browser.get(self.live_server_url + '/cv/edit')
        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Edit CV', title_text)


        # Input Name
        namebox = self.browser.find_element_by_name('name')
        self.assertEqual(
            namebox.get_attribute('placeholder'),
            ''
        )
        namebox.send_keys('Matthew Wardle')

        # Input Address
        addressbox = self.browser.find_element_by_name('address')
        self.assertEqual(
            addressbox.get_attribute('placeholder'),
            ''
        )
        addressbox.send_keys('58 Dereham Road, Mattishall, Norfolk, NR20 3NS')

        # Input Mobile Number
        mobilebox = self.browser.find_element_by_name('mobile_number')
        self.assertEqual(
            mobilebox.get_attribute('placeholder'),
            ''
        )
        mobilebox.send_keys('07455706343')

        # Input Email
        emailbox = self.browser.find_element_by_name('email')
        self.assertEqual(
            emailbox.get_attribute('placeholder'),
            ''
        )
        emailbox.send_keys('mwardle1000@gmail.com')

        # Input Personal Profile
        profilebox = self.browser.find_element_by_name('personal_profile')
        self.assertEqual(
            profilebox.get_attribute('placeholder'),
            ''
        )
        profilebox.send_keys('A hard-working, responsible and adaptable Computer Science student.')

        # Save Form
        savebutton = self.browser.find_element_by_xpath("//button[@type='submit']")
        savebutton.click()

        # Check user is redirected to CV home page after submitting form
        self.assertIn('Matthew Wardle', self.browser.title)
        header_text = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertIn('Matthew Wardle', header_text)

        # Check name displays in correct place on page
        nametesttext = self.browser.find_element_by_xpath("//p[b = 'Name:']").text
        name = nametesttext.split(":")[-1].strip()
        self.assertEqual('Matthew Wardle', name)

        # Check address displays in correct place on page
        addresstesttext = self.browser.find_element_by_xpath("//p[b = 'Address:']").text
        address = addresstesttext.split(":")[-1].strip()
        self.assertEqual('58 Dereham Road, Mattishall, Norfolk, NR20 3NS', address)

        # Check mobile number displays in correct place on page
        mobiletesttext = self.browser.find_element_by_xpath("//p[b = 'Mobile Number:']").text
        mobile_number = mobiletesttext.split(":")[-1].strip()
        self.assertEqual('07455706343', mobile_number)

        # Check email displays in correct place on page
        emailtesttext = self.browser.find_element_by_xpath("//p[b = 'Email:']").text
        email = emailtesttext.split(":")[-1].strip()
        self.assertEqual('mwardle1000@gmail.com', email)

        # Check personal profile displays in correct place on page
        profiletesttext = self.browser.find_element_by_xpath("//p[b = 'Personal Profile:']").text
        personal_profile = profiletesttext.split(":")[-1].strip()
        self.assertEqual('A hard-working, responsible and adaptable Computer Science student.', personal_profile)

        # Check new category page loads
        self.browser.get(self.live_server_url + '/cv/edit')
        add_category_button = self.browser.find_element_by_xpath('//*[text()="Add New Category"]')
        add_category_button.click()
        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Add New Category', title_text)

        # Input new category
        categorybox = self.browser.find_element_by_name('title')
        self.assertEqual(
            categorybox.get_attribute('placeholder'),
            ''
        )
        categorybox.send_keys('Work Experience')
        sendbutton = self.browser.find_element_by_xpath("//button[@type='submit']")
        sendbutton.click()

        # Check submitting new category redirects to edit page
        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Edit CV', title_text)

        # Check new category appears on edit page
        response = self.client.get('/cv/edit/')
        self.assertIn('Work Experience', response.content.decode())

        # Input text for new category
        work_experience_button = self.browser.find_element_by_xpath('//*[text()="Work Experience"]')
        work_experience_button.click()
        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Work Experience', title_text)
        textbox = self.browser.find_element_by_name('text')
        self.assertEqual(
            textbox.get_attribute('placeholder'),
            ''
        )
        textbox.send_keys('I did some work experience.')
        sendbutton = self.browser.find_element_by_xpath("//button[@type='submit']")
        sendbutton.click()

        # Check submitting text for category redirects to edit page
        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Edit CV', title_text)

        # Check title and text for new category appears on home page
        response = self.client.get('/cv/')
        self.assertIn('Work Experience', response.content.decode())
        self.assertIn('I did some work experience.', response.content.decode())




