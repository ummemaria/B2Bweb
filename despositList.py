from time import sleep
from playwright.sync_api import TimeoutError

def deposit_list(page, expected_data):
    page.goto("https://bdf.centralindia.cloudapp.azure.com/deposit-list")
    print("Go to the deposit list")

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
            # value_xpath = f"//ul[contains(@class,'depositInfoList')]//li[span[contains(@class,'labelBox') and normalize-space(text())='{label_text}']]/span[contains(@class,'valueBox')]"
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

    close_info = modal.get_by_role('button', name="Close")
    close_info.click()
    print("Clicked 'Close' button.")

  
    reference_no = page.locator('td[data-th="Reference No"]').nth(0).inner_text()
    print(f"Reference No: {reference_no}")

    page.evaluate(f"navigator.clipboard.writeText('{reference_no}')")
    print("Reference No copied to clipboard.")

    try:
        close_info.wait_for(state="hidden", timeout=5000)
        print("Modal closed successfully.")
    except TimeoutError:
        errors.append("Close button (modal) did not disappear after clicking.")

    if errors:
        error_message = "\n".join(errors)
        raise AssertionError(f"Validation errors:\n{error_message}")

    sleep(2)


    try:
    
        balance = page.locator("//span[@class='myBalanceBtnData']/span[@class='amountBox']")
        current_balance_text = balance.text_content()

        if current_balance_text:
            current_balance = int(current_balance_text.strip().replace(",", "").split()[1])
            print(f"Current Balance: BDT {current_balance}")
        else:
            print("Balance element not found.")
            current_balance = None
    except Exception as e:
        print(f"Error extracting balance: {e}")
        current_balance = None

    return current_balance  
