FROM python:3.10-slim AS core

RUN mkdir -p /opt/application
WORKDIR /opt/application
COPY src/ ./


FROM python:3.10-alpine AS test

RUN mkdir -p /opt/application && mkdir -p /opt/results && pip install pylint
WORKDIR /opt/application
VOLUME /opt/results
COPY --from=core /opt/application ./
CMD ["pylint", "--output-format=json:/opt/results/result.json", "./"]


FROM python:3.10-slim AS steady

RUN useradd -d /opt/application -m -r -s /bin/false -U application
WORKDIR /opt/application
COPY --from=test --chown=application:application /opt/application ./
RUN pip install -r requirements.txt
EXPOSE 8080/tcp
CMD ["python", "/opt/application/main.py"]
