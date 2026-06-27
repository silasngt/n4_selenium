from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Cấu hình Chrome
    chrome_options = Options()
    # Tắt thông báo "Chrome is being controlled by automated test software" cho đẹp mắt khi Demo
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 

    # Tắt popup "Change your password / password found in data breach" vì phiền vl
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    # Tắt tính năng kiểm tra rò rỉ mật khẩu (Safe Browsing leak detection) qua flag
    chrome_options.add_argument("--disable-features=PasswordLeakDetection,SafetyCheck")

    # Khởi tạo driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5) # Chờ tối đa 5s nếu mạng chậm chưa load kịp HTML
    
    return driver