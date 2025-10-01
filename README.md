**Установка и запуск**
**1. Клонирование репозитория**
 
git clone https://github.com/Sealal07/django_blog_PHY43_.git
cd dj_blog/site_blog

**2. Создание виртуального окружения**
Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

**3. Установка зависимостей**
Затем установите зависимости:

pip install -r requirements.txt

**4. Настройка базы данных**

python manage.py migrate

**5. Создание суперпользователя (опционально)**
 
python manage.py createsuperuser

6. Запуск сервера разработки
 
python manage.py runserver

Приложение будет доступно по адресу: http://127.0.0.1:8000/

 
