FROM python:3.9-slim

# EN Varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --upgrade pip && pip install -r requirments.txt

COPY . /app/

COPY enterypoint.sh /app/enterypoint.sh

RUN chmod +x /app/enterypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/enterypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]






