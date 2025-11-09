import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


# Specify the path to your msedgedriver.exe
edge_driver_path = "C:\\shush\\not in capgs interest\\selenium\\msedgedriver.exe"  # Replace with the actual path to your msedgedriver.exe

# Create a Service object
service = Service(executable_path=edge_driver_path)

# Initialize the Edge browser with the Service object
driver = webdriver.Edge(service=service)

url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(url)

driver.fullscreen_window()

title = driver.title
print(title)


username_enter = "student"
email_enter = "student@gmail.com"
mobile_enter = "9028921961"
dob_enter = "21-08-2003"

name = driver.find_element(By.ID, value="name")
name.send_keys(username_enter)
email = driver.find_element(By.ID, value="email")
email.send_keys(email_enter)

time.sleep(3)

gender = driver.find_element(By.XPATH,value="//label[text()='Male']/preceding-sibling::input[@type='radio']")
gender.click()
time.sleep(3)

mobile = driver.find_element(By.NAME,value="mobile")
mobile.send_keys(mobile_enter)
time.sleep(3)

dob = driver.find_element(By.XPATH,value="//input[@type='date']")
dob.send_keys(dob_enter)

time.sleep(3)

check_box = driver.find_element(By.ID, "hobbies")

if not check_box.is_selected():
    check_box.click()
    time.sleep(3)

time.sleep(10)