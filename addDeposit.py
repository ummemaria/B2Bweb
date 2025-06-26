from time import sleep

def add_deposit(page):
    try:
        close_add = page.locator("//button[@class='btn-close' and @aria-label='Close']")
        close_add.click()
        print("Close button clicked.")

    except Exception as e:
        print(f"An error occurred: {e}")


    burger_button = page.locator('//button[@class="navigationToggleBtn"]')
    burger_button.click()
    sleep(1)

    deposit_button = page.locator("//span[@class='tabTitle' and text()='Add Deposit Request']")
    deposit_button.click()
    sleep(1)

    # Select bank dropdown and choose 'Maria'
    bank_select = page.locator("//div[contains(@class, 'select__dropdown-indicator')]")
    bank_select.click()
    bank_done = page.locator("//div[@class='accounNumberBox' and text()='Maria']")
    bank_done.click()
    sleep(1)

    selected_bank = page.locator("//div[contains(@class, 'select__single-value')]")
    selected_bank_text = selected_bank.evaluate("el => el.textContent.trim()")
    assert selected_bank_text.startswith("Maria"), f"Expected bank 'Maria' but got '{selected_bank_text}'"
    sleep(2)

    submit_button = page.get_by_role('button', name="Submit")

    amount_field = page.locator("//input[@name='amount']")
    amount_field.fill('')  # clear amount
    submit_button.click()

    # Check validation error near amount input
    amount_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), \"Amount\")]")
    amount_error.wait_for(state='visible', timeout=3000)
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

    # Clear date field
    date_field = page.get_by_placeholder("Enter or Select Deposit Date")
    date_field.fill('')
    submit_button.click()

    # Check validation error near date input
    date_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'Select deposited date')]")
    date_error.wait_for(state='visible', timeout=3000)
    error_text = date_error.inner_text().strip().lower()
    assert "select deposited date" in error_text, f"Date validation message not found or mismatch: '{error_text}'"
    print("Date validation error correctly shown:", error_text)

    amount_field = page.locator("//input[@name='amount']")
    amount_field.fill('@@@')  
    submit_button.click()
    amount_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'The amount should be a number')]")
    amount_error.wait_for(state='visible', timeout=3000)
    error_text = amount_error.inner_text().strip().lower()
    expected_phrases = [
        "required",
        "invalid",
        "please enter",
        "can’t be blank",
        "can't be blank",
        "the amount should be a number (max two digits after dot)",
    ]
    assert any(phrase in error_text for phrase in expected_phrases), (
        f"Expected amount validation error but got: '{error_text}'"
    )
    print("Amount validation error correctly shown:", error_text)

    ref_field = page.locator('//input[@name="referenceNumber"]')
    ref_field.fill('!@#$%')
    submit_button.click()
    ref_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'Reference')]")
    ref_error.wait_for(state='visible', timeout=5000)
    error_text = ref_error.inner_text().strip().lower()
    expected_phrases = ["invalid", "special character", "not allowed", "please enter valid"]
    assert any(phrase in error_text for phrase in expected_phrases), \
        f"Expected special character validation error for reference but got: '{error_text}'"
    print("Reference special character validation error correctly shown:", error_text)

    deposit_slip = page.locator('//input[@name="referenceDocument" and @type="file"]')
    deposit_slip.set_input_files([])
    submit_button.click()

    file_error = page.locator("//span[contains(@class, 'errorMsgBox') and contains(text(), 'No file choosen')]")
    file_error.wait_for(state='visible', timeout=3000)
    error_text = file_error.inner_text().strip().lower()
    expected_phrases = ["required", "please upload", "no file choosen", "no file chosen"]
    assert any(phrase in error_text for phrase in expected_phrases), \
        f"Expected file upload validation error but got: '{error_text}'"
    print("File upload validation error correctly shown:", error_text)

    submit_button = page.get_by_role('button', name="Submit")
    submit_button.click()

    # Now fill valid data to pass validation and submit 
    amount_field.fill('402')
    amount_value = amount_field.input_value().strip()
    assert amount_value == '402', f"Expected amount to be '501' but got '{amount_value}'"

    date_field.fill('13/06/2025')
    date_value = date_field.input_value().strip()
    assert date_value == '13/06/2025', f"Expected date to be '12/06/2025' but got '{date_value}'"

    ref_field.fill('121')
    ref_value = ref_field.input_value().strip()
    assert ref_value == '121', f"Expected reference to be '1000' but got '{ref_value}'"

    file_path = r"C:\Users\ASUS\Pictures\download.jpg"
    deposit_slip.set_input_files(file_path)
    uploaded_files = deposit_slip.evaluate("element => element.files.length")
    assert uploaded_files == 1, "File upload failed: No file selected."

    submit_button.click()
    sleep(3)

    # Verify successful redirect
    expected_url = "https://bdf.centralindia.cloudapp.azure.com/bank-deposit"
    assert page.url == expected_url, f"Expected URL '{expected_url}' but got '{page.url}'"
    print("Form submitted successfully with valid data.")

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

    # Verify the reference number in the deposit list
    verify_reference_deposit_list(page, reference_number)

    # Return reference number for further use if needed
    return reference_number

def verify_reference_deposit_list(page, reference_number):
    page.goto("https://bdf.centralindia.cloudapp.azure.com/deposit-list")
    print("Navigated to deposit list page")

    # Wait for the list to appear
    table = page.locator("//table[contains(@class, 'bdfare-table')]") 
    table.wait_for(state="visible", timeout=10000)

    reference_locator = table.locator(f"xpath=.//td[text()='{reference_number}']")

    # Assert that the reference number exists in the list
    count = reference_locator.count()
    assert count > 0, f"❌ Reference number '{reference_number}' not found in the deposit list"
    print(f"✅ Reference number '{reference_number}' is present in the deposit list.")
