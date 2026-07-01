import sys
import os
import time
from datetime import datetime

# Thêm đường dẫn thư mục gốc của dự án vào sys.path để có thể import các module từ các file khác
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


# Import các hàm run_test từ từng Test Case
from test.tc02_data_driven_huy import run_test as run_tc02
from test.tc03_cart_logic_hy import run_test as run_tc03
from test.tc04_screenshot_fail_khoi import run_test as run_tc04
from test.tc05_end_to_end_menh import run_test as run_tc05

def generate_report():
    print("\n=========================================")
    print("BẮT ĐẦU CHẠY CHUỖI KIỂM THỬ TỰ ĐỘNG")
    print("=========================================\n")
    
    # Ghi nhận thời gian bắt đầu
    start_time = datetime.now()

    # Chạy lần lượt các Test Case
    print(">>> Đang chạy TC02 (Nguyễn Quang Huy)...")
    run_tc02()
    time.sleep(1) 

    print("\n>>> Đang chạy TC03 (Nguyễn Tâm Hy)...")
    run_tc03()
    time.sleep(1)

    print("\n>>> Đang chạy TC04 (Nguyễn Đăng Khôi)...")
    run_tc04()
    time.sleep(1)

    print("\n>>> Đang chạy TC05 (Đinh Thiên Mệnh)...")
    run_tc05()
    
    # Ghi nhận thời gian kết thúc
    end_time = datetime.now()
    duration = end_time - start_time

    # XUẤT FILE BÁO CÁO 
    report_content = f"""
    =========================================
    BÁO CÁO KẾT QUẢ KIỂM THỬ TỰ ĐỘNG SELENIUM
    =========================================
    - Thời gian chạy: {start_time.strftime("%d/%m/%Y %H:%M:%S")}
    - Tổng thời gian thực thi: {duration.total_seconds():.2f} giây
    - Các Test Case đã thực thi:
      1. TC02 - Data-Driven Testing (Nguyễn Quang Huy)
      2. TC03 - Cart Logic (Nguyễn Tâm Hy)
      3. TC04 - Screenshot on Fail (Nguyễn Đăng Khôi)
      4. TC05 - End-to-End Wait (Đinh Thiên Mệnh)
      5. Chạy toàn bộ TC và Xuất báo cáo (Nguyễn Giang Thành Tài)
    
    * Vui lòng kiểm tra màn hình Console để xem chi tiết Pass/Fail của từng TC.
    * Các ảnh chụp Bug được lưu tự động tại: evidence/screenshots/
    =========================================
    """
    
    # Tạo và ghi vào file test_report.txt
    with open("test_report.txt", "w", encoding="utf-8") as file:
        file.write(report_content)
        
    print("\n=========================================")
    print("HOÀN THÀNH! Đã xuất báo cáo ra file 'test_report.txt'")
    print("=========================================")

    # XUẤT FILE BÁO CÁO DƯỚI DẠNG HTML
    # html_content = f"""
    # <!DOCTYPE html>
    # <html lang="vi">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Báo Cáo Kiểm Thử Tự Động</title>
    #     <style>
    #         body {{
    #             font-family: Arial, sans-serif;
    #             background-color: #f4f7f6;
    #             color: #333;
    #             margin: 0;
    #             padding: 20px;
    #         }}
    #         .container {{
    #             max-width: 800px;
    #             margin: auto;
    #             background: #fff;
    #             padding: 30px;
    #             border-radius: 8px;
    #             box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    #         }}
    #         h1 {{
    #             text-align: center;
    #             color: #2c3e50;
    #             border-bottom: 2px solid #3498db;
    #             padding-bottom: 10px;
    #         }}
    #         .summary {{
    #             background-color: #e8f4f8;
    #             padding: 15px;
    #             border-left: 5px solid #3498db;
    #             margin-bottom: 20px;
    #             border-radius: 4px;
    #         }}
    #         .summary p {{
    #             margin: 5px 0;
    #             font-size: 16px;
    #         }}
    #         table {{
    #             width: 100%;
    #             border-collapse: collapse;
    #             margin-top: 20px;
    #         }}
    #         th, td {{
    #             padding: 12px;
    #             text-align: left;
    #             border-bottom: 1px solid #ddd;
    #         }}
    #         th {{
    #             background-color: #3498db;
    #             color: white;
    #         }}
    #         tr:hover {{
    #             background-color: #f1f1f1;
    #         }}
    #         .status-done {{
    #             color: #27ae60;
    #             font-weight: bold;
    #         }}
    #         .footer {{
    #             text-align: center;
    #             margin-top: 30px;
    #             font-size: 12px;
    #             color: #7f8c8d;
    #         }}
    #     </style>
    # </head>
    # <body>
    #     <div class="container">
    #         <h1>Báo Cáo Kết Quả Kiểm Thử Tự Động (Selenium)</h1>
            
    #         <div class="summary">
    #             <p><strong>Ngày giờ thực thi:</strong> {start_time.strftime("%d/%m/%Y %H:%M:%S")}</p>
    #             <p><strong>Tổng thời gian chạy:</strong> {duration.total_seconds():.2f} giây</p>
    #             <p><strong>Môi trường:</strong> Google Chrome WebDriver</p>
    #         </div>

    #         <table>
    #             <thead>
    #                 <tr>
    #                     <th>#</th>
    #                     <th>Tên Test Case</th>
    #                     <th>Phụ trách</th>
    #                     <th>Trạng thái thực thi</th>
    #                 </tr>
    #             </thead>
    #             <tbody>
    #                 <tr>
    #                     <td>1</td>
    #                     <td>TC02 - Data-Driven Testing (Đọc file CSV)</td>
    #                     <td>Nguyễn Quang Huy</td>
    #                     <td class="status-done">Hoàn thành luồng</td>
    #                 </tr>
    #                 <tr>
    #                     <td>2</td>
    #                     <td>TC03 - Cart Logic (Tính toán giá tiền)</td>
    #                     <td>Nguyễn Tâm Hy</td>
    #                     <td class="status-done">Hoàn thành luồng</td>
    #                 </tr>
    #                 <tr>
    #                     <td>3</td>
    #                     <td>TC04 - Screenshot on Fail (Chụp màn hình lỗi)</td>
    #                     <td>Nguyễn Đăng Khôi</td>
    #                     <td class="status-done">Đã bắt Bug & Lưu ảnh</td>
    #                 </tr>
    #                 <tr>
    #                     <td>4</td>
    #                     <td>TC05 - End-to-End Wait (Luồng mua hàng)</td>
    #                     <td>Đinh Thiên Mệnh</td>
    #                     <td class="status-done">Hoàn thành luồng</td>
    #                 </tr>
    #                 <tr>
    #                     <td>5</td>
    #                     <td>Chạy toàn bộ TC và Xuất báo cáo</td>
    #                     <td>Nguyễn Giang Thành Tài</td>
    #                     <td class="status-done">Hoàn thành luồng</td>
    #                 </tr>
    #             </tbody>
    #         </table>

    #         <div class="footer">
    #             <p>Báo cáo được tạo tự động bởi Python & Selenium WebDriver.</p>
    #             <p><em>* Vui lòng kiểm tra thư mục evidence/screenshots/ để xem chi tiết hình ảnh lỗi (nếu có).</em></p>
    #         </div>
    #     </div>
    # </body>
    # </html>
    # """
    
    # # Ghi nội dung vào file test_report.html
    # with open("test_report.html", "w", encoding="utf-8") as file:
    #     file.write(html_content)
        
    # print("\n=========================================")
    # print("HOÀN THÀNH! Đã xuất báo cáo ra file 'test_report.html'")
    # print("=========================================")

if __name__ == "__main__":
    generate_report()