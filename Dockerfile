FROM jenkins/jenkins:lts

USER root

# Install Python3, pip, and venv
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    apt-get clean

USER jenkins

