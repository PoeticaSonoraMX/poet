all: pull down up

pull:
	git pull

up:
	docker-compose -f docker-compose.prod.yml up --build -d

down:
	docker-compose -f docker-compose.prod.yml down

logs:
	docker-compose -f docker-compose.prod.yml logs -f

tests:
	docker-compose -f docker-compose.test.yml up --abort-on-container-exit --exit-code-from django
