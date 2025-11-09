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

url = "https://the-internet.herokuapp.com/dropdown"
driver.get(url)


time.sleep(5)

dropdown_option_1 = driver.find_element(By.XPATH,"//select[@id='dropdown']/option[@value='1']")

dropdown_option_2 = driver.find_element(By.XPATH,"//select[@id='dropdown']/option[@value='2']")

dropdown_option_1.click()

time.sleep(3)

dropdown_option_2.click()

time.sleep(5)