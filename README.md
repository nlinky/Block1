# Block1
Практическое задание к курсу "Автоматизация тестирования с помощью Selenium и Python"

Объект тестирования
http://demowebshop.tricentis.com/
Инструментарий:
- python
- selenium
- pytest

Особенности:
- с использованием паттерна PageObject (без использования сторонних фреймворков)

Цели:

закрепление материалов курса путем самостоятельного построения архитектуры и структуры проекта автотестов.
Детали задания:
1 Блок (неделя)

Покрыть автотестами (только критичные проверки):
1. регистрацию нового пользователя - http://demowebshop.tricentis.com/register
2. авторизацию пользователя - http://demowebshop.tricentis.com/login
3. смену пароля в на странице профиля http://demowebshop.tricentis.com/customer/changepassword

UPD:
- реализовать возможность запуска тестов в двух браузерах (chrome и firefox) путем указания параметра запуска pytest
- реализовать возможность запуска тестов в headless режиме браузера путем указания параметра запуска а pytest
- критичные проверки собрать в test suite (используя pytest.mark)
