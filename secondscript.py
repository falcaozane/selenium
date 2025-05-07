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

url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
username_enter = "student"
Password_Enter = "Password123"
username = driver.find_element(By.ID, value="username")
username.send_keys(username_enter)
Password = driver.find_element(By.ID, value="password")
Password.send_keys(Password_Enter)
Submit = driver.find_element(By.ID, value="submit")
Submit.click()
Logout = driver.find_element(By.LINK_TEXT, value="Log out")
Logout_text = Logout.text
Expected_text = "Log out"
assert Logout_text == Expected_text

print("Session correct")

# You might want to add a driver.quit() at the end to close the browser
# driver.quit()