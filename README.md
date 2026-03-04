#Learning Project.
# CI/CD Test Automation Framework

Python-based test automation framework for validating structured datasets, with CI execution in Jenkins.

## What this repo is for (Learning Goals)

I’m using this project to practice:

* Writing dataset validations as reusable Python modules
* Running tests with `pytest` and exporting CI-friendly reports (JUnit XML)
* Building a Jenkins pipeline to run tests on every change
* Publishing test reports as Jenkins artifacts

## Project Structure

* `src/` — validation modules (business rules / schema checks)
* `tests/` — test cases + sample datasets
* `reports/` — generated test outputs (ignored or kept depending on CI setup)
* `Jenkinsfile` — Jenkins pipeline definition

## Requirements

* Python 3.10+ (3.11 recommended)
* `pip` + `venv`
* (CI) Jenkins with a Pipeline job

## Setup (Local)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests (Local)

```bash
pytest -q
```

## Generate JUnit XML Report (for CI)

```bash
mkdir -p reports
pytest --junitxml=reports/results.xml
```

## Jenkins CI Pipeline

This repository includes a `Jenkinsfile` that:

1. Checks out the code
2. Installs dependencies
3. Runs `pytest`
4. Publishes `reports/results.xml` as a test report
5. Archives generated artifacts (if configured)

### Jenkins Setup (Quick)

* Create a **Pipeline** job in Jenkins
* Point it to this repository
* Ensure the agent/node has Python installed
* Run the job

## Notes / Next Improvements

Planned upgrades as I learn more:

* Add linting (`ruff`) and formatting checks
* Add type checks (`mypy`)
* Add coverage reports (`pytest-cov`)
* Add sample HTML report generation
* Add Dockerized CI execution for consistent builds

