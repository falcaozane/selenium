from selenium import webdriver
from selenium.webdriver.edge.service import Service
# Specify the path to your msedgedriver.exe
edge_driver_path = "E:\\QA\\selenium\\msedgedriver.exe"

#browser = webdriver.Chrome("C:\Drivers\network\chrome-win64.exe")
#browser =  webdriver.Edge("F:\edgedriver_win64\msedgedriver.exe")

# Create a Service object with the executable path
service = Service(executable_path=edge_driver_path)

# Initialize the Edge browser with the Service object
browser = webdriver.Edge(service=service)
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

browser.get(url)
print("Open Browser")
