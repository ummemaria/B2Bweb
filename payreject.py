from time import sleep
def payment_reject(page, current_balance, expected_data):
    print("Go to the manage deposit request page ")

    # try:
    #     close_add = page.locator("//button[@class='btn-close' and @aria-label='Close']")
    #     close_add.click()
    #     print("Close button clicked.")

    # except Exception as e:
    #     print(f"An error occurred: {e}")

    burger_button = page.locator('//button[@class="navigationToggleBtn"]')
    burger_button.click()

    try:
        print("Burger button disappeared after click.")
    except TimeoutError:
        raise AssertionError("Burger button did not disappear after clicking.")
    sleep(1)

    manage_deposit = page.get_by_role('link', name = "Manage Deposit Request")
    manage_deposit.click()
    sleep(1)

    try:
        page.wait_for_url("https://bdf.centralindia.cloudapp.azure.com/deposit-list", timeout=10000)
        print("Navigation to Manage Deposit Request page confirmed.")
    except TimeoutError:
        raise AssertionError("Navigation to Payment Ledger page did not happen after clicking the link.")


    ref_check = page.locator("//input[@class='searchInputBox']")
    ref_check.click()
    ref_check.press('Control+V')
    ref_check.press('Enter')
    search_btn = page.locator("//div[@class='formInlineGroup referenceNoSearchCol']//button[@class='searchBtn']")
    search_btn.click()
    sleep(2)

    highlight = page.locator("//td[@data-th='Reference No']").nth(0)
    element_handle = highlight.element_handle()

    page.evaluate("""
        element => {
            element.style.border = '3px solid red';
            element.style.backgroundColor = 'yellow';
        }
    """, element_handle)
    sleep(4)

    search_value = page.locator("//div[@class='tableDataWrap transactionsTabs bdfareMobileTableWrap']//table[@class='table bdfare-table']")
    table_content = search_value.inner_text()  
    print(table_content)

    balance_after_deposit = page.locator("//span[@class='myBalanceBtnData']/span[@class='amountBox']")
    try:
        new_balance_text = balance_after_deposit.text_content()
        new_balance = int(new_balance_text.strip().split()[1])
        print(f"New Balance after deposit: BDT {new_balance}")
    except Exception as e:
        print(f"Failed to parse the balance: {e}")
        new_balance = current_balance 

    deposit_amount = 25
    expected_new_balance = current_balance + deposit_amount
    if new_balance != expected_new_balance:
        error_message = f"Balance verification failed! Expected BDT {expected_new_balance}, but got BDT {new_balance}"
        print(error_message) 
    else:
        print("Deposit successful. Balance updated correctly.")


    view = page.locator("//td[@class='actionCol']/button[text()='View']").nth(0)
    view.click()
    
    modal = page.locator("//div[contains(@class, 'modal') and contains(@class, 'show') and contains(@class, 'depositInfoModal')]")
    modal.wait_for(state="visible", timeout=5000)

    errors = []  

    for label, expected_value in expected_data.items():
        if label == "Proof of deposit":
            img_xpath = "//ul[contains(@class,'depositInfoList')]//li[span[contains(@class,'labelBox') and contains(text(),'Proof of deposit')]]//img"
            img_locator = modal.locator(img_xpath)
            try:
                img_locator.wait_for(state='visible', timeout=5000)
                if not img_locator.is_visible():
                    errors.append("Proof of deposit image missing!")
                else:
                    print("Proof of deposit image is visible.")
            except Exception:
                errors.append("Proof of deposit image missing!")
        else:
            label_text = f"{label} :"
            value_xpath = f"//ul[contains(@class,'depositInfoList')]//li[span[contains(@class,'labelBox') and normalize-space(text())='{label_text}']]/span[contains(@class,'valueBox')]"
            
            value_locator = modal.locator(value_xpath)
            try:
                actual_value = value_locator.inner_text().strip()
                print(f"Actual '{label}': '{actual_value}' (Expected: '{expected_value}')")
                if expected_value not in actual_value:
                    errors.append(f"{label} value mismatch: expected '{expected_value}', got '{actual_value}'")
                else:
                    print(f"{label} value validated: {expected_value}")
            except Exception as e:
                errors.append(f"Failed to get {label} value: {e}")
    print("\nModal Data:")
    modal_content = modal.inner_text()  
    formatted_modal_data = "\n".join(modal_content.split())
    print(formatted_modal_data)

    close_info = modal.get_by_role('button', name="Close")
    close_info.click()
    print("Clicked 'Close' button.")


    