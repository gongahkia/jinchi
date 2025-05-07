all:clean

clean:
	@echo "creating virtual environment..."
	@python3 -m venv myenv
	@echo "installing dependencies..."
	@pip install -r requirements.txt
	@echo "removing set up files..."
	rm -rf .pre-commit-config.yaml .git .gitignore README.md Makefile requirements.txt helper