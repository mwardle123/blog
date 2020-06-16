from selenium import webdriver
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
        self.fail('Finish the test!')

        # Asked to enter a new item

        # Type something into a text box

        # When hitting enter, the page updates, and now the page lists the new something

        # There is still a text box to add another item. Enter something else

        # The page updates again, and now shows both items on the list

        # The site has generated a unique URL and it explains thos

        # Visit that URL to see CV is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

