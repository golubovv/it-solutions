Запуск проекта:

git clone https://github.com/golubovv/it-solutions.git

Не забудьте про виртуальное оркужение

python -m venv venv

venv\scripts\activate

pip install -r requirements.txt 

SQLite хватает для нужного функционала, подключать другие БД нет необходимости

python manage.py makemigrations

python manage.py migrate

django manage.py runserver

После запуска проекта вам необходимо перейти на урл "ticker", создать настройки текста, нажав на "create font" внизу страницы (или воспользоваться уже заготовленными), вы можете загружать видео с необходимой бегущей строкой