# Сервис уведомлений
---
*Сервис управления рассылками, API администрирования и получение статистики.*
*Выполнены дополнительные задания (1, 3, 5, 6, 8 ,9, 11, 12).*

---
### **Для запуска тестов необходимо:**
>python3 manage.py test
---
### **Для запуска необходимо:**
1. Клонировать репозиторий:
> git clone https://github.com/A-Sergey/Drf_mailing.git
2. В директории проекта создать файл .env и заполнить:
>SECRET_KEY=secret key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
TOKEN=token
URL_API=url_api
SERVER_EMAIL = server_mail
DEFAULT_FROM_EMAIL = default_from_email
EMAIL_BACKEND = email_backend
EMAIL_PORT = port
EMAIL_HOST = email_host
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
EMAIL_USE_TLS = True
SEND_STAT=example@example.ru #email для отправки статистики
3. В директории проекта создать виртуальное окружение:
>python3 -m venv venv
4. Активировать виртуальное окружение:
>source venv\bin\activate
5. Установка зависимостей:
>pip3 install -r requirements.txt
6. Создать миграции:
>python3 manage.py makemigrations
>python3 manage.py migrate
7. Запустить сервер:
>python3 manage.py runserver 0.0.0.0:8000
8. Запустить celery + планировщик:
>celery -A drf_mailing worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
9. Запустить flower:
>celery -A drf_mailing flower -l info
---
### **Для запуска с помощью docker-compose необходимо:**
1. Клонировать репозиторий:
> git clone https://github.com/A-Sergey/Drf_mailing.git
2. В директории проекта создать файл .env и заполнить:
>SECRET_KEY=secret key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
TOKEN=token
URL_API=url_api
POSTGRES_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=port
SERVER_EMAIL = server_mail
DEFAULT_FROM_EMAIL = default_from_email
EMAIL_BACKEND = email_backend
EMAIL_PORT = port
EMAIL_HOST = email_host
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
EMAIL_USE_TLS = True
SEND_STAT = example@example.ru #email для отправки статистики
3. Собрать и запустить контейнеры:
>sudo docker-compose up -d --build
4. Для остановки контейнеров необходимо:
>sudo docker-compose stop
---
### **API сервиса уведомлений**
- API
>http://0.0.0.0:8000/api/v1/
- Клиенты:
>http://0.0.0.0:8000/api/v1/clients/
- Просмотр и редактирование \<pk> клиента:
>http://0.0.0.0:8000/api/v1/clients/\<pk>/
- Рассылки:
>http://0.0.0.0:8000/api/v1/mailings/
- Просмотр и редактирование \<pk> рассылки:
>http://0.0.0.0:8000/api/v1/mailings/\<pk>/
- Сообщения:
>http://0.0.0.0:8000/api/v1/messages/
- Просмотр и редактирование \<pk> сообщения:
>http://0.0.0.0:8000/api/v1/messages/\<pk>/
- Статистика по рассылкам:
>http://0.0.0.0:8000/api/v1/mailings/complited_mailing/
- /docs проекта:
>http://0.0.0.0:8000/docs/
- Celery flower:
>http://0.0.0.0:5555/
