# 🌿 Nature Blog — Django Web Application

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?logo=javascript\&logoColor=black)
![jQuery](https://img.shields.io/badge/jQuery-3.x-0769AD?logo=jquery\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

Современный веб-блог на Django с аутентификацией, управлением статьями и интерактивным интерфейсом.

---

## 🚀 Demo

> После запуска доступно по адресу:
> **http://127.0.0.1:8000/**

---

## ✨ Основные возможности

* 🔐 Регистрация / вход / выход пользователей
* ✍️ Создание и просмотр статей (CRUD-основа)
* 👤 Привязка статей к автору
* 📄 Список статей с датой публикации
* 🎯 Сворачивание/разворачивание постов (JS)
* 🎨 Hover-эффекты и кастомные кнопки
* 🖼️ Параллакс в шапке (scroll-based animation)
* 💎 Центрированный layout, карточки, тени, градиенты

---

## 📸 Preview

![Main](screenshots/main.png)
![Article](screenshots/article.png)
![Create article](screenshots/create-article.png)
![Registry](screenshots/registry.png)
![Login](screenshots/login.png)

---

## 🧱 Стек технологий

* **Backend:** Django, Python
* **Frontend:** HTML, CSS, JavaScript (jQuery)
* **DB:** SQLite
* **Templates:** Django Templates
* **Static:** CSS / JS / Images

---

## ⚙️ Установка и запуск

```bash
# Клонировать репозиторий
git clone https://github.com/helena6421/git-project.git

# Перейти в папку проекта
cd git-project

# Создать виртуальное окружение
python -m venv venv

# Активировать
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# Установить зависимости
pip install -r requirements.txt

# Миграции
python manage.py migrate

# Запуск
python manage.py runserver
```

Открыть в браузере:

```
http://127.0.0.1:8000/
```

---

## 🔑 Функционал

### 👥 Пользователи

* регистрация (валидация, уникальность username)
* вход/выход через Django auth
* отображение текущего пользователя

### 📝 Статьи

* создание статьи (только для авторизованных)
* список статей
* детальная страница статьи
* сворачивание/разворачивание контента

### 🎨 Интерфейс

* карточки статей с hover-эффектами
* кастомные кнопки
* параллакс-анимация (разные скорости слоёв)
* центрированный контейнер с тенями

---

## 💡 Особенности реализации

* Использован `ModelForm` + корректное хэширование пароля (`set_password`)
* Встроенная система аутентификации Django
* Разделение логики:

  * JS → поведение
  * CSS → отображение
* Параллакс через обработку события `scroll`
* Интерактивность без перезагрузки (частично, через JS)

---

## 📌 Автор

**Алёна Ласкина** | Frontend Developer
