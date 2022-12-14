<h1 align="center">Web UI automation project for amazon marketplace <a href="https://www.amazon.com" target="_blank"><img src="https://github.com/Fatalwgx/README/blob/master/icons/amazon_icon.png" width="300" height="100" alt="Logo"/></a></h1>

&#8287;&#8287;&#8287;&#8287;&#8287;
## :open_book: Summary:
- [Technologies and tools](#gear-Technologies-and-Tools-used-in-the-project)
- [Description](#heavy_check_mark-Description)
- [Running tests using Jenkins](#-Running-tests-using-Jenkins)
- [Running tests locally](#computer-Running-tests-locally)
- [Analytics and Reports](#bar_chart-Analytics-and-Reports)
  - [Allure](#-allure)
  - [Telegram](#-telegram)

&#8287;&#8287;&#8287;&#8287;&#8287;
## :gear: Technologies and Tools used in the project
  <p align="left">
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/python.svg" title="Python" width="50" height="50"  alt="python"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/pycharm.svg" title="Pycharm" width="50" height="50"  alt="pycharm"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/pytest.svg" title="Pytest" width="50" height="50"  alt="pytest"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/selene.png" title="Selene" width="50" height="50"  alt="selene"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/selenoid.svg" title="selenoid" width="50" height="50"  alt="selenoid"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/jenkins.svg" title="Jenkins" width="50" height="50"  alt="jenkins"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/allure.svg" title="Allure" width="50" height="50"  alt="allure"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/testops.svg" title="Testops" width="50" height="50"  alt="testops"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/github.svg" title="Github" width="50" height="50"  alt="github"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/telegram.svg" title="Telegram" width="50" height="50"  alt="telegram"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/icons/jira.svg" title="Jira" width="50" height="50"  alt="jira"/>
 </p>


&#8287;&#8287;&#8287;&#8287;&#8287;
## :heavy_check_mark: Description
Web UI automation is performed in Python using Selenium webdriver along side Selene(A selenide like api for python selenium). Framework structure follows PageObject design pattern.
This project is supposed is also meant to perform API and mobile testing, but this functionality is not yet implemented
  
## :heavy_check_mark: Tested functionality
> - Searching from products and fetching results
> - Changing locale
> - Changing search categories
> - Authorization
> - Adding products to cart
> - Presence of added products in cart
> - Verification of various headers and elements on different pages


&#8287;&#8287;&#8287;&#8287;&#8287;
## <img src="https://github.com/Fatalwgx/README/blob/master/icons/jenkins.svg" width="50" height="50"  alt="jenkins"/> Running tests using Jenkins
  
  Setting up Jenkins:

  <details><summary>1. To be filled.</summary>
  <p align="center">
    <div>Right now the job is set-up on a non-public server, instructions on job setup process will be added at a later date.</div>
  </p>
  </details>
  
  
&#8287;&#8287;&#8287;&#8287;&#8287;
## :computer: Running tests locally

To run tests locally:
1. Install poetry if not installed
2. Create ".env" file in project root directory and specify credentials for selenoid
```
LOGIN='selenoid_login'
PASSWORD='selenoid_password'
```
3. Specify a link to your selenoid host at "tests/conftest" for "command_executor" webdriver parameter
```
driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
```
4. From project root execute a terminal command
```
poetry run pytest tests/
```

&#8287;&#8287;&#8287;&#8287;&#8287;
## :bar_chart: Analytics and Reports
  
### <img src="https://github.com/Fatalwgx/README/blob/master/icons/allure.svg" width="50" height="50"  alt="allure"/> Allure

Test results are generated as Allure reports and are attached to a ran Jenkins job(Integration with Allure Testops and Jira is intended, but not yet implemented)
For each test html-document, screenshot, video and browser logs are attached.
  <p align="center">
    <img src="https://github.com/Fatalwgx/README/blob/master/report1.png" height=100% alt="allure"/>
    <img src="https://github.com/Fatalwgx/README/blob/master/report2.png" height=100% alt="allure"/>
  
  
https://user-images.githubusercontent.com/98048609/209472904-630c2211-5e9e-4e9d-b0e3-5398e634e480.mp4
  
  
&#8287;&#8287;&#8287;&#8287;&#8287;
### <img src="https://github.com/Fatalwgx/README/blob/master/icons/telegram.svg" width="50" height="50"  alt="telegram"/> Telegram

Test results are additionally sent as a notfication via chat messenger of choice or email. In this case - Telegram


<img src="https://github.com/Fatalwgx/README/blob/master/notification.png" height=100% alt="notify"/>

  
