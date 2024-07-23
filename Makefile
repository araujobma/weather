run_test:
	docker compose down
	docker compose up --build test
	docker compose down
	
run:
	docker compose up -d --build web
	
stop:
	docker compose down
