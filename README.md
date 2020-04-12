# django-formvalidation #

## 專案介紹 ##

本專案使用Python的Django網站框架，基於ModelForm(資料模型表單)類別，來實作表單客製化驗證的方式，可以搭配[[Django教學10]客製化Django ModelForm表單欄位驗證的技巧](https://www.learncodewithmike.com/2020/04/django-custom-form-field-validation.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ pipenv migrate`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /customers (例：http://127.0.0.1:8000/customers/) 後，即可看到填寫的表單畫面。

![Alt text](https://1.bp.blogspot.com/-oKIJkJMr4aQ/XpLcxl70FaI/AAAAAAAAB0s/ZAXNrV7gGOwFsBZ6Np1yvGKSj86mY7blwCKgBGAsYHg/s1600/django_custom_form_field_validation.PNG "Optional title")
