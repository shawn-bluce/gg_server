runserver:
	docker-compose run --rm -p 6688:6688 development python manage.py runserver 0.0.0.0:6688

makemigrations:
	docker-compose run --rm development python manage.py makemigrations

migrate:
	docker-compose run --rm development python manage.py migrate

shell:
	docker-compose run --rm development python manage.py shell

bash:
	docker-compose run --rm -p 6688:6688 development bash

build:
	echo "通过Dockerfile构建镜像"
	docker-compose build
