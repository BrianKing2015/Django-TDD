from selenium import webdriver
import unittest

class NewVistorTest (unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app she goes to check it out
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn ('To-Do', self.browser.title)
        self.fail('Finish the test!')

# She is invited to enter a to-do item right now
# she types "Buy peacock feathers" into text box

# When she hits enter, the page updates and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item
# she enters "Use peacock feathers to make a fly"

# The page updates again, now it shows both items

# Edtih wonders whether the site will remember this if she leaves
# Then she sees that the site has generated a unique URL for her
# There is some explanatory text to that effect.

# She visits the URL - her to-do list is still there.
# Satisfie, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
