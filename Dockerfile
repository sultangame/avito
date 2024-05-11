FROM python:3.11.8-alpine3.18

RUN mkdir /backend
RUN cd /backend
WORKDIR /backend
COPY . /backend
RUN pip install poetry
RUN poetry install

RUN chmod a+x docker/*.sh

CMD ["uvicorn", "main:app", "--reload", "--port 4000"]
