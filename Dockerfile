# Python Based Docker
FROM python:3.11-slim

# Avoid latest due to pandas build errors on Python 3.13

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg aria2 build-essential gcc g++ libffi-dev libpq-dev python3-dev -y

# Updating Pip Packages
RUN pip3 install -U pip

# Copying Files
COPY . /EXTRACTOR

# Set Working Directory
WORKDIR /EXTRACTOR

# Installing Requirements
RUN pip3 install -U -r requirements.txt

# Running MessageSearchBot
CMD ["/bin/bash", "start.sh"]
