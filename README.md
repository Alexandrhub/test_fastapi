# Booking app

## Шаги для запуска приложения

1. Скопируй репозиторий    
```git clone https://github.com/Alexandrhub/test_fastapi.git```
2. Перейди в папку ```cd test_fastapi```, скопируй файлы конфигурации
```cd .env.example .env-non-dev``` и заполни их.
3. Выбери своё виртуальное окружение и запусти команду ```make install-deps``` для установки всех зависимостей.
4. Для запуска миграций ```make migrate```
5. Линтеры и форматтеры ```make black``` и ```make flake8```
6. Для локального запуска введи команду ```make run ```
7. При проблемах с запуском попробуйте команду ```make clean```
8. Для запуска всех сервисов (БД, Redis, веб-сервер (FastAPI), Celery, Flower, Grafana, Prometheus) необходимо использовать файл docker-compose.yml и команды ```make up ``` или ```make down``` 
для запуска и остановки соответственно



### Celery & Flower
Для запуска Celery используется команда  
```
celery --app=app.tasks.celery:celery worker -l INFO -P solo
```
Обратите внимание, что `-P solo` используется только на Windows, так как у Celery есть проблемы с работой на Windows.  
Для запуска Flower используется команда  
```
celery --app=app.tasks.celery:celery flower
``` 

Они уже включены в настройки запуска докер контейнера

### Dockerfile
Если вы меняли что-то внутри Dockerfile, то есть меняли логику составления образа
Запустите команду ```docker build .```

### Sentry
Для настройки логирования зарегестрируйтесь на [офф.сайте](https://sentry.io/welcome/) или зайдите через гугл/гитхаб
Выберите фреймворк своего проекта и скопируйте sentry_dns, который вам предложат и введите его в .env-non-dev файл.


### Grafana / Prometheus
[Гайд по настройке](https://grafana.com//tutorials/grafana-fundamentals/)

1. Для входа в кабинет нужно указать ```username: admin, password: admin```
2. Потом переопределить пароль
3. Чтобы заработали графики вы должны в grafana-dashboard указать свой uid в следующем куске кода:
```"datasource":{"type": "prometheus","uid": "ВАШ UID"} ```
4. Взять его можно из json-схемы предустановленных дашбордов  
   (в настройках add data source -> prometheus -> "выбираем имя").
Затем в Dashboards -> import -> Вставляем содержимое grafana-dashboard.json и выбираем какой-нибудь случайный uuid(и имя для дашборда)
5. Если не интересуют метрики / логирование можно отключить закоментировав строчки с sentry и instumentator в файле app/main.py и docker-compose

### Документация

- [x] Swagger UI <localhost:8000/docs>
- [x] ReDoc <localhost:8000/redoc>
- [x] Api routes <localhost:8000/api/v1/docs>

## Обратная связь
Любые комментарии, исправления, замечания пишите мне в [телеграм](https://t.me/alex_cherr).
