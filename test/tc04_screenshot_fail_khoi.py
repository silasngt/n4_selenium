import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.driver_factory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def run_test():
    print("--- Bắt đầu chạy TC04: Lọc sản phẩm + Thanh toán ---")
    driver = get_driver()
    try:
        #1. Mở trang và đăng nhập
        driver.get("https://www.saucedemo.com/")
        time.sleep(3) 
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(4)
        assert "inventory.html" in driver.current_url
        print("[PASS] TC04: Đăng nhập thành công!")

        # 2. Lọc sản phẩm theo A-Z
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        select = Select(sort_dropdown)
        select.select_by_value("az")  # Lọc A-Z
        time.sleep(3)
        
        
        items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        item_names = [item.text for item in items]
        print(f"Danh sách sản phẩm sau khi lọc A-Z: {item_names}")
 
       
        assert item_names == sorted(item_names), \
            f"Lọc A-Z SAI! Thứ tự thực tế: {item_names}"
        print("[PASS] TC04: Lọc sản phẩm A-Z thành công!")
        
        # 3. Thêm sản phẩm đầu tiên vào giỏ hàng
        add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        add_buttons[0].click()
        time.sleep(3) # Dừng 3s để thấy sản phẩm được thêm vào giỏ hàng
        print("[INFO] Đã thêm sản phẩm vào giỏ hàng!")
 
        # 4. Vào giỏ hàng
        print("[INFO] Chuẩn bị vào giỏ hàng...")
        time.sleep(3) # Dừng 3s để thấy nút giỏ hàng
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3) # Dừng 3s để thấy trang giỏ hàng
        print("[INFO] Đã vào giỏ hàng!")
 
        # 5. Nhấn Checkout
        print("[INFO] Chuẩn bị nhấn Checkout...")
        time.sleep(3) # Dừng 3s để thấy nút Checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(5) # Dừng 5s để thấy trang Checkout
        print("[INFO] Đã nhấn Checkout!")
 
        # 6. Cố tình để TRỐNG thông tin → web sẽ hiện lỗi thật
        driver.find_element(By.ID, "first-name").send_keys("")  # Để trống
        driver.find_element(By.ID, "last-name").send_keys("")   # Để trống
        driver.find_element(By.ID, "postal-code").send_keys("") # Để trống
        driver.find_element(By.ID, "continue").click()
        time.sleep(3)
        print("[INFO] Đã nhấn Continue với thông tin trống!")
 
        # 7. Kiểm tra web có hiện thông báo lỗi không
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_message.is_displayed(), "Không thấy thông báo lỗi trên web!"
 
        # Nếu có lỗi thật trên web → chụp màn hình
        print(f"[INFO] Web hiện lỗi: {error_message.text}")
        raise AssertionError(f"Web báo lỗi: {error_message.text}")
 
    
    except Exception as e:
        print(f"[FAIL] TC04 gặp lỗi: {e}")

        # Chụp màn hình khi fail - lưu vào evidence/screenshots/
        screenshot_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "evidence", "screenshots"
        )
        os.makedirs(screenshot_dir, exist_ok=True)
 
        timestamp = time.strftime("%Y%m%d%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"error_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"[SCREENSHOT] Đã lưu ảnh lỗi tại: {screenshot_path}")

    finally:
        driver.quit()
# Cho phép test độc lập file này
if __name__ == "__main__":
    run_test()