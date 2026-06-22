import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.driver_factory import get_driver
from selenium.webdriver.common.by import By
import time

def run_test():
    print("--- Bắt đầu chạy TC02: Login Thất Bại ---")
    driver = get_driver()

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text

        assert "Username and password do not match" in error_message

        print("[PASS] TC02: Hiển thị thông báo lỗi chính xác!")

    except Exception as e:
        print(f"[FAIL] TC02 gặp lỗi: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()