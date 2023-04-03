from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Translator:
    def __init__(self):
        # Install and initialize Chrome driver
        chrome_driver = ChromeDriverManager().install()
        service = Service(chrome_driver)
        self.driver = webdriver.Chrome(service=service)
    
    def translate(self, text):
        # Exit program if no input provided
        if text == "":
            sys.exit(0)

        # Navigate to translation page and input text
        URL = "https://papago.naver.com/"
        self.driver.get(URL)
        time.sleep(2)

        form = self.driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")
        form.send_keys(text)
        time.sleep(2)

        # Click translation button
        #xpath = "/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[4]/span[1]/span/span/button"
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_sound___2H-0Z')))
        button.click()

        # wait for the button to change state
        while 'active___3VPGL' in button.get_attribute('class'):
            time.sleep(1) # wait for 1 second
    
    def close(self):
        self.driver.close()

def main():
    translator = Translator()
    
    # Get input from command line arguments
    answer = " ".join(sys.argv[1:])
    print(answer)

    # Translate input and print result
    result = translator.translate(answer)

    translator.close()

if __name__ == "__main__":
    main()
