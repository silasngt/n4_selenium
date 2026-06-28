import sys
import os
import csv
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.driver_factory import get_driver
from selenium.webdriver.common.by import By


def run_test():

    print("=" * 65)
    print("        Data-Driven Testing - Login Test")
    print("=" * 65)

    csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "users.csv"
    )

    with open(csv_path, newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file, delimiter=';')

        print(f"{'Username':<25}{'Expected':<12}{'Actual':<12}{'Result'}")
        print("-" * 65)

        total = 0
        passed = 0

        for row in reader:

            username = row["username"]
            password = row["password"]
            expected = row["expected"]

            driver = get_driver()

            try:

                driver.get("https://www.saucedemo.com/")
                time.sleep(1)

                driver.find_element(By.ID, "user-name").send_keys(username)
                driver.find_element(By.ID, "password").send_keys(password)
                driver.find_element(By.ID, "login-button").click()

                time.sleep(2)

                login_success = "inventory.html" in driver.current_url

                actual = "PASS" if login_success else "FAIL"

                result = "PASS" if actual == expected else "FAIL"

                print(f"{username:<25}{expected:<12}{actual:<12}{result}")

                total += 1
                if result == "PASS":
                    passed += 1

            except Exception as e:

                print(f"{username:<25}{expected:<12}{'ERROR':<12}FAIL")
                print(f"Error: {e}")

            finally:

                driver.quit()

        print("-" * 65)
        print(f"Total Test Cases : {total}")
        print(f"Passed           : {passed}")
        print(f"Failed           : {total - passed}")
        print("=" * 65)


if __name__ == "__main__":
    run_test()