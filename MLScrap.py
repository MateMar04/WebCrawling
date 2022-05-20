from selenium import webdriver


driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.mercadolibre.com.ar/ofertas#nav-header")

promotion_items = driver.find_elements_by_xpath('//li[@class="promotion-item"]')

for promotion_item in promotion_items:
    price = promotion_item.find_element_by_xpath('.//span[@class="promotion-item__price"]').text
    title = promotion_item.find_element_by_xpath('.//p[@class="promotion-item__title"]').text
    print(title, price)


