all: setup django-setup

setup:
	pip install pylint
	pip install -r requirements.txt
	mkdir -p tmp/

django-setup:
	python manage.py migrate

lint:
	pylint meetupselector/
