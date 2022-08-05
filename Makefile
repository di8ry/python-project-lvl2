install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

test:
	poetry run coverage run --source=gendiff -m pytest tests

cc-coverage:
	poetry run coverage xml

lint:
	poetry run flake8 gendiff
