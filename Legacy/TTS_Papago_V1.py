from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys

# Install and initialize Chrome driver
chrome_driver = ChromeDriverManager().install()
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

# Get input from command line arguments
answer = ""
print(sys.argv)
for i, key in enumerate(sys.argv):
    if i != 0:
        answer += key + " "
print(answer)

# Exit program if no input provided
if answer == "":
    sys.exit(0)

# Navigate to translation page and input text
URL = "https://papago.naver.com/"
driver.get(URL)
time.sleep(2)

form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")
form.send_keys(answer)
time.sleep(2)

# Click translation button
xpath = "/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[4]/span[1]/span/span/button"
button = driver.find_element(By.XPATH, xpath)
button.click()

# Wait for translation to complete and close the browser
time.sleep(20)
driver.close()
