from selenium import webdriver


def href(node):
    return node.get_attribute('href')


driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.instagram.com/leomessi/")


try:
    posts = list(map(href, driver.find_elements_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]/a')))

    for i in posts:
        driver.get(i)
        likes = driver.find_element_by_xpath('.//button[@class="sqdOP yWX7d     _8A5w5    "]/span').text
        print(likes)

except:
    pass

