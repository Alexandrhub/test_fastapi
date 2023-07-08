black: ## Run black formatter service
	python -m black . --check

flake8: ## Run flake8 linting tool service
	python -m flake8 .

migrate: ## Run alembic migration service
	python -m alembic upgrade head

install-deps: ## Install all dependencies
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@echo "Done."

up: ## Run Docker Compose services
	docker-compose -f docker-compose.yml up -d

down:  ## Shutdown Docker Compose services
	docker-compose -f docker-compose.yml down


clean:
	@echo "Cleaning up..."
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	@echo "Done"

run:
	@echo "Running the app..."
	uvicorn app.main:app --reload --port 8000
