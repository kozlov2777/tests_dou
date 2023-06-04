from selenium.webdriver.common.by import By


class MainPagesLocators:
    JOB_PAGES_LOCATOR = (By.XPATH, '/html/body/div[1]/header/ul/li[6]/a')
    SALARY_PAGES_LOCATOR = (By.XPATH, '/html/body/div[1]/header/ul/li[5]/a')
    FORUM_PAGES_LOCATOR = (By.XPATH, '/html/body/div[1]/header/ul/li[3]/a')


class JobPagesLocators:
    QA_ON_JOB_PAGE = (By.XPATH, '//*[@id="container"]/div[3]/div/div[2]/div[2]/div[1]/ul[1]/li[5]/a')
    CITY_FILTER_ON_JOB_PAGE = (By.CSS_SELECTOR, '#container > div.content-wrap > div > div.row.m-db > div.cell.m-db > div > div.row > div:nth-child(3) > div > div > ul:nth-child(5) > li:nth-child(1) > a')
    EXPERIENCE_FILTER_ON_JOB_PAGE = (By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div/ul[1]/li[2]/a[1]')
    CITY_IN_JOB_VACANCY = (By.CLASS_NAME, 'cities')


class SalaryPagesLocators:
    SLIDER_OF_EXPERIENCE = (By.CSS_SELECTOR, '#dws-fl-experience > div > svg > g > circle.handle.right')
    JOB_VACANCY_LIST = (By.XPATH, '//*[@id="dd-position"]/div[1]/div/div')
    JUNIOR_QA_IN_JOB_VACANCY_LIST = (By.XPATH, '//*[@id="dd-position"]/div[2]/div[2]/div[2]/div[2]')
    FILTER_AUTOMATION_QA = (By.XPATH, '//*[@id="dws-fl-specialization"]/div/div[2]/div[2]')
    FILTER_TECHNOLOGY_PYTHON = (By.CSS_SELECTOR, '#dws-fl-technology > div > div.tags-box > div:nth-child(7)')
    ENGLISH_LEVEL = (By.CSS_SELECTOR, '#dws-fl-english > div > svg > g > circle.handle.right')
    DATE_LIST = (By.XPATH, '//*[@id="dd-date"]/div[1]/div/div')
    DATE = (By.XPATH, '//*[@id="dd-date"]/div[2]/div[2]')
    SALARY = (By.XPATH, '//*[@id="median"]/div/span[2]')


class ForumsPagesLocators:
    BUTTON_ADD_TOPIC = (By.XPATH, '/html/body/div[1]/div[4]/ul/li[5]/div/a')
    TITLE_TOPIC = (By.XPATH, '//*[@id="txtTitle"]')
    IFRAME = (By.CLASS_NAME, 'tox-edit-area__iframe')
    TEXT_AREA = (By.XPATH, '//*[@id="tinymce"]')
    ADD = (By.XPATH, '//*[@id="btnSubmit"]')
    LOG_IN = (By.XPATH, '//*[@id="_loginDialog"]/div[1]/div[1]')

