def old_balance(page):
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