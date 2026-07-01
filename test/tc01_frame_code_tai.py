import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.driver_factory import get_driver
from selenium.webdriver.common.by import By
import time

def run_test():
    print("--- Bắt đầu chạy TC01: Login Thành Công ---")
    driver = get_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1) 
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2)
        assert "inventory.html" in driver.current_url
        print("[PASS] TC01: Đăng nhập thành công!")
        
    except Exception as e:
        print(f"[FAIL] TC01 gặp lỗi: {e}")
    finally:
        driver.quit()

# Cho phép test độc lập file này
if __name__ == "__main__":
    run_test()