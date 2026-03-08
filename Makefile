install:
	uv sunc
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl 
lint:
	uv run ruff check brain_games
fix:
	uv run ruff check --fix
format:
	uv run ruff format brain_games
