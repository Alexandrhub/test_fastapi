black: ## Run black formatter service
	python -m black . --check

flake8: ## Run flake8 linting tool service
	python -m flake8 .

migrate: ## Run alembic migration service
	python -m alembic upgrade head

install-deps: ## Install all dependencies
	python -m pip install -r requirements.txt

up: ## Run Docker Compose services
	docker-compose -f docker-compose.yml up -d

down:  ## Shutdown Docker Compose services
	docker-compose -f docker-compose.yml down



