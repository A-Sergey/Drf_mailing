# Сервис уведомлений
---
Сервис управления рассылками, API администрирования и получение статистики.  
  
В данном проекте был задействован следующий стек: Django, Django REST framework, Celery, flower, OpenAPI, gunicorn, nginx, docker, postgreSQL, redis.

---
### **Для запуска тестов необходимо:**
>python3 manage.py test
---
### **Для запуска необходимо:**
1. Клонировать репозиторий:
> git clone https://github.com/A-Sergey/Drf_mailing.git
2. В директории проекта создать файл .env по примеру .env.example. И закомментировать переменные POSTGRES_*.  
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
2. В директории проекта создать файл .env по примеру .env.example.
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
