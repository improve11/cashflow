# cashflow
1. Установите зависимости:
```bash
# Активируйте виртуальное окружение (рекомендуется)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Установите все необходимые пакеты
pip install django django-filter crispy-bootstrap5 django-crispy-forms pandas
```
2. Настройте базу данных:
```bash
# Примените миграции
python manage.py makemigrations
python manage.py migrate

# Создайте суперпользователя (для доступа в админ-панель)
python manage.py createsuperuser
# Следуйте инструкциям в терминале
```
3. Запустите веб-сервис:
```bash
python manage.py runserver
```
После запуска сервера перейдите в браузере по адресу:
http://localhost:8000 или http://127.0.0.1:8000
