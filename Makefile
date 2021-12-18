.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: up
up: ## Start docker environment
	sleep 3 && xdg-open http://127.0.0.1:3000 & docker-compose up --build --abort-on-container-exit -t0


.PHONY: clean
clean: ## Clean up
	docker-compose down -t0
