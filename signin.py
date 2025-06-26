from time import sleep
from cred import email, password
def after_signin(page):

    close_add= page.locator('//button[@aria-label="Close"]')
    close_add.click()

    print("Maaaffffffff chaiiiiiii")

    burger_button = page.locator('//button[@class="navigationToggleBtn"]')
    burger_button.click()

    
