## **Yatube API** ## 
**Описание**
**Yatube API** - это **RESTful API** для веб-приложения **Yatube**, предоставляющее CRUD (Create, Read, Update, Delete) функциональность для управления записями и комментариями.Аутентификация пользователя осуществляется по токену TokenAuthentication. Аутентифицированные пользователи имеют разрешения на изменение и удаление своих записей, в остальных случаях доступ предоставляется только для чтения.

**Эндпоинты API (API Endpoints).**

**api/v1/api-token-auth/(POST):** Аутентификация по логину и паролю для получения токена.

**api/v1/posts/(GET, POST):** Получение списка всех постов или создание нового поста.

**api/v1/posts/{post_id}/(GET, PUT, PATCH, DELETE):** Получение, редактирование или удаление поста по его id.

**api/v1/groups/(GET):** Получение списка всех групп записей.

**api/v1/groups/{group_id}/(GET):** Получение информации о группе по её id.

**api/v1/posts/{post_id}/comments/(GET, POST):** Получение списка всех комментариев к посту с id=post_id или создание нового комментария.

**api/v1/posts/{post_id}/comments/{comment_id}/(GET, PUT, PATCH, DELETE):** Получение, редактирование или удаление комментария по его id у поста с id=post_id.

**Установка и запуск.**

**Клонировать репозиторий:**

git clone git@github.com:d1g-1t/api_yatube.git

**Перейти в папку проекта:**

cd api_yatube

**Создать и активировать виртуальное окружение:**

python -m venv venv
source venv/Scripts/activate

**Обновить pip:**

python -m pip install --upgrade pip

**Установить зависимости:**

pip install -r requirements.txt

**Выполнить миграции:**

python manage.py migrate

**Запустить сервер:**

python manage.py runserver