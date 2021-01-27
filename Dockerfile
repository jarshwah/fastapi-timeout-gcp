FROM python:3.8-slim
RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
ENV POETRY_VIRTUALENVS_CREATE false
RUN poetry install --no-dev
COPY main.py /app/main.py
COPY utils.py /app/utils.py
CMD uvicorn main:app --workers 10 --port $PORT --host 0.0.0.0
