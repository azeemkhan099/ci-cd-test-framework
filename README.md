# CI/CD Test Automation Framework

## Overview
Python-based automated test framework for structured datasets with Jenkins CI/CD integration.

## Structure
- src/        Python validator modules
- tests/      Test scripts + sample datasets
- reports/    Generated test reports
- Jenkinsfile Jenkins pipeline definition

## Running Locally
source venv/bin/activate
pytest --junitxml=reports/results.xml

## Running via Jenkins
- Install Jenkins
- Create a pipeline pointing to this repo
- Run the job to automatically execute tests and archive reports
