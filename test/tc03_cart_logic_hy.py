import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.driver_factory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# ==============================================================================
# HÀM BỔ TRỢ: ĐĂNG NHẬP
# ==============================================================================
def login_to_saucedemo(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# ==============================================================================
# HÀM BỔ TRỢ: XỬ LÝ CHUỖI GIÁ TIỀN
# ==============================================================================
def parse_price_to_float(price_text):
    match = re.search(r"[-+]?\d*\.\d+|\d+", price_text)
    if match:
        return float(match.group())
    return 0.0

# ==============================================================================
# TẦNG KIỂM THỬ CHÍNH
# ==============================================================================
def run_test():
    print("\n--- Bắt đầu chạy TC03: Kiểm thử Logic Tính toán & Xác minh Tài chính ---")
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Bước 1: Tiền điều kiện (Đăng nhập)
        login_to_saucedemo(driver, "standard_user", "secret_sauce")
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        time.sleep(1.5)
        
        # Bước 2: Định vị lấy giá tiền của 3 sản phẩm trên giao diện
        price_item1_text = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']").text
        price_item2_text = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']").text
        price_item3_text = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']").text
        
        price_1 = parse_price_to_float(price_item1_text)
        price_2 = parse_price_to_float(price_item2_text)
        price_3 = parse_price_to_float(price_item3_text)
        
        expected_total = price_1 + price_2 + price_3
        print(f"[INFO] Giá Sp1: {price_1} | Giá Sp2: {price_2} | Giá Sp3: {price_3}")
        print(f"[INFO] Tổng số tiền tính toán trên lý thuyết (Expected): ${expected_total}")
        
        # Bước 3: Click thêm 3 sản phẩm này vào giỏ hàng
        print("[STEP] Tiến hành thêm lần lượt 3 sản phẩm vào giỏ...")
        item1_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        item1_btn.click()
        time.sleep(1)
        
        item2_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        item2_btn.click()
        time.sleep(1)
        
        item3_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        item3_btn.click()
        time.sleep(2) 
        
    
        # Bước 4: Vào Giỏ hàng và tiến hành Checkout
        print("[STEP] Vào giỏ hàng...")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2) 
        
        print("[STEP] Nhấn nút Checkout...")
        checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()
        time.sleep(2) 
        
        # Bước 5: Điền thông tin thông tin Checkout
        print("[STEP] Nhập thông tin thanh toán giả lập...")
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        driver.find_element(By.ID, "first-name").send_keys("Nguyen")
        time.sleep(0.5) 
        driver.find_element(By.ID, "last-name").send_keys("Tam Hy")
        time.sleep(0.5)
        driver.find_element(By.ID, "postal-code").send_keys("70000")
        time.sleep(1.5) 
        
        print("[STEP] Nhấn nút Continue...")
        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()
        time.sleep(3) 
        
        # Bước 6: Lấy giá trị "Item total" thực tế hiển thị trên Web
        print("[STEP] Chờ hệ thống hiển thị hóa đơn tổng tiền...")
        actual_total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_subtotal_label")))
        actual_total_text = actual_total_element.text
        actual_total = parse_price_to_float(actual_total_text)
        print(f"[INFO] Tổng số tiền hệ thống hiển thị thực tế (Actual): ${actual_total}")
        
        # Bước 7: Tiến hành đối chiếu logic tài chính
        print("[STEP] Thực hiện so sánh đối chiếu logic tài chính...")
        assert round(expected_total, 2) == round(actual_total, 2), f"Lỗi Logic! Tổng tính toán là {expected_total} nhưng web hiển thị {actual_total}"
        
        print(f"[PASS] TC03: Logic tính toán hoàn toàn CHÍNH XÁC (${expected_total} == ${actual_total})")
        time.sleep(3) 
        
    except Exception as e:
        print(f"[FAIL] TC03 gặp lỗi: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()