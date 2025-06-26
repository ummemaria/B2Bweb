from time import sleep
def home_page(page):
    close_add= page.locator('//button[@aria-label="Close"]')
    close_add.click()

    print("Maaaffffffff chaiiiiiii")


    # holiday = page.locator('//li[.//span[text()="Holidays"]]')
    # holiday.click()
    
    # visa = page.locator('//li[.//span[text()="Visa"]]')
    # visa.click()
    # xclusive = page.locator('//li[.//span[text()="Xclusive Fares"]]')
    # xclusive.click()
    # umrrah = page.locator('//li[.//span[text()="Umrah"]]')
    # umrrah.click()
    destination = page.locator("//button[@class='flightSearchDopdownBtn showDropDownBtn']").nth(0)  # Click the second button
    destination.click()

    destination = page.locator("//button[@class='flightSearchDopdownBtn showDropDownBtn']").nth(1)  # Click the second button
    destination.click()

    city = page.get_by_placeholder("Enter airport code or city")
    city.fill("Cxb")
    # city.press("Enter") 
    city_select = page.locator('//a[@aria-label="CXB"]')
    city_select.click()
    sleep(2)
    print("woooowwwwwwwwwwwwwwwwwww")

    departure = page.locator('//button[@type="button" and contains(@class, "showDropDownBtn") and contains(@class, "dateSelectDopdownBtn")]').nth(0)
    departure.click()
    start_date = page.locator("//div[contains(@class, 'rmdp-week')]//span[text()='16' and contains(@class, 'sd')]")
    start_date.click()
    sleep(1)


    return_time = page.locator('//button[@type="button" and contains(@class, "showDropDownBtn") and contains(@class, "dateSelectDopdownBtn")]').nth(1)
    return_time.click()
    return_date = page.locator("//div[contains(@class, 'rmdp-week')]//span[text()='25' and contains(@class, 'sd')]").nth(1)
    return_date.click()

    traveller_class = page.locator("//button[@class='showDropDownBtn travellerClassDropdownBtn']")
    traveller_class.click()

    search_button = page.locator("//button[@class='bdfareBtn largeBtn primaryBtn searchBtn']")

    sleep(1)



    # select_city = page.locator('//a[.//div[contains(text(), "Coxs Bazar, Bangladesh")]]')
    # select_city.click()
    

