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

url = "https://www.tutorialspoint.com/selenium/practice/check-box.php"
driver.get(url)

time.sleep(3)

driver.fullscreen_window()


time.sleep(10)

