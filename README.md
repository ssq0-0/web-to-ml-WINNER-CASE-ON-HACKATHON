# Обработка обращений граждан

## Введение

Наш проект предлагает инновационное решение для обработки и анализа обращений граждан, используя современные технологии искусственного интеллекта и веб-разработки. Мы стремимся облегчить коммуникацию между жителями и муниципалитетами, обеспечивая эффективное управление запросами и предложениями граждан.

### О проекте

Проект состоит из трех основных компонентов:

* Веб-сайт для подачи обращений: Платформа позволяет гражданам напрямую отправлять обращения к местным властям, упрощая процесс коммуникации и обеспечивая его прозрачность.

* Парсер комментариев из социальных сетей: Автоматизированный инструмент для сбора данных из пабликов в "Вконтакте", позволяющий анализировать общественное мнение и отзывы жителей.

* Система анализа и классификации обращений: Используя модель Rubert2-tinu для получения эмбеддингов и CNN для классификации, наша система определяет категории обращений и направляет их в соответствующие органы.

### Технические детали

Проект реализован с использованием следующих технологий и инструментов:

* Машинное обучение и AI: Jupyter Notebook, PyTorch, TensorFlow, Scikit Learn.
* Обработка и анализ данных: Matplotlib, Pandas, NLTK.
* Веб-разработка: Django, HTML, CSS.

### Уникальность проекта

Наш подход уникален сочетанием удобства использования, технологического новаторства и масштабируемости. Мы предлагаем не просто платформу для обращений, а полноценную экосистему для анализа и управления гражданскими инициативами.


# Установка и запуск

### 1. Подготовка сервера

* Установите Python и создайте виртуальное окружение:
```sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
```
* Установите сервер PostgreSQL (если используете другую СУБД, выполните соответствующую установку):

```
sudo apt install postgresql postgresql-contrib
```

Настройте базу данных в PostgreSQL:
```
sudo -u postgres psql
CREATE DATABASE yourdbname;
CREATE USER youruser WITH PASSWORD 'password';
ALTER ROLE youruser SET client_encoding TO 'utf8';
ALTER ROLE youruser SET default_transaction_isolation TO 'read committed';
ALTER ROLE youruser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;
\q
```

* Установите и настройте веб-сервер, например Nginx, и систему управления процессами, например Gunicorn:
```
sudo apt install nginx
pip install gunicorn
```
### 2. Настройка Django-проекта
Скопируйте ваш проект на сервер, используя Git или любой другой способ.
```git clone https://github.com/ssq0-0/web-to-ml ```

* Активируйте виртуальное окружение и установите зависимости проекта:
```
source venv/bin/activate
pip install -r requirements.txt
```

* Обновите настройки в settings.py:

-Установите DEBUG = False.
-Добавьте домен вашего сервера или IP-адрес в ALLOWED_HOSTS.
-Обновите конфигурацию базы данных в DATABASES согласно вашим настройкам.
-Настройте STATIC_ROOT и MEDIA_ROOT.
-Выполните сбор статических файлов:
```
python manage.py collectstatic
```

* Примените миграции к базе данных:
```
python manage.py migrate
```

### 3. Настройка Gunicorn

* Создайте файл gunicorn.service в /etc/systemd/system/, чтобы управлять Gunicorn как службой systemd:

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=youruser
Group=www-data
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/project/project.sock your_project_name.wsgi:application

[Install]
WantedBy=multi-user.target
```

* Запустите и включите службу:
```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 4. Настройка Nginx

* Создайте файл конфигурации Nginx для вашего сайта в /etc/nginx/sites-available/ и создайте символическую ссылку в /etc/nginx/sites-enabled/.

Пример конфигурации:
```
nginx
Copy code
server {
    listen 80;
    server_name your_domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/project/project.sock;
    }
}
```
 * Проверьте конфигурацию Nginx и перезапустите службу:

```
sudo nginx -t
sudo systemctl restart nginx
```

### 5. Настройка брандмауэра

Разрешите трафик на необходимых портах (обычно это порт 80 и 443 для HTTPS):
```
sudo ufw allow 'Nginx Full'
```
После выполнения этих шагов ваш Django-проект должен быть доступен по указанному домену или IP-адресу.

# Пример использования.
![Общая страница](https://i.ibb.co/1q2kMpZ/2024-03-16-01-11-22.jpg)

И далее получаем ответ в виде уведомления:
![Ответ](https://i.ibb.co/4PqQ1f2/2024-03-16-01-11-30.png)

Так же есть страница модератора. Функционал страницы модератора представляет из себя следующее:

- запуск парсера вконтакте на определенную группу(указывается ссылка в файле парсера)
- выгрузка собранных обработанных моделью машинного обучения данных модератору
- после того, как модератор проанализирует данные он делает выбор: отправить в базу данных(согласиться с результатом работы модели), отправить на переобучение, удалить из базы

Выгрузка производится в удобной для человека форме:

![Модератор](https://i.ibb.co/KKyCBSk/2024-03-16-01-12-03.png)

### Настройка парсера

* В функции поменять токен от страницы вк:
  ```
  def do_something():
    token = 'ваш токен'
  ```

* В этой же функции прописать домен группы, комментарии которой нужно парсить:
```
domain = 'example_domain'
```

# Контакты разработчиков команды 'The Boys'
[Ратников Максим - Front-end разработчик](https://github.com/RatnikovMax)

[Шебани Антон - Data Science, Backend](https://github.com/modecstap)

[Дьяков Никита - Backend](https://github.com/ssq0-0)

[Гречихин Никита - Machine Learning](https://github.com/f0rxz)

Виталий Нант - Дизайн



