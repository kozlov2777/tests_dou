from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://dou.ua'

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")

    def find_element_for_clickable(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                     message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                     message=f"Can't find elements by locator {locator}")

    def go_to_web_site(self):
        return self.driver.get(self.base_url)

    def execute_script(self, script):
        return self.driver.execute_script(script)


class ForumPage(BasePage):
    def click_on_add_topic(self):
        self.find_element(ForumsPagesLocators.BUTTON_ADD_TOPIC).click()

    def set_title_of_topic(self, title):
        self.find_element(ForumsPagesLocators.TITLE_TOPIC).send_keys(title)

    def switch_to_iframe(self):
        iframe = self.find_element(ForumsPagesLocators.IFRAME)
        self.driver.switch_to.frame(iframe)

    def set_description(self, description):
        self.find_element(ForumsPagesLocators.TEXT_AREA).send_keys(description)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def create_topic(self):
        self.find_element(ForumsPagesLocators.ADD).click()

    def appear_window_for_log_in(self):
        log_in = self.find_element(ForumsPagesLocators.LOG_IN).text
        return log_in


class JobPage(BasePage):
    def click_on_QA(self):
        self.find_element(locator=JobPagesLocators.QA_ON_JOB_PAGE, time=20).click()

    def click_on_filter_city(self):
        self.find_element(locator=JobPagesLocators.CITY_FILTER_ON_JOB_PAGE, time=20).click()

    def click_on_experience_filter(self):
        self.find_element(locator=JobPagesLocators.EXPERIENCE_FILTER_ON_JOB_PAGE, time=20).click()

    def get_text_about_city_in_job_vacancy(self):
        city = self.find_elements(locator=JobPagesLocators.CITY_IN_JOB_VACANCY, time=20)
        return city


class MainPage(BasePage):
    def click_on_job_page(self):
        self.find_element(locator=MainPagesLocators.JOB_PAGES_LOCATOR, time=2).click()

    def click_on_salary_page(self):
        self.find_element(locator=MainPagesLocators.SALARY_PAGES_LOCATOR, time=2).click()

    def click_on_forum_page(self):
        self.find_element(locator=MainPagesLocators.FORUM_PAGES_LOCATOR, time=2).click()

    def get_title_page(self):
        title = self.driver.title
        return title


class SalaryPage(BasePage):
    def move_experience_slider(self):
        slider = self.find_element(SalaryPagesLocators.SLIDER_OF_EXPERIENCE, time=20)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(slider).click_and_hold().move_by_offset(-234, 0).release().perform()

    def open_job_vacancy_list(self):
        self.find_element(SalaryPagesLocators.JOB_VACANCY_LIST, time=20).click()

    def select_job_vacancy(self):
        self.find_element(SalaryPagesLocators.JUNIOR_QA_IN_JOB_VACANCY_LIST, time=20).click()

    def select_automation_qa_filter(self):
        self.find_element_for_clickable(SalaryPagesLocators.FILTER_AUTOMATION_QA, time=20).click()

    def select_technology_python(self):
        self.find_element(SalaryPagesLocators.FILTER_TECHNOLOGY_PYTHON, time=20).click()

    def move_english_slider(self):
        slider = self.find_element(SalaryPagesLocators.ENGLISH_LEVEL, time=20)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(slider).click_and_hold().move_by_offset(-130, 0).release().perform()

    def open_date_list(self):
        self.find_element(SalaryPagesLocators.DATE_LIST, time=20).click()

    def select_date(self):
        self.find_element(SalaryPagesLocators.DATE, time=20).click()

    def salary(self):
        salary = self.find_element(SalaryPagesLocators.SALARY, time=20).text
        return salary