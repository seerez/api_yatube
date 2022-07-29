<h3>Описание:</h3>
<p>API для приложение yatube. Позволяет получать, изменять и удалять информацию о постах, комментариях и группах</p>
<h3>Как запустить проект:</h3>
<p>Клонировать репозиторий и перейти в него в командной строке:<p>
<pre>git clone https://github.com/seerez/api_yatube.git</pre>
<pre>cd api_yatube</pre>
<p>Cоздать и активировать виртуальное окружение:</p>
<pre>python -m venv venv</pre>
<pre>source venv/bin/activate</pre>
<pre>python -m pip install --upgrade pip</pre>
<p>Установить зависимости из файла requirements.txt:</p>
<pre>pip install -r requirements.txt</pre>
<p>Выполнить миграции:</p>
<pre>python manage.py migrate</pre>
<p>Запустить проект:</p>
<pre>python manage.py runserver</pre>
<h3>Пример запросов и ответов</h3>
<p>* для отображения запросов и ответов используем Postman</p>
<p>POST запрос к <code>http://127.0.0.1:8000/api/v1/posts/</code></p>
<pre><code>{
    "text": "Всем привет! Это тестовая запись",
}</code></pre>
<p>GET запрос к <code>http://127.0.0.1:8000/api/v1/posts/</code></p>
<pre><code>{
    {
    "id": 1,
    "text": "запись 1",
    "pub_date": "2022-07-26T17:14:23.630745Z",
    "author": "admin",
    "image": null,
    "group": null
    }
}</code></pre>

