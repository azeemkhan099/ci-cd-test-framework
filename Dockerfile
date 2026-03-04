FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --upgrade pip

# Copy requirements first (better caching)
COPY requirements.txt /app/requirements.txt

# Install dependencies + tools used in CI
RUN pip install -r /app/requirements.txt && pip install ruff pytest

# Copy the rest of the project
COPY . /app

CMD ["pytest", "-q"]
