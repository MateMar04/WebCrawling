from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.youtube.com/")

ytd_rich_item_render = driver.find_elements_by_xpath('//ytd-rich-item-renderer[@class="style-scope ytd-rich-grid-renderer"]')

for item in ytd_rich_item_render:
    title = item.find_element_by_xpath('.//yt-formatted-string[@id="video-title"]').text
    print(title)





