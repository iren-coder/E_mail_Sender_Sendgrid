Приложение для отправки писем c возможность отложенной отправки (использованы Процессы Python).
Реализовано через Sendgrid.

Oтправка писем идет через mail.ru, на локальном сервере необходимо указать переменные окружения: 
SECRET_KEY = <ваш SECRET_KEY для Django> 
EMAIL_HOST_USER = имя Вашего почтового ящика на mail.ru в формате example@mail.ru 
EMAIL_HOST_PASSWORD = пароль для Вашего почтового ящика

Для локального запуска:
1. Скопируйте репозиторий.
2. Создайт виртуальное окружение: python -m venv env
3. Активировать виртуальное окружение: source env/bin/activate
4. Установить зависимости: pip install -r requirements.txt.        
5. Запустить сервер python manage.py runserver

