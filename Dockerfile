FROM python:3.11.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /pythonProject12
WORKDIR /pythonProject12

CMD [ "pytest", "-vv", "-s", "--alluredir=/allure-results", "test_dou.py" ]
