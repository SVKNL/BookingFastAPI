### Описание проекта:

АПИ для бронирования столиков в ресторане, упакованы
в два контейнера Докер, один для бэкенда, другой для БД,
также есть вольюм для бд.

Стэк:

```
Python
FastAPI
SQLAlchemy
Alembic
Docker
PostgreSQL
```

Запуск проекта:

```
Скачать репозиторий при помощи команды: git clone <ccылка с github>
Запускаем контейнеры командой: sudo docker compose -f docker-compose.yml up
```


Выполнить миграции и сбор статики:

```
sudo docker compose -f docker-compose.yml exec web alembic revision --autogenerate -m "Создание таблиц"

sudo docker compose -f docker-compose.yml exec web alembic upgrade head
```
Провести тесты:

```
sudo docker compose -f docker-compose.yml exec web pytest app/tests
```

Проект доступен по адресу:

```
localhost:8000
```
Документация:
```
localhost:8000/api/docs#/
```

Автор:
Карпов Степан
[Github](https://github.com/SVKNL)
