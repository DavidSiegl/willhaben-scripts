from multiprocessing import Value
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

driver.get('https://sso.willhaben.at/auth/realms/willhaben/protocol/openid-connect/auth?response_type=code&client_id=bbx-bff&scope=openid&state=fGi_5ww27bGSJ3_6J-t5HjUi8qcrIbJ7hAev7flL_oA%3D&redirect_uri=https://www.willhaben.at/webapi/oauth2/code/sso&nonce=9AAPIW3uAQyir-_1i_3syEdJ_K12zmeNb8Zwdros-iE')
driver.find_element(By.ID, value="email").send_keys(username)
driver.find_element(By.ID, value="password").send_keys(password)
driver.find_element(By.NAME, value="login").click()
driver.find_element(By.ID, value="didomi-notice-agree-button").click()
driver.get("https://www.willhaben.at/iad/myprofile/myadverts?page=1")

max_pages = driver.find_elements(By.XPATH, value="//a[contains(@aria-current,'page')]")
max_pages = str(len(max_pages))
driver.get("https://www.willhaben.at/iad/myprofile/myadverts?page=" + max_pages)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

while driver.find_element(By.NAME, value="republish") != []:
    driver.find_element(By.NAME, value="republish").click()
    time.sleep(2)
    driver.find_element(By.ID, value="saveAndContinueId").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, value="saveAndContinueId").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try: 
        if driver.find_element(By.NAME, value="deliveryOption") != []:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element(By.ID, value="saveAndContinueId").click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element(By.ID, value="saveAndContinueId").click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element(By.NAME, value="_eventId_payAndPublish").click()
            time.sleep(10)
            driver.get("https://www.willhaben.at/iad/myprofile/myadverts?page=" + max_pages)
    except NoSuchElementException:
            driver.find_element(By.ID, value="saveAndContinueId").click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element(By.NAME, value="_eventId_payAndPublish").click()
            time.sleep(10)
            driver.get("https://www.willhaben.at/iad/myprofile/myadverts?page=" + max_pages)

time.sleep(10), driver.close()
