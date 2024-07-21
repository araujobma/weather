include .env
export $(shell sed 's/=.*//' .env)

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

#test:
#	python -m pytest --vv

format:
	black *.py

lint:
	pylint --disable=R,C main.py

all: install format lint

build:
	docker compose build
	
run:
	#docker compose up -d
	# docker exec -it rabbitmq rabbitmq-plugins enable rabbitmq_management
	# docker compose down
	docker compose up
	rabbitmqctl add_user myuser mypassword &&\
	rabbitmqctl add_vhost myvhost &&\
    rabbitmqctl set_user_tags myuser mytag &&\
    rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
	

stop:
	docker compose down
