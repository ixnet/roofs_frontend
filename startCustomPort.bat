pip install -r requirements/base.txt
python manage.py makemigrations
python manage.py migrate
SET /p b=[Enter server address]
python manage.py runserver %b%