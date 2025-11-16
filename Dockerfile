FROM jenkins/jenkins:lts

# Switch to root to install Python
USER root

# Install Python, venv, pip, git
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip git && \
    rm -rf /var/lib/apt/lists/*

# Switch back to jenkins user
USER jenkins
