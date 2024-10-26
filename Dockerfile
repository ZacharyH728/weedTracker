# Use the official Ubuntu image
FROM python:3.10-slim

WORKDIR /code

ENV TZ=America/New_York

COPY . ./app

# Install necessary dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]