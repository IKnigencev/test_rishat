<h1 align="center"> Тестовое задание Stripe. </h1>
<p align="center" style="font-size:20px;">
Сервер для создания платженой системы Stripe. 
<a href="https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit#">
Ссылка на тестовое задание.
</a>
</p>

---

<h2> Запуск. </h2>

### Клонирование проекта.

```git
git clone https://github.com/IKnigencev/test_rishat.git
```

### Создание и активация виртуального окружения.

``` 
python -m venv venv
```

Полный путь до файла

 \venv\Scripts\Activate.ps1

Например: 
```
& c:/Project/test_rishat/venv/Scripts/Activate.ps1
```

### Установка необходимых библиотек.

```pip
pip install -r requirements. txt
```

### Запуск сервера.

```
cd test_rishat

python manage.py runserver
```

## Тестирование.

Для доступа в панель admin необходимо ввести логин admin и пароль p@ssw0rd. 

При переходе на главную страницу вы увидите ссылки на имеющиеся в базе тестовые записи. При нажитии вы переместитесь на страницу этого объекта. 
Для тестов в базе создана одна запись с id = 1.
