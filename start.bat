pip install -r requirements/base.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver