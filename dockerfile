FROM python:3.9

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy app code
WORKDIR /app/
COPY . /app/

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

