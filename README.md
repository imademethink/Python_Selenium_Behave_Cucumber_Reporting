# Python_Selenium_Behave_Cucumber_Reporting

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped

allure serve allure-report

