Список основных команд
1. python virtualenv.pyz venv Создание виртуального окружения
2. source venv/bin/activate Активация виртуального окружения
3. pip install -r requirements.txt   Установка зависимостей
4. python mange.py migrate  Принятие миграций
5. python mange.py createsuperuser создание администратора для Джанго
6. python mange.py runserver запуск сервера
7. redis-server запуск redis
8. python -m celery -A mailing worker запуск Celery

Для создания рассылки необходимо добавить подписчиков(subscribers), и в Email создать и сохранить саму рассылку.
Создать .env файл и добавить туда следующие переменные:
MAIL_SMTP_ADDRESS= SMTP адресс 
MAIL_USER=пользователь полностью (example@example.com)
MAIL_PASSWORD=пароль 
MAIL_SMTP_PORT=порт
BACKEND_HOST=хост на котором запускается приложение
CELERY_URL=адрес redis сервера
