import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.driver_factory import get_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    print("--- Bắt đầu chạy TC05: Sử dụng Chờ đợi thông minh ---")
    driver = get_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        
        # Login
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        ).send_keys("standard_user")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        ).send_keys("secret_sauce")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()   
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )
        print("[STEP] Đăng nhập thành công!")
        
        # Nhấn nút "Add to cart" cho Sauce Labs Backpack
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        print("[STEP] Đã thêm Sauce Labs Backpack vào giỏ hàng")
        
        # Nhấn nút "Add to cart" cho Sauce Labs Bike Light
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        ).click()
        print("[STEP] Đã thêm Sauce Labs Bike Light vào giỏ hàng")
        
        # Nhấn vào giỏ hàng
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )
        print("[STEP] Đã vào trang giỏ hàng!")
        
        # Nhấn nút Checkout
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )
        print("[STEP] Đã vào trang Checkout")
        
        # Nhập thông tin giao hàng
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys("thien")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        ).send_keys("menh")
        driver.find_element(By.ID, "postal-code").send_keys("700000")
        print("[STEP] Đã nhập thông tin giao hàng")
        
        # Nhấn Continue
        driver.find_element(By.ID, "continue").click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()
        print("[PASS] TC05: Đặt hàng thành công!")
        
    except Exception as e:
        print(f"[FAIL] TC05 gặp lỗi: {e}")
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    run_test()
