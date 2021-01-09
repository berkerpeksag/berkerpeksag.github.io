clean:
	rm docs/*.html docs/posts/*.html docs/posts/archive/*.html

build:
	python build_html.py

serve:
	python3 -m http.server --bind 127.0.0.1 8008

.PHONY: build clean serve
