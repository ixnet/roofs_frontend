pip install -r requirements/local.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver --settings=roofs_project.settings.local