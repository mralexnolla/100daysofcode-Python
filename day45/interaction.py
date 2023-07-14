from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "/Users/alexnolla/Desktop/pycharmpython/development/chromedriver"

webdriver_service = ChromeService(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=webdriver_service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# numbArticles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# numbArticles.click()

# linkText = driver.find_element(By.LINK_TEXT, 'Margaret Murray')
# linkText.click()

firstName = driver.find_element(By.NAME, 'fName')
lastName = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')


actions = ActionChains(driver)
actions.move_to_element(firstName)
actions.click()
actions.send_keys("salami")
actions.move_to_element(lastName)
actions.click()
actions.send_keys("ambigue")
actions.move_to_element(email)
actions.click()
actions.send_keys("shorthiliourgreat@gmail.com")
actions.send_keys(Keys.ENTER)
actions.perform()


input("Press Enter to close the browser...")
driver.close()
# driver.quit()