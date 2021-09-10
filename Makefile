all: down up

up:
	docker-compose -f docker-compose.prod.yml up --build -d

down:
	docker-compose -f docker-compose.prod.yml down

logs:
	docker-compose -f docker-compose.prod.yml logs -f
