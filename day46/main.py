from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/Users/alexnolla/Desktop/pycharmpython/development/chromedriver"
webdriver_service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=webdriver_service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

wait = WebDriverWait(driver, 60)
checkBox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']")))

action = ActionChains(driver)
action.move_to_element(checkBox)
action.click()
action.perform()

# store = driver.find_elements(By.ID, "store")


# action = ActionChains(driver)
# action.move_to_element(cookie)


input("Press Enter to close the browser...")
driver.close()
