from selenium import webdriver

def load_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    html = driver.page_source
    print(html[:500])
    driver.quit()
    return html

if __name__ == "__main__":
    load_dynamic()
