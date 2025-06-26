def password_reset(page):

    password = page.get_by_placeholder("Password").nth(1)
    password.fill("Rime@1234")

    confirm_pass = page.locator('//*[@id="floatingConfirmPassword"]')
    confirm_pass.fill("Rime@1234")

    pass_button = page.get_by_role('button',name = "Change password")
    pass_button.click()