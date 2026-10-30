# Một lệnh cho mỗi hiện vật (điều kiện gate: "chạy lại được bằng một lệnh").
COMPOSE_DEV := docker compose -f SUT/infra/compose.dev.yml
B ?= B1
SEED ?=

.PHONY: help install check up down demo battle

help:
	@echo "install   cài deps SUT (npm) + engines + Arena (uv)"
	@echo "check     typecheck, lint, test cả hai phía"
	@echo "up/down   hạ tầng dev một node"
	@echo "demo      TODO(Block 4): 1 file sạch + 1 EICAR qua Kafka, nhận verdict"
	@echo "battle    make battle B=B2 SEED=42"

install:
	cd SUT && npm install
	cd SUT/engines && uv sync
	cd Arena && uv sync

check:
	cd SUT && npm run typecheck && npm test
	cd SUT/engines && uv run ruff check && uv run mypy && uv run pytest -q
	cd Arena && uv run ruff check && uv run mypy && uv run pytest -q

up:
	$(COMPOSE_DEV) up -d

down:
	$(COMPOSE_DEV) down -v

demo:
	@echo "TODO(Block 4, bước 5). Gate: chạy trên máy sạch dưới 10 phút." && exit 1

battle:
	cd Arena && uv run arena run --battle $$(ls battles/$(B)_*.yaml) $(if $(SEED),--seed $(SEED))
