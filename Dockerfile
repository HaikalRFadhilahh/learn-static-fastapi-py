# BASE IMAGE
FROM python:3.10.20-slim AS runtime

# ENV
ENV APP_NAME=
ENV APP_HOST=0.0.0.0
ENV APP_PORT=
ENV token=

# SETTING WORKDIR
WORKDIR /app

# COPY SC
COPY . .

# UPGRADE PIP
RUN python -m pip install --upgrade pip

# INSTALL DEPS
RUN python -m pip install -r /app/requirements.txt

# HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl -X GET http://127.0.0.1:8000/health --fail" ]

# ENTRYPOINT
ENTRYPOINT [ "python","/app/main.py" ]