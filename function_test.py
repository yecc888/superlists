from selenium import webdriver
import unittest

class Testfirst(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #driver.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.driver.quit()

    def test_can_list(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn('TO-DO', self.driver.title)
        self.fail('test over')
        t = driver.title
        print(t)

if __name__ == '__main__':
    unittest.main()


