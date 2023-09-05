<h1 align="center">Docker+Django+Celery+Redis(учебный проект)</h1>
<ol>
    <li><h4>28 августа 2023<br><a href="https://youtu.be/XEjJpGv5BsY?si=sFkzkLznfjYvqD_9">Ссылка на урок</a> Настройка окружения:<br>
    """     Docker+Django+PostgreSQL    """</h4></li>
    <li><h4>29 августа 2023<br>
    Создание минимального приложения с API интерфейсом для работы с Celery<br>
    """     http://127.0.0.1:8000/api/subscriptions/?format=json    """</h4>
    </li>
    <li><h4>2 сентября 2023<br>
    Выбор полей и оптимизация (n+1) запросов. </h4>
    </li>
    <li><h4>3 сентября 2023<br>
    Рассмотр функций Annotate и Aggregate.<br>
    Установка Celery, Redis и Flover (получил зацикливание, пока не дописал аргументы декоратору и namespase=CELERY но это не точно, т.к. через pip установил celery[redis], подтянулись еще несколько пакетов, все перенес `pip freeze > requirements.txt`)</h4></li>
    <li><h4>5 сентября 2023<br>
    Создание tasks , оптимизация и автоматизация расчета при изменении полей, добавление celery_singleton, использование with transaction.atomic():</h4></li>
</ol>