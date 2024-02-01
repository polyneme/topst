
install-env:
	@echo "Installing environment from current workspace..."
	@echo cwd: $(CURDIR)
	poetry install --no-root

activate-env:
	@echo "Activating environment..."
	poetry shell

deactivate-env:
	@echo "Deactivating environment..."
	deactivate

clean:
	@echo "Cleaning..."
	rm *.json

stop-terminus-server:
	@echo "Stopping terminus server..."
	cd ../terminusdb & docker compose down

run-terminus-server:
	@echo "Running terminus server..."
	# @echo "Warning: This will close existing server remove all existing data..."
	# docker compose rm
	# docker compose run
	cd ../terminusdb & docker compose up 


run-full-pipeline-demo:
	@echo "Running full pipeline demo..."
	python full_pipeline_demo.py