from time import sleep
from cred import email, password
def login_final(page, context):
    email_field = page.locator('//*[@name="email"]')
    email_field.fill(email)

    password_field = page.locator('//*[@id="floatingPassword"]')
    password_field.fill(password)

    # login_button = page.get_by_role('button', name="Login")
    # login_button.click()

    page.locator('//button[contains(@class, "bdfareBtn") and contains(@class, "loginBtn") and contains(@class, "primaryBtn") and contains(@class, "largeBtn") and contains(@class, "columnBlock")]').click()
    # sleep(2)

    # change_number = page.get_by_role('button', name= "Change Number")
    # change_number.click()l

    # code = page.get_by_role('button', name = "Send Code")
    # code.click()
    # sleep(3)

    for i in range(6):
        manual_value = input(f"Enter the OTP digit for input field otp-{i}: ")
        otp_input = page.locator(f'//*[@id="otp-{i}"]')  # XPath used here
        otp_input.fill(manual_value)

    go_verify = page.get_by_role('button', name="Verify")
    go_verify.click()
    sleep(1)

    code = page.get_by_role('button', name = "Send Code")
    code.click()
    sleep(2)

    for i in range(6):
        manual_value = input(f"Enter the OTP digit for input field otp-{i}: ")
        otp_input = page.locator(f'//*[@id="otp-{i}"]')  # XPath used here
        otp_input.fill(manual_value)

        varify_confirm = page.get_by_role('button', name ="Verify")
        varify_confirm.click()




    context.storage_state(path = "playwright/.auth/storage_state.json")

    sleep(2)
