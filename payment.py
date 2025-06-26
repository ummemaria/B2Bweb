from time import sleep
def payment_ledger(page, current_balance):
    print("Go to the payment page")

    # try:
    #     close_add = page.locator("//button[@class='btn-close' and @aria-label='Close']")
    #     close_add.click()
    #     print("Close button clicked.")

    # except Exception as e:
    #     print(f"An error occurred: {e}")

    burger_button = page.locator('//button[@class="navigationToggleBtn"]')
    burger_button.click()

    try:
        burger_button.wait_for(state="hidden", timeout=5000)
        print("Burger button disappeared after click.")
    except TimeoutError:
        raise AssertionError("Burger button did not disappear after clicking.")


    payment_field = page.get_by_role('link', name="Payment Ledger")
    payment_field.click()

    try:
        page.wait_for_url("https://bdf.centralindia.cloudapp.azure.com/my-transactions", timeout=10000)
        print("Navigation to Payment Ledger page confirmed.")
    except TimeoutError:
        raise AssertionError("Navigation to Payment Ledger page did not happen after clicking the link.")


    ref_check = page.locator("//input[@class='searchInputBox']")
    ref_check.click()
    ref_check.press('Control+V')
    ref_check.press('Enter')
    search_btn = page.locator("//div[@class='formInlineGroup referenceNoSearchCol']//button[@class='searchBtn']")
    search_btn.click()
    sleep(2)

    highlight = page.locator("//td[@data-th='Order Reference']").nth(0)
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
    new_balance_text = balance_after_deposit.text_content()
    new_balance = int(new_balance_text.strip().split()[1])  # Extract numeric part

    # Print the new balance after the deposit
    print(f"New Balance after deposit: BDT {new_balance}")

    # Step 4: Compare the balance before and after the deposit
    deposit_amount = 400
    expected_new_balance = current_balance + deposit_amount

    # Verify if the new balance matches the expected balance
    assert new_balance == expected_new_balance, f"Balance verification failed! Expected BDT {expected_new_balance}, but got BDT {new_balance}"

    # If the assertion passes, it means the deposit was successful and the balance updated correctly
    print("Deposit successful. Balance updated correctly.")



     
    