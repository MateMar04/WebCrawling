from time import sleep
from selenium import webdriver


def load_items(result):
    promotion_items = driver.find_elements_by_xpath('//li[@class="promotion-item"]')
    for promotion_item in promotion_items:
        price = promotion_item.find_element_by_xpath('.//span[@class="promotion-item__price"]/span').text
        title = promotion_item.find_element_by_xpath('.//p[@class="promotion-item__title"]').text
        result.append((title, price))


driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.mercadolibre.com.ar/ofertas#nav-header")
result = []
for i in range(3):
    load_items(result)
    sig = driver.find_element_by_xpath('//li[@class="andes-pagination__button andes-pagination__button--next"]/a').get_attribute('href')
    sleep(10)
    driver.get(sig)

print(len(result),  result)
