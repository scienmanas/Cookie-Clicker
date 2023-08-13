from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def TestStore():
    money = int(driver.find_element(By.ID,"money").text.replace(',',''))
    storeitems = driver.find_elements(By.CSS_SELECTOR,'#store > div')
    i = 0
    expensive = 0
    capture = storeitems[0]
    for item in storeitems:
        if i >= 8 :
            break 
        cost = int(item.find_element(By.TAG_NAME,'b').text.split('-')[1].strip().replace(',',''))
        if cost > expensive and cost <= money:
            expensive = cost
            capture = item
        i += 1
    capture.click()
            
        

options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
pause = 1
while True:
    if pause%40==0 :
        TestStore()
    cookie.click()
    pause+=1
    