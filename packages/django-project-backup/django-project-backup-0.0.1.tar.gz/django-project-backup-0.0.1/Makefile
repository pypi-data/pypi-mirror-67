DOCKER=docker
DPATH=${CURDIR}

export DPATH
.PHONY:	clean build

clean:
	rm -rf ./dist/*
	rm -rf ./build/*
	rm -rf  ./src/django_sso_app.egg-info
	find ./src -name *.pyc -exec rm {} \;

build: clean
	python setup.py sdist bdist_wheel

