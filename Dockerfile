FROM python:3.11.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /pythonProject12
WORKDIR /pythonProject12

# Встановлення Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.tgz \
    && tar -zxvf allure-2.14.0.tgz \
    && rm allure-2.14.0.tgz \
    && ln -s allure-2.14.0 allure

VOLUME /allure_test_results

CMD ["sh", "-c", "pytest -vv -s --alluredir=/allure_test_results && allure/bin/allure generate --clean /allure_test_results -o /allure_report"]