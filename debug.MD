git clone https://github.com/yourusername/yourproject.git


mkvirtualenv env --python=python3.10

workon env


pip install -r requirements.txt

python manage.py migrate


source python3.10/bin/activate


pip freeze > requirements.txt
