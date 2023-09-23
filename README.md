# Django Web Scraper

## Технологии проекта:

1. [Django Framework](https://docs.djangoproject.com/en/4.0/)
2. [PostgreSQL](https://www.postgresql.org/)
3. [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#)

## Запуск  

### При помощи [docker compose](https://docs.docker.com/compose/)
1. Необходимо скачать репозиторий и перейти в него:  
   ```git clone https://github.com/Cthupby/django-web-scraper.git```  
   ```cd django-web-scraper```  
2. Создать Docker образ:  
   ```docker build -t django_web_scraper_image .```  
3. Создать файл окружения ".env" и указать в нем переменные:  
   ```DEBUG``` - Режим отладки "1" или "0";  
   ```DJANGO_SUPERUSER_PASSWORD``` - Пароль администратора по умолчанию;  
   ```DJANGO_SUPERUSER_USERNAME``` - Имя администратора по умолчанию;  
   ```DJANGO_SUPERUSER_EMAIL``` - Email администратора по умолчанию;  
   ```DB_USER``` - Имя пользователя для базы данных;  
   ```DB_PASSWORD``` - Пароль пользователя для базы данных;  
   ```DB_HOST``` - Хост базы данных;  
   ```DB_PORT``` - Порт базы данных;  
3. Создать и активировать Docker контейнеры:  
   ```docker-compose up -d --build```  
4. Перейти в административную панель  
и зайти по паролю и имени администратора из окружения:   
   ```http://0.0.0.0:8000/admin```
