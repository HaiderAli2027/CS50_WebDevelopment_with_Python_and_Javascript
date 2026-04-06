import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class webpageTests(unittest.TestCase):
    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")
        increase.click()
        # Add assertions to verify the increase functionality
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        
        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()
        # Add assertions to verify the decrease functionality
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "0")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")

        for i in range(25):
            increase.click()
        # Add assertions to verify the multiple increase functionality
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "25")

if __name__ == "__main__":
    unittest.main()