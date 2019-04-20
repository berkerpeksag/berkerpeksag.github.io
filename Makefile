clean:
	rm build/*.html build/posts/*.html build/posts/archive/*.html

deploy: clean
	python build_html.py
	cp -r static build
	scp -r build wakefield@berkerpeksag.com:/home/wakefield/berkerpeksag

.PHONY: clean deploy
