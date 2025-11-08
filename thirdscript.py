import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Specify the path to your msedgedriver.exe
edge_driver_path = "E:\\QA\\selenium\\msedgedriver.exe"  # Replace with the actual path to your msedgedriver.exe

# Create a Service object
service = Service(executable_path=edge_driver_path)

# Initialize the Edge browser with the Service object
driver = webdriver.Edge(service=service)

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)

time.sleep(5)

driver.fullscreen_window()

title = driver.title
print(title)

username_enter = "Admin"
Password_Enter = "admin123"

username = driver.find_element(By., value="username")
username.send_keys(username_enter)
Password = driver.find_element(By.name, value="password")
Password.send_keys(Password_Enter)
# Submit = driver.find_element(By.ID, value="submit")
# Submit.click()