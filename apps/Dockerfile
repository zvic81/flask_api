FROM python:3.10-alpine

WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip | python -m pip install cmake | python -m pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["/app/app.py"]
