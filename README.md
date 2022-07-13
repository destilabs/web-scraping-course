# Udemy Scraping Course
## _Repository for Udemy Course_
https://www.udemy.com/course/practical-web-scraping-course/

## Tutorials

- Tracking HTTP Requests
- Beautiful Soup 4
- Selenium Intro
- Authentication with Selenium
- Passing captcha with Selenium
- Pagination wtih Selenium
- Scraping dynamic websites with Selenium
- Scraping HighCharts.js

## Installation

Course requires Python3.6.9 to be installed.
1. [On Windows](https://www.tutorialspoint.com/how-to-install-python-in-windows)
2. [On Linux](https://opensource.com/article/20/4/install-python-linux)
3. [On MacOS](https://docs.python-guide.org/starting/install3/osx/)

Next run following comands: 

```sh
$ git clone git@github.com:destilabs/web-scraping-course.git
$ cd web-scraping-course
$ python3.9 -m pip install virtualenv
$ python3.9 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Selenium Installation

1. [On WSL Windows](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/) *
2. [On Linux](https://www.geeksforgeeks.org/how-to-install-selenium-tools-on-linux/)
3. [On MacOS](https://www.geeksforgeeks.org/how-to-install-selenium-on-macos/)

'*' I encourage you to use WSL on Windows 

## Docker Installation

[Course requires Docker to be installed](https://docs.docker.com/engine/install/) 

```sh
$ docker pull selenium/standalone-chrome
$ docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome
```

## Verify Installation
```sh
$ python -m unittest
```
