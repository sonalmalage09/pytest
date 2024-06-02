import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# links = driver.find_elements(By.TAG_NAME,"a")
# for link in links:
#     if link.text == 'Open Tab':
#         time.sleep(1)
#         link.send_keys(Keys.CONTROL+Keys.RETURN)
#         time.sleep(1)
#         driver.switch_to.window(driver.window_handles[1])
#         course_link = WebDriverWait(driver, 10).
#         until(EC.presence_of_element_located((By.LINK_TEXT, "Courses")))
#         time.sleep(1)
#         course_link.click()
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
element = driver.find_element(By.ID,"mousehover")
driver.execute_script("arguments[0].scrollIntoView();", element)
# Create an ActionChains object
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"mousehover")))
actions = ActionChains(driver)
# Perform a series of actions
actions.move_to_element(element).click().perform()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Top']")))
ele2 = driver.find_element(By.XPATH, "//a[normalize-space()='Top']")
actions.click(ele2).perform()
driver.quit()
