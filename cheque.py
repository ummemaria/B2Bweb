from time import sleep
def cheque_deposit(page):
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

    cheque_add = page.get_by_role('link', name ="Cheque Deposit")
    cheque_add.click()

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

    date_select = page.locator("//div[@class='react-datepicker-wrapper']//input[contains(@class, 'form-control')]").nth(0)
    date_select.fill(' ')
    submit.click()
    date_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'Select deposited date')]")
    error_text = date_error.inner_text().strip().lower()
    assert "select deposited date" in error_text, f"Date validation message not found or mismatch: '{error_text}'"
    print("Date validation error correctly shown:", error_text)

    cheque_no = page.locator("//input[@name='chequeNumber']")
    cheque_no.fill('@@')
    submit.click()
    cheque_error = page.locator("//div[@class='form-group is-invalid']//span[@class='errorMsgBox' and text()='Please enter valid Cheque Number']")
    error_text = cheque_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "please enter valid cheque number",
        "please enter",
        "can’t be blank",
        "can't be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected cheque number validation error but got: '{error_text}'"
    )
    print("Cheque number validation error correctly shown:", error_text)

    cheque_issue = page.locator("//input[@name='issuedBank']")
    cheque_issue.fill('##') 
    submit.click() 
    cheque_issue_error = page.locator("//div[contains(@class, 'form-group is-invalid')]//input[@name='issuedBank']/following-sibling::span[contains(@class, 'errorMsgBox')]")
    error_text = cheque_issue_error.inner_text().strip().lower()
    print(f"Error text: '{error_text}'")
    expected_phrases = [
        "required",
        "please enter valid cheque issued bank",
        "please enter",
        "can’t be blank",
        "can't be blank",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected issued bank validation error but got: '{error_text}'"
    )
    print("Issued Bank validation error correctly shown:", error_text)

    cheque_date = page.locator("//div[@class='react-datepicker-wrapper']//input[contains(@class, 'form-control')]").nth(1)
    cheque_date.fill('')

    ref_field = page.locator("//input[@name='referenceNumber']")
    ref_field.fill('!@#$%')  
    ref_error = page.locator("//div[contains(@class, 'form-group is-invalid')]//input[@name='referenceNumber']/following-sibling::span[@class='errorMsgBox' and contains(text(),'Please enter valid Reference')]")
    error_text = ref_error.inner_text().strip().lower()
    expected_phrases = [
        "reference can’t be blank",  
        "required",
        "please enter valid reference",  
        "can’t be blank",
        "can't be blank"
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected reference number validation error but got: '{error_text}'"
    )
    print("Reference Number validation error correctly shown:", error_text)
    submit.click()
    sleep(3)

    amount_field = page.locator("//input[@name='amount']")
    amount_field.fill('10')
    amount_verify = amount_field.input_value().strip()
    assert amount_verify == '10', f"Expected amount to be '500' but got '{amount_verify}'"
    print("Amount field verified successfully:", amount_verify)

    date_select = page.locator("//div[@class='react-datepicker-wrapper']//input[contains(@class, 'form-control')]").nth(0)
    date_select.fill('24/06/2025')  
    date_verify = date_select.input_value().strip()
    assert date_verify == '24/06/2025', f"Expected date to be empty but got '{date_verify}'"
    print("Date field verified successfully:", date_verify)

    cheque_no = page.locator("//input[@name='chequeNumber']")
    cheque_no.fill('345')
    cheque_verify = cheque_no.input_value().strip()
    assert cheque_verify == '345', f"Expected cheque number to be '@@' but got '{cheque_verify}'"
    print("Cheque number field verified successfully:", cheque_verify)

    cheque_issue = page.locator("//input[@name='issuedBank']")
    cheque_issue.fill('SCB') 
    cheque_issue_verify = cheque_issue.input_value().strip()
    assert cheque_issue_verify == 'SCB', f"Expected cheque issue to be 'SCB' but got '{cheque_issue_verify}'"
    print("Cheque issue field verified successfully:", cheque_issue_verify)

    cheque_date = page.locator("//div[@class='react-datepicker-wrapper']//input[contains(@class, 'form-control')]").nth(1)
    cheque_date.fill('29/05/2025')  
    cheque_date_verify = cheque_date.input_value().strip()
    assert cheque_date_verify == '29/05/2025', f"Expected cheque date to be 28/05/2025 but got '{cheque_date_verify}'"
    print("Cheque date field verified successfully:", cheque_date_verify)

    ref_field = page.locator("//input[@name='referenceNumber']")
    ref_field.fill('11')  
    ref_field_verify = ref_field.input_value().strip()
    assert ref_field_verify == '11', f"Expected reference 11 but got '{ref_field_verify}'"
    print("Reference field verified successfully:" , ref_field_verify)

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

   
    reference_number = toast_text.split(':')[-1].strip()
    print(f"Captured reference number from toast: {reference_number}")

    expected_url = "https://bdf.centralindia.cloudapp.azure.com/cheque-deposit"
    assert page.url == expected_url, f"Expected URL '{expected_url}' but got '{page.url}'"
    print("Form submitted successfully with valid data.")



    sleep(3)

