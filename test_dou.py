import time
import pytest
from selenium import webdriver
from pages import MainPage, JobPage, SalaryPage, ForumPage


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=webdriver.ChromeOptions()
    )
    driver.set_window_size(1920, 1080)
    driver.get('https://dou.ua')
    mainPage = MainPage(driver)
    jobPage = JobPage(driver)
    salaryPage = SalaryPage(driver)
    forumPage = ForumPage(driver)
    yield driver, mainPage, jobPage, salaryPage, forumPage




@pytest.fixture(autouse=True)
def teardown(setup):
    yield
    driver, _, _, _, _ = setup
    driver.quit()


def test_main_page_title(setup):
    """
    In this test, I am testing the title of the main page
    :param setup:
    :return:
    """
    driver, mainPage, _,_,_ = setup
    title = mainPage.get_title_page()
    assert title == 'Спільнота програмістів | DOU'


def test_job_page_with_filters(setup):
    """
    In this test, I check several filters at the same time on job page and check the result they return
    :param setup:
    :return: "Київ" in all vacancies
    """
    driver, mainPage, jobPage, _, _ = setup
    mainPage.click_on_job_page()
    time.sleep(2)
    jobPage.click_on_QA()
    time.sleep(3)
    jobPage.click_on_filter_city()
    time.sleep(3)
    jobPage.click_on_experience_filter()
    time.sleep(3)
    city = jobPage.get_text_about_city_in_job_vacancy()
    for i in city:
        assert 'Київ' in i.text



def test_salary_page_with_filters(setup):
    """
    In this test, I check several filters at the same time on salary page and check the result they return
    :param setup:
    :return: 950$
    """
    driver, mainPage, _, salaryPage, _ = setup
    mainPage.click_on_salary_page()
    salaryPage.move_experience_slider()
    salaryPage.open_job_vacancy_list()
    salaryPage.select_job_vacancy()
    time.sleep(3)
    salaryPage.select_automation_qa_filter()
    time.sleep(3)
    salaryPage.select_technology_python()
    time.sleep(3)
    salaryPage.move_english_slider()
    salaryPage.open_date_list()
    salaryPage.select_date()
    time.sleep(3)
    salary = salaryPage.salary()
    assert salary == '950'


@pytest.mark.parametrize("title, description", [
    ("Test title 1", "Test description 1")
])
def test_add_topic(setup, title, description):
    """
    In this test, I check whether the site will allow an unregistered user to add a topic
    :param setup:
    :param title: Test title 1
    :param description: Test description 1
    :return:
    """
    driver, mainPage, _, _, forumPage = setup
    mainPage.click_on_forum_page()
    forumPage.click_on_add_topic()
    forumPage.set_title_of_topic(title)
    forumPage.switch_to_iframe()
    forumPage.set_description(description)
    forumPage.switch_to_default_content()
    forumPage.create_topic()
    res = forumPage.appear_window_for_log_in()
    assert res == 'Cкористайтесь акаунтом'


