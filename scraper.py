from selenium import webdriver

with webdriver.Chrome() as driver:
  base_url = "https://apkpure.com/app"

  driver.get("https://apkpure.com/app")
  # apps are web elements
  apps = driver.find_elements_by_class_name("category-template-down")
  download_links = []

  for web_elt in apps:
    anchr = web_elt.find_element_by_tag_name('a')
    dl_link = anchr.get_attribute("href")
    download_links.append(dl_link)
  
  
  for applink in download_links:
    driver.get(applink)


