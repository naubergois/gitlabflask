FROM python:3.10-alpine
ARG USERNAME=app
WORKDIR /${USERNAME}

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ARG USERNAME=app

RUN adduser --disabled-password --gecos '' ${USERNAME}

RUN chmod +x entrypoint.sh \
    && chown -R ${USERNAME}:${USERNAME} /${USERNAME}

USER ${USERNAME}

EXPOSE 3000

ENTRYPOINT [ "./entrypoint.sh" ]
