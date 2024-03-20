import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AppSeleniumTest(unittest.TestCase):

	def setUp(self):
        	self.driver = webdriver.Chrome()

	def tearDown(self):
        	self.driver.quit()

	def test_home_page(self):
		self.driver.get("http://172.17.0.2/")  

		self.assertEqual("Weather Forecast", self.driver.title)

		location_input = self.driver.find_element(By.NAME, 'location')
		location_input.send_keys("new york")
		submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
		submit_button.click()
		forecast_heading = self.driver.find_element(By.TAG_NAME, 'h1')
		self.assertIn("Weekly Forecast for New York, NY, United States", forecast_heading.text)

		

		self.driver.implicitly_wait(5)  # Wait for the page to load the results
		time.sleep(3)
		search_again_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Search Again')]")
		search_again_button.click()
		time.sleep(3)
		location_input = self.driver.find_element(By.NAME, 'location')
		location_input.send_keys("Schnitzel")
		submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
		submit_button.click()
		forecast_heading = self.driver.find_element(By.TAG_NAME, 'h1')
		self.assertIn("Weekly Forecast for ERROR, INVALID COUNTRY/CITY", forecast_heading.text)

		time.sleep(3)


if __name__ == '__main__':
    unittest.main()

