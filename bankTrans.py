from time import sleep
# def submit_button(page):
#     submit = page.get_by_role('button', name="Submit")
def bank_transfer(page):
    try:
        close_add = page.locator("//button[@class='btn-close' and @aria-label='Close']")
        close_add.click()
        print("Close button clicked.")

    except Exception as e:
        print("Close button not visible")


    side_button = page.locator('//button[@class="navigationToggleBtn"]')
    side_button.click()
    sleep(1)

    deposit_button = page.locator("//span[@class='tabTitle' and text()='Add Deposit Request']")
    deposit_button.click()
    sleep(1)

    transfer = page.get_by_role('link', name= "Bank Transfer")
    transfer.click()

    submit = page.get_by_role('button', name="Submit")
    submit.click()

    deposit_in = page.locator("//div[@class='select__indicator select__dropdown-indicator css-1xc3v61-indicatorContainer']").first
    deposit_in.click()
    bank_done = page.locator("//div[@class='accounNumberBox' and text()='Maria']")
    bank_done.click()
    sleep(1)

    selected_bank = page.locator("//div[contains(@class, 'select__single-value')]")
    selected_bank_text = selected_bank.evaluate("el => el.textContent.trim()")
    assert selected_bank_text.startswith("Maria"), f"Expected bank 'Maria' but got '{selected_bank_text}'"
    sleep(2)
    submit.click()

    amount_field = page.locator("//input[@name='amount']")
    amount_field.fill('') 
    submit.click()
    amount_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), \"Amount\")]")
    error_text = amount_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected amount validation error but got: '{error_text}'"
    )
    print("Amount validation error correctly shown:", error_text)


    date_select = page.locator("//div[@class='react-datepicker-wrapper']//input[contains(@class, 'form-control')]")
    date_select.fill(' ')
    submit.click()

    date_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'Select deposited date')]")
    date_error.wait_for(state='visible', timeout=3000)
    error_text = date_error.inner_text().strip().lower()
    assert "select deposited date" in error_text, f"Date validation message not found or mismatch: '{error_text}'"
    print("Date validation error correctly shown:", error_text)

    ref_field = page.locator('//input[@name="referenceNumber"]')
    ref_field.fill('!@#$%')
    submit.click()
    ref_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'Reference')]")
    ref_error.wait_for(state='visible', timeout=5000)
    error_text = ref_error.inner_text().strip().lower()
    expected_phrases = ["invalid", "special character", "not allowed", "please enter valid"]
    assert any(phrase in error_text for phrase in expected_phrases), \
        f"Expected special character validation error for reference but got: '{error_text}'"
    print("Reference special character validation error correctly shown:", error_text)



    add_acc = page.get_by_role('button', name ="Add Account")
    add_acc.click()

    acc_submit = page.get_by_role('button', name ="Submit").nth(1)
    acc_submit.click()
   
    acc_type = page.locator("//div[@class='Select Account Type__indicator Select Account Type__dropdown-indicator css-1xc3v61-indicatorContainer']")
    acc_type.click()

    acc_submit = page.locator("//button[@type='submit']").nth(1)  
    acc_submit.click()

    acc_type = page.locator("//div[@class='Select Account Type__indicator Select Account Type__dropdown-indicator css-1xc3v61-indicatorContainer']")
    acc_type.click()
    acc_select = page.locator("//div[contains(text(), 'Savings')]")
    acc_select.click()

    acc_no = page.locator("//input[@type='text' and @name='accountNumber']")
    acc_no.fill('aaaaaa')

    acc_no_error = page.locator("//span[@class='errorMsgBox' and text()='Please enter valid Account Number']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "Please enter valid Account Number",
    ]

    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected account number validation error but got: '{error_text}'"
    )
    print("Account number validation error correctly shown:", error_text)

    acc_holder = page.locator("//input[@type='text' and @name='accountHolderName']")
    acc_holder.fill('12334')

    acc_holder_error = page.locator("//span[@class='errorMsgBox' and text()='Account Holder Number can’t be blank']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "Account Number can’t be blank",
    ]

    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected account holder number validation error but got: '{error_text}'"
    )
    print("Account holder number validation error correctly shown:", error_text)

    route_no = page.locator("//input[@type='text' and @name='ifsc']")
    route_no.fill('@@@@@')
    route_no_error = page.locator("//span[@class='errorMsgBox' and text()='Routing Number can’t be blank']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "Routing Number can’t be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected route number validation error but got: '{error_text}'"
    )
    print("route number validation error correctly shown:", error_text)


    branch_c = page.locator("//input[@type='text' and @name='branchCode']")
    branch_c.fill('wwww')
    branch_c_error = page.locator("//span[@class='errorMsgBox' and text()='Please enter valid Branch Code']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "Please enter valid Branch Code",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected branch code validation error but got: '{error_text}'"
    )
    print("branch code validation error correctly shown:", error_text)
    

    branch_name = page.locator("//input[@type='text' and @name='branchName']")
    branch_name.fill('1234')
    branch_name_error = page.locator("//span[@class='errorMsgBox' and text()='Branch Name can’t be blank']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "Branch Name can’t be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected branch name validation error but got: '{error_text}'"
    )
    print("branch name validation error correctly shown:", error_text)



    bank_name = page.locator("//input[@type='text' and @name='bankName']")
    bank_name.fill('9876')
    bank_name_error = page.locator("//span[@class='errorMsgBox' and text()='Bank Name can’t be blank']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "Bank Name can’t be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected bank name validation error but got: '{error_text}'"
    )
    print("bank name validation error correctly shown:", error_text)


    country = page.locator("//div[@class='country-option']//span[text()='Select Country']")
    country.click(force=True)
    country_name = page.locator("//span[text()='Bangladesh']")
    country_name.click()

    city = page.locator("//input[@type='text' and @name='city']")
    city.fill('2323')
    city_error = page.locator("//span[@class='errorMsgBox' and text()='City can’t be blank']")
    error_text = acc_no_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "City can’t be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected city validation error but got: '{error_text}'"
    )
    print("city validation error correctly shown:", error_text)
    acc_submit.click()

    acc_no.fill('567812341')
    acc_verify = acc_no.input_value().strip()
    assert acc_verify == '567812341', f"Expected amount to be '567812341' but got '{acc_verify}'"
    print("Account number verified successfully:", acc_verify)

    acc_holder = page.locator("//input[@type='text' and @name='accountHolderName']")
    acc_holder.fill('Juliaaa')
    acc_holder_verify = acc_holder.input_value().strip()
    assert acc_holder_verify == 'Juliaaa', f"Expected account holder name to be 'John Doe' but got '{acc_holder_verify}'"
    print("Account holder name verified successfully:", acc_holder_verify)

    route_no = page.locator("//input[@type='text' and @name='ifsc']")
    route_no.fill('123456')
    route_no_verify = route_no.input_value().strip()
    assert route_no_verify == '123456', f"Expected routing number to be '123456' but got '{route_no_verify}'"
    print("Routing number verified successfully:", route_no_verify)

    branch_c = page.locator("//input[@type='text' and @name='branchCode']")
    branch_c.fill('78910')
    branch_c_verify = branch_c.input_value().strip()
    assert branch_c_verify == '78910', f"Expected branch code to be '78910' but got '{branch_c_verify}'"
    print("Branch code verified successfully:", branch_c_verify)

    branch_name = page.locator("//input[@type='text' and @name='branchName']")
    branch_name.fill('Main Branch')
    branch_name_verify = branch_name.input_value().strip()
    assert branch_name_verify == 'Main Branch', f"Expected branch name to be 'Main Branch' but got '{branch_name_verify}'"
    print("Branch name verified successfully:", branch_name_verify)

    bank_name = page.locator("//input[@type='text' and @name='bankName']")
    bank_name.fill('ABC Bank')
    bank_name_verify = bank_name.input_value().strip()
    assert bank_name_verify == 'ABC Bank', f"Expected bank name to be 'ABC Bank' but got '{bank_name_verify}'"
    print("Bank name verified successfully:", bank_name_verify)

    city = page.locator("//input[@type='text' and @name='city']")
    city.fill('Dhaka')
    city_verify = city.input_value().strip()
    assert city_verify == 'Dhaka', f"Expected city to be 'Dhaka' but got '{city_verify}'"
    print("City verified successfully:", city_verify)
    acc_submit.click()
    sleep(2)

    amount_field = page.locator("//input[@name='amount']")
    amount_field.fill('25')  
    amount_verify = amount_field.input_value().strip() 
    assert amount_verify == '25', f"Expected amount to be '255' but got '{amount_verify}'"
    print("Amount field verified successfully:", amount_verify)

    date_select = page.locator("//div[@class='react-datepicker-wrapper']//input[contains(@class, 'form-control')]")
    date_select.fill('20/06/2025')  
    date_verify = date_select.input_value().strip() 
    assert date_verify == '20/06/2025', f"Expected date to be '20/06/2025' but got '{date_verify}'"
    print("Date field verified successfully:", date_verify)

    ref_field = page.locator('//input[@name="referenceNumber"]')
    ref_field.fill('10')  
    ref_verify = ref_field.input_value().strip()  
    assert ref_verify == '10', f"Expected reference number to be '11' but got '{ref_verify}'"
    print("Reference number field verified successfully:", ref_verify)

    deposit_form = page.locator("//div[@class='select__input-container css-19bb58m']").nth(1)
    deposit_form.click()
    deposit_done = page.locator("//div[@class='accountDetailsBox']/div[@class='accounNumberBox'][text()='Rime']")
    deposit_done.click()

    deposit_slip = page.locator("input[type='file'][name='referenceDocument']")
    deposit_slip.set_input_files(r"C:\Users\ASUS\Pictures\download.jpg")
    submit.click()

    toast_container = page.locator("//div[contains(@class, 'Toastify__toast-container')]").first
    toast_container.wait_for(state="visible", timeout=15000)

    toast_alert = toast_container.locator("//div[contains(@class, 'Toastify__toast--success')]//div[@role='alert']")
    toast_alert.wait_for(state="visible", timeout=5000)
    toast_text = toast_alert.inner_text().strip()

    print(f"Toast message text: {toast_text}")
    assert "Deposit requested" in toast_text, "Toast does not contain 'Deposit requested'"

    # Extract reference number from the toast message
    reference_number = toast_text.split(':')[-1].strip()
    print(f"Captured reference number from toast: {reference_number}")

    expected_url = "https://bdf.centralindia.cloudapp.azure.com/bank-transfer"
    assert page.url == expected_url, f"Expected URL '{expected_url}' but got '{page.url}'"
    print("Form submitted successfully with valid data.")





































    
