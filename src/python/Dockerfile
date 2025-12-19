FROM python:3.13-alpine

RUN --mount=type=bind,src=requirements.txt,dst=requirements.txt \
  pip install -r requirements.txt
