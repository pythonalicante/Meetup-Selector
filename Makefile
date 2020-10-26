all: setup django-setup lint test

setup:
	pip install flake8
	pip install -r requirements.txt
	mkdir -p tmp/

django-setup:
	python manage.py migrate

lint:
	flake8 meetupselector/

test:
	python manage.py test

prepush: lint test
	
