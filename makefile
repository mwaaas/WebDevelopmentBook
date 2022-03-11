build:
	jupyter-book build doc

deploy: build
	ghp-import  -n -p -f doc/_build/html