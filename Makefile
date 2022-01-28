dist: ## build source and wheel packages
	python setup.py sdist bdist_wheel

release: dist ## package and upload a relase