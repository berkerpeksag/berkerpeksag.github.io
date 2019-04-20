clean:
	rm build/*.html build/posts/*.html build/posts/archive/*.html

deploy:
    scp -r build wakefield@berkerpeksag.com:/home/wakefield/berkerpeksag

.PHONY: clean deploy
