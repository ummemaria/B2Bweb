from time import sleep
def log_in(page, context):

    # close_add= page.locator('//button[@aria-label="Close"]')
    # close_add.click()

    # expired = page.locator("//button[contains(@class, 'primaryBtn') and text()='Ok']")
    # expired.click()

    # print("expire token modal handling if present")
    # expired = page.locator("//button[contains(@class, 'primaryBtn') and text()='Ok']")
    # if expired.is_visible(timeout=3000):
    #     expired.click()



    email_field = page.get_by_placeholder("name@example.com")
    email_field.fill("ummemariarime@gmail.com")

    password_field = page.get_by_placeholder("Password")
    password_field.fill("Rime@1234")

    login_button = page.get_by_role('button', name="Login")
    login_button.click()
    sleep(2)

    context.storage_state(path = "playwright/.auth/storage_state.json")

    for i in range(6):
        manual_value = input(f"Enter the OTP digit for input field otp-{i}: ")
        otp_input = page.locator(f'//*[@id="otp-{i}"]')
        otp_input.fill(manual_value)

    go_verify = page.get_by_role('button', name="Verify")
    go_verify.click()

    close_add= page.locator('//button[@aria-label="Close"]')
    close_add.click()

    sleep(2)


