# О проекте
![Static Badge](https://img.shields.io/badge/python%20-%20%23000000?logo=python)
![Static Badge](https://img.shields.io/badge/django%20-%20%23000000?logo=django)
![Static Badge](https://img.shields.io/badge/postgresql%20-%20%23000000?logo=postgresql)
![Static Badge](https://img.shields.io/badge/javascipt%20-%20%23000000?logo=JavaScript)
![Static Badge](https://img.shields.io/badge/webpack%20-%20%23000000?logo=webpack)
![Static Badge](https://img.shields.io/badge/docker%20-%20%23000000?logo=docker)
![Static Badge](https://img.shields.io/badge/html5%20-%20%23000000?logo=HTML5)
![Static Badge](https://img.shields.io/badge/css3%20-%20%23000000?logo=CSS3&logoColor=%231572B6)
![Static Badge](https://img.shields.io/badge/SASS%20-%20%23000000?logo=SASS)

## ТЗ

Технологии:
- Django 3.2
- Python 3.9
- Webpack 5
- Yarn
- MySQL 8 или PostgreSQL 14 как база данных (на выбор)
- Redis 6.2 или Memcached 1.6 для кэширования (на выбор)

Важные моменты:
- Вёрстка не важна
- Скорость не важна, но будет плюсом
- Важно качество архитектуры программы

Задача:
- Создать модели с книгами и авторами
- У книги могут быть несколько авторов
- Реализовать добавление книг и авторов
- Реализовать удаление книг и авторов
- Реализовать вывод книг и авторов
- Реализовать поиск книг и авторов

## Реализация

- Созданы необходимые модели с примерным минимальным набором полей
- Релизован функционал добавления и удаления книг и авторов
- Реализован поиск по книгам и авторам
- В качестве СУБД выбран `PostgreSQL`
- Прикручен `Redis`
- Прикручен `Webpack` и `SASS` (для удобства)
- Для удобной работы на фронте с m2m прикручена библиотека `django-select2`
- Для работы в prod-режиме используется `gunicorn` + `whitenoise`
- Для удобства добавлены фикстуры и всё завёрнуто в `docker`

### Развёртывание приложения

- Проверить файл `entrypoint.sh`, чтобы окончание строк было `LF`
- Переименовать `.env.example` в `.env` и заполнить своими данными при необходимости
- Собрать и запустить контейнер `docker-compose up --build`
- Приложение будет доступно по адресу http://localhost:8000/