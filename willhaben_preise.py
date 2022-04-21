from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
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

result = driver.find_elements(By.XPATH, value = "//div[@class = 'MultiLineTextTruncation__MultiLineTextTruncationInner-sc-8560bl-1 bCUUvz']")

article_names = []
for el in result:
    article_names.append(el.text)
article_names = article_names[-5:]

result = driver.find_elements(By.XPATH, value = "//span[@class = 'Text-sc-10o2fdq-0 fbpghM']")

article_ids = []
for el in result:
    el = el.get_attribute("data-testid")
    el = el.split("-")
    article_ids.append(el[0])
article_ids = article_ids[-5:]

old_prices = []
for el in result:
    el = el.text
    el = el.split()
    old_prices.append(int(el[1]))
old_prices = old_prices[-5:]

dict_articles = {k: {x: y} for k, x, y in zip(article_ids, article_names, old_prices)}

for id, values in list(dict_articles.items()):
    for key in values:
        discount = float(input("Assign discount (as percentage e. g. 0.25, for no discount type 0) to %s (%d€) : " %(key, values[key])))
        if discount != 0:
            new_price = int(values[key] - values[key] * discount)
            values[key] = new_price
        else: 
            dict_articles.pop(id)


for id, values in list(dict_articles.items()):
    for key in values:
        driver.find_element(By.XPATH, value = "//button [@data-testid = '%s-context-menu']" %str(id)).click()
        driver.find_element(By.XPATH, value = "//button [@data-testid= 'ad-contextlink-editText']").click()
        driver.find_element(By.ID, value="ad_price").clear()
        driver.find_element(By.ID, value="ad_price").send_keys(values[key])
        time.sleep(2)
        driver.find_element(By.XPATH, value = "//button [@name= '_eventId_proceed']").click()
        time.sleep(10)
        driver.get("https://www.willhaben.at/iad/myprofile/myadverts?page=" + max_pages)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

time.sleep(10), driver.quit()