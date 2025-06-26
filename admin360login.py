from time import sleep
import re

def admin_log(page, expected_data1):
    print("Go to the Admin360 page")

    email_field = page.locator("//input[@name='email' and @type='email' and @id='floatingInput']")
    email_field.fill("maria@bdfare.com")

    password_field = page.locator("//input[@name='password' and @type='password' and @id='floatingPassword']")
    password_field.fill("Rime@1234")

    login_button = page.get_by_role('button', name= "Login")
    login_button.click()
    print(f"Current URL after login: {page.url}")
    sleep(7)

    # expected URL to match the actual URL after login
    # expected_url = 'https://uatadmin.bdfare.com/FlightBookingList'
    # assert page.url == expected_url, f"Expected URL after login was not found. Found: {page.url}"
    # sleep(3)

    side_button = page.locator("//button[@type='button' and @class='navigationSlideBtn']")
    side_button.click()
    sleep(2)

    finance_menu = page.get_by_role('button', name= " Finance")
    finance_menu.click()
    sleep(2)

    deposit_manage = page.get_by_role('link', name="Deposit Management")
    deposit_manage.click()
    sleep(2)

    search = page.locator("//input[@class='searchInputBox form-control' and @placeholder='Reference']")
    search.click()
    search.press('Control+V')
    search.press('Enter')

    # modal_content = page.locator('//ul[@class="depositInfoList columnBlock"]')
    # assert modal_content == expected_data["Created by"], "Created by does not match"
    modal_content = page.locator('//ul[@class="depositInfoList columnBlock"]')
    modal_text = modal_content.inner_text()  

    print(f"Modal content: {modal_text}")  # 

    missing_fields = []
    for key, expected_value in expected_data1.items():

        match = re.search(rf"{re.escape(key)}\s*[:\-]?\s*(.*)", modal_text)
        if match:
            actual_value = match.group(1).strip()

            # Normalize the 'Amount' field by removing commas
            if key == "Amount":
                actual_value = actual_value.replace(",", "")
                expected_value = expected_value.replace(",", "")

            print(f"Actual '{key}': '{actual_value}' (Expected: '{expected_value}')")
            assert actual_value == expected_value, f"{key} value does not match"
            print(f"{key} value validated: {actual_value}")
        else:
            raise AssertionError(f"{key} not found in modal content!")

    proof_of_deposit = page.locator("//span[@class='labelBox' and contains(text(), 'Proof of deposit')]")
    assert proof_of_deposit.is_visible(), "Proof of deposit is not visible."
    print("Proof of deposit is visible.")

    # for reject case
    # rejected = page.get_by_role('button', name="Reject Deposit ")
    # rejected.click()
    # sleep(1)
    # rejection_field = page.get_by_placeholder("Write reason")
    # rejection_field.fill("Cheque has some issue")
    # assert rejection_field.input_value() == "Cheque has some issue", "The remark field is not filled correctly."

    #for hold case
    hold_button = page.get_by_role('button', name = " Hold")
    hold_button.click()
    sleep(1)
    hold_field = page.get_by_placeholder("Write reason")
    hold_field.fill("Please wait some moment")
    assert hold_field.input_value() == "Please wait some moment", "The remark field is not filled correctly."



    # approved = page.get_by_role('button', name= "Approve Deposit")
    # approved.click()
    # sleep(2)
    # remark_field = page.get_by_placeholder("Write reason")
    # remark_field.fill("Checkingggg")
    # assert remark_field.input_value() == "Checkingggg", "The remark field is not filled correctly."

    confirm_button = page.get_by_role('button', name=" Confirm")
    confirm_button.click()
    print("waitttttt")
    sleep(2)

    try:
        print("Navigating to the deposit list page...")                                                                              
        page.goto("https://uatadmin.bdfare.com/deposit-list")
        sleep(2)

        print(f"Current URL after navigation: {page.url}")

        expected_url = "https://uatadmin.bdfare.com/deposit-list"
        
        assert page.url == expected_url, f"Expected URL: {expected_url}, but found: {page.url}"
        print(f"Verified URL: {page.url} is correct.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    ref_num =  page.locator("//button[@class='primaryLink wordNoWrap']").nth(0).inner_text()
    print(f"Reference No: {ref_num}")
    # assert ref_num != "", "Reference No is empty!"


    highlight = page.locator("//button[@class='primaryLink wordNoWrap']").nth(0)

    element_handle = highlight.element_handle()

    page.evaluate("""
          (element) => {
        element.style.setProperty('border', '3px solid red', 'important');
        element.style.setProperty('background-color', 'yellow', 'important');
    }
    """, element_handle)
    print("Color ki hoiche????")
    sleep(5)

    page.evaluate(f"navigator.clipboard.writeText('{ref_num}')")
    print("Reference No copied to clipboard.")











