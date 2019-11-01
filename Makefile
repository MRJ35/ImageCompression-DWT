start:
	pip3 install -r requirements.txt \
	&& python3 app.py

test:
	python3 -m unittest tests/*.py
