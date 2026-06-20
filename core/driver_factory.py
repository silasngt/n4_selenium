from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Cấu hình Chrome
    chrome_options = Options()
    # Tắt thông báo "Chrome is being controlled by automated test software" cho đẹp mắt khi Demo
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    
    # Khởi tạo driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5) # Chờ tối đa 5s nếu mạng chậm chưa load kịp HTML
    
    return driver