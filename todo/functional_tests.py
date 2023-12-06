from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
            
        # Edtih has heard about a cool new online to-do app. She gos
        # to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices  the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        expectedText = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('To-Do', expectedText)
        

        # She is invited to enter a to-do item straitght a way
        inputbox = self.browser.find_element(By.ID,'add_new_item')
        self.asserEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is trying fly-fishing lures)
        inputbox.clear()
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == 'Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting her to add anothe item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')
        

        # The page updates again, and now shows both items on her list

        # Edith wonders wheater the site will remember her list. Then she sees
        # that the site has generated a unique URL for her == there is some
        # expalnatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep.
if __name__ == '__main__':
    unittest.main(warnings='ignore')