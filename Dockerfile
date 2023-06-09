FROM python:3.11.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /pythonProject12
WORKDIR /pythonProject12

VOLUME /allure_test_results

CMD ["pytest", "-vv", "-s", "--alluredir=/allure_test_results", "test_dou.py"]

