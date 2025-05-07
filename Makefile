all:clean

clean:
	@echo "installing dependencies..."
	@pip install -r requirements.txt
	@echo "removing set up files..."
	rm -rf .pre-commit-config.yaml .git .gitignore README.md Makefile requirements.txt helper