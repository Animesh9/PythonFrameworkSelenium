import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.yatra.com/")
    request.cls.driver = driver
    print(driver.title)
    driver.maximize_window()
    yield
    driver.quit()
