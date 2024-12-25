PYTHON=python
VENV_DIR=.venv
VENV=$(VENV_DIR)/bin/python

$(VENV):
	$(PYTHON) -m venv $(VENV_DIR)

clean:
	rm docs/*.html docs/posts/*.html docs/posts/archive/*.html

build: $(VENV)
	$(VENV) build_html.py

serve:
	$(VENV) -m http.server --bind 127.0.0.1 8008

.PHONY: build clean serve
