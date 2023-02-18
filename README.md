# My Django App


## Adding Secrets

This app requires certain secrets to run, such as passwords or access tokens. To acquire and add these, follow these steps:

1. Create a file named `.env` in the root directory of this repository.

2. In the `.env` file, add your secrets in the following format:


This is a sample Django app that can be built and run using venv or Docker.

## Build and Run with venv

1. Create and activate a new virtual environment:

python3 -m venv env
source env/bin/activate


2. Install the required dependencies:

3. Start the Django development server:
python manage.py runserver

4. Access the app by navigating to `http://localhost:8000` in your web browser.

## Build and Run with Docker

1. Build the Docker image:

docker build -t my-django-app .

2. Start a container running the Docker image:


3. Access the app by navigating to `http://localhost:8000` in your web browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


docker run -p 8000:8000 my-django-app



