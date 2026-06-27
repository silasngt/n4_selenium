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
    print("--- Bat dau chay TC05: Them item vao gio hang ---")
    driver = get_driver()
    try:
        # Buoc 1: Mo trang web
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        
        # Buoc 2: Login
        print("[STEP] Dang nhap...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        ).send_keys("standard_user")
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        ).send_keys("secret_sauce")
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()   
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )
        print("[STEP] Dang nhap thanh cong!")
        time.sleep(1)
        
        # Buoc 3: Them Sauce Labs Backpack
        print("[STEP] Them Sauce Labs Backpack...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        time.sleep(1)
        print("[STEP] Da them Sauce Labs Backpack vao gio hang")
        
        # Buoc 4: Them Sauce Labs Bike Light
        print("[STEP] Them Sauce Labs Bike Light...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        ).click()
        time.sleep(1)
        print("[STEP] Da them Sauce Labs Bike Light vao gio hang")
        
        # Buoc 5: Vao gio hang
        print("[STEP] Vao gio hang...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )
        print("[STEP] Da vao trang gio hang!")
        
        # Buoc 6: Nhan Checkout
        print("[STEP] Nhan Checkout...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )
        print("[STEP] Da vao trang Checkout")
        
        # Buoc 7: Nhap thong tin giao hang
        print("[STEP] Nhap thong tin giao hang...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys("thien")
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        ).send_keys("menh")
        time.sleep(2)
        
        driver.find_element(By.ID, "postal-code").send_keys("700000")
        time.sleep(2)
        print("[STEP] Da nhap thong tin giao hang")
        
        # Buoc 8: Nhan Continue
        print("[STEP] Nhan Continue...")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-step-two.html")
        )
        print("[STEP] Da vao trang xem lai don hang")
        
        # Buoc 9: Nhan Finish
        print("[STEP] Nhan Finish...")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-complete.html")
        )
        print("[PASS] TC05: Dat hang thanh cong!")
        
    except Exception as e:
        print(f"[FAIL] TC05 gap loi: {e}")
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    run_test()
