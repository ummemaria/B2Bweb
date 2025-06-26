def menu_bar(page):

    burger_button = page.locator('//button[@class="navigationToggleBtn"]')
    burger_button.click()

    my_bookings = page.locator("//span[text()='My Bookings']")
    my_bookings.click()

    manage_traveller = page.locator("//span[text()='Manage Traveller']")
    manage_traveller.click()

    payment_ledger = page.locator("//span[text()='Payment Ledger']")
    payment_ledger.click()