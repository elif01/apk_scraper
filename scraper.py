from selenium import webdriver

with webdriver.Chrome() as driver:
  
  base_url = "https://apkpure.com/app"

  driver.get(base_url)

  # driver returns web elements
  apps = driver.find_elements_by_class_name("category-template-down")
  download_links = []

  for web_elt in apps:
    anchor = web_elt.find_element_by_tag_name('a')
    l = anchor.get_attribute("href")
    download_links.append(l)
  
  # click on each payload
  for l in download_links:
    driver.get(l)


