start:
	env/bin/python run.py

pyresttest:
	env/bin/pyresttest http://localhost:8080/ test/main.yaml

env:
	pip install virtualenv && virtualenv env

install: env
	env/bin/pip install flask flask-sqlalchemy flask-jwt pyresttest