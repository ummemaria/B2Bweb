import pytest
from playwright.sync_api import sync_playwright

# from registerProprietor import add_agency
# from registerPartner import add_partner
# from registerCompany import add_company
from login import log_in

# from passwordset import password_reset
from signin import after_signin
from loginFinal import login_final
from homePage import home_page
from sidebar import menu_bar
from addDeposit import add_deposit
from despositList import deposit_list
from admin360login import admin_log
from payment import payment_ledger
from bankTrans import bank_transfer
from payreject import payment_reject
from cheque import cheque_deposit
from payhold import payment_hold
from time import sleep

import allure



# Test function with Allure annotations
@allure.feature("User Registration")
@allure.story("User registers on the site")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_run():
    base_url1 = "https://bdf.centralindia.cloudapp.azure.com/"
    base_url2 = "https://uatadmin.bdfare.com/"
    expected_data = {
        # "Reference No": "DEP25061310",
        "Created by": "Umme Rime",
        # "Created on": "04 Jun 2025, 13:56",
        # "Payment type": "Bank Deposit",
        # "Payment type": "Bank Transfer",
        # "Payment type" :"Cheque",
        # "Amount": "BDT 1",
        # "Deposited To Bank": "Brac Bank Ltd",
        # "Deposited From": "AC No - 012012012012",
        "Cheque Issued Bank" :"SCB",
        # "Deposited To": "AC No - 111222111222",
        "Deposited From": "AC No - 111222111222",
        # "Cheque Issued Date" :"29 May 2025"
        # "Proof of deposit": True,
        # "Status": "Requested",
    }


    expected_data1 = {
        # "Reference No": "DEP25061310",
        "Created by": "Umme Rime",
        # "Created on": "04 Jun 2025, 13:56",
        # "Payment type": "Bank Deposit",
        # "Amount": "BDT 400",
        # "Payment type": "Bank Transfer",
        # "Payment type" :"Cheque",
        # "Deposited To Bank": "Brac Bank Ltd",
         "Cheque Issued Bank" :"SCB",
        # "Deposited To AC No:": "111222111222",
        "Deposited In" : "AC No - 111222111222",
        # "Proof of deposit": True,
        "Status": "Requested",
    }

    row_index = 5 

    with sync_playwright() as playwright:  # Make sure this line is correctly indented
        browser = playwright.chromium.launch(
            headless=False, args=["--start-maximized"], slow_mo=500
        )

        context = browser.new_context(
            no_viewport=True,
            storage_state="playwright/.auth/storage_state.json",
            ignore_https_errors=True,
        )
        context.set_extra_http_headers({"Cache-Control": "max-age=31536000"})
        page = context.new_page()

        page.goto(base_url1)  # Navigate to the first URL

        try:
            # Here will add Modules or features

            # add_agency(page)
            # add_partner(page)
            # add_company(page)

            # if page.get_by_role("button", name="Login").is_visible(timeout=5000):
            #     print("Session expired or not logged in, running login flow...")
            #     log_in(page, context)
            #     context.storage_state(path="playwright/.auth/storage_state.json")
            #     page.goto(base_url1)
            # else:
            #     print("Session is valid, proceeding with test...")



            # password_reset(page)
            # login_final(page, context)
            # after_signin(page)
            # home_page(page)
            # menu_bar(page)
            # add_deposit(page)
            # sleep(1)
            # deposit_list(page, expected_data)
            # current_balance = deposit_list(page, expected_data)
            # sleep(2)

            # page.goto(base_url2) 
            # admin_log(page, expected_data1)  

            # page.goto(base_url1)

            # payment_ledger(page, current_balance)

            # @allure.step("Navigating to the registration page and adding a deposit")
            # def add_and_validate_deposit():
            #     page.goto(base_url1)  # Navigate to the first URL
            #     add_deposit(page)  # Add deposit
            #     sleep(1)  # Wait for the deposit to be added
            #     current_balance = deposit_list(page, expected_data)  # Validate deposit and get balance
            #     return current_balance
            
            # current_balance = add_and_validate_deposit()



            # @allure.step("Navigating to the registration page and adding a Bank Transfer")
            # def add_and_validate_bank_transfer():
            #     page.goto(base_url1)
            #     bank_transfer(page)
            #     sleep(1)
            #     current_balance = deposit_list(page, expected_data)  
            #     return current_balance
            
            # current_balance = add_and_validate_bank_transfer()

            @allure.step("Navigating to the bdfare page and adding a cheque deposit")
            def add_and_validate_cheque_deposit():
                page.goto(base_url1, timeout=60000)
                sleep(2)
                cheque_deposit(page)
                sleep(1)
                current_balance = deposit_list(page, expected_data)  
                return current_balance
            current_balance = add_and_validate_cheque_deposit()


            @allure.step("Admin approving the deposit")
            def admin_approval():
                page.goto(base_url2)  # Go to the admin page
                admin_log(page, expected_data1)  # Approve the deposit
                sleep(2)
            admin_approval()

            # @allure.step("Navigating back to the registration page and validating payment ledger")
            # def validate_payment_ledger():
            #     page.goto(base_url1)  # Go back to the deposit list page
            #     payment_ledger(page, current_balance)  # Validate payment ledger data
            # validate_payment_ledger()

            @allure.step("Navigation back to the BdFare website and validating manage deposit")
            def validate_payment_reject():
                page.goto(base_url1)
                payment_reject(page, current_balance, expected_data)
            validate_payment_reject()

            # @allure.step("Navigation back to the BdFare website and validating manage deposit")
            # def validate_payment_hold():
            #     page.goto(base_url1)
            #     payment_hold(page, current_balance, expected_data)
            # validate_payment_hold()

            # success_message = page.locator("text=Registration Successful")  # Example: update with the actual message or element
            # assert success_message.is_visible(), "Registration success message is not visible"

        except Exception as e:
            screenshot_path = "screenshot_failure.png"
            try:
                if not page.is_closed():
                    page.screenshot(path=screenshot_path)
                    with open(screenshot_path, "rb") as f:
                        allure.attach(
                            f.read(),
                            name="Failure Screenshot",
                            attachment_type=allure.attachment_type.PNG,
                        )
            except Exception as screenshot_error:
                print(f"Failed to take screenshot: {screenshot_error}")

            allure.attach(
                str(e),
                name="Error Details",
                attachment_type=allure.attachment_type.TEXT,
            )
            print(f"An error occurred during registration: {e}")
            raise
        finally:
            browser.close()
