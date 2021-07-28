# API для Yatube
Финальный проект спринта "API для Yatube".

Курс Яндекс [Практикум](https://praktikum.yandex.ru/) Python-Разработчик

---
## Установка
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/RomanCherkasov/api_final_yatube.git
```
```bash
cd api_final_yatube
```
2. Создать venv
```bash
python3 -m venv venv
```
```bash
source venv/Scripts/Activate (windows)
или
source venv/bin/activate (osx/linux)
```
3. Установить зависимости
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Создать и выполнить миграции
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Запустить проект
```bash
python3 manage.py runserver
```
---
## Примеры запросов
Запрос GET
```
http://127.0.0.1:8000/api/v1/posts/
```
Ответ
```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
  }
]
```
---
Запрос POST
```
http://127.0.0.1:8000/api/v1/posts/
```
Нагрузка (Payload)
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ 200(Успешно)
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Ответ 401(Не авторизован)
```json
{
  "detail": "Учетные данные не были предоставлены."
}
```