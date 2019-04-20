clean:
	rm build/*.html build/posts/*.html build/posts/archive/*.html

build: clean
	python build_html.py

deploy: build
	cp -r static build
	scp -r build wakefield@berkerpeksag.com:/home/wakefield/berkerpeksag

serve:
	python3 -m http.server --bind 127.0.0.1 8008

upload-nginx-config:
	scp conf/nginx.conf wakefield@berkerpeksag.com:/home/wakefield/berkerpeksag

.PHONY: build clean deploy serve upload-nginx-config
