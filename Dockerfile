# Use the official Ubuntu image
FROM ubuntu:20.04

WORKDIR /code
#ENV FLASK_APP=weedTracker.py
#ENV FLASH_RUN_HOST=0.0.0.0

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    firefox \
    xvfb \
    libxrender1 \
    libx11-6 \
    libxi6 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    && pip3 install selenium \
    && apt-get clean

ENV DISPLAY=:99

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["xvfb-run", "python3", "weedTracker.py"]