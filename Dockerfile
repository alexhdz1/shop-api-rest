FROM python:3.9

# build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    wget \
    gettext

RUN mkdir /var/log/uwsgi

# Install dockerize to wait db to be ready
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Web app source code
COPY . /app

WORKDIR /app

# POETRY SETUP
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN wget -O - https://install.python-poetry.org | python - \
    && poetry --version  \
    && poetry config virtualenvs.create false

RUN poetry install --no-dev --no-interaction --no-ansi -vvv
RUN poetry shell
RUN pip install -U uwsgi

EXPOSE 8000

EXPOSE 3031

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD [ "uwsgi", "--http", "0.0.0.0:3031", \
               "--protocol", "uwsgi", \
               "--wsgi", "backend_crm.wsgi:application" ]