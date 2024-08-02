# Django Forms Clone by Redian Marku

Demo Image:
![](TwitterDemo.png)

## Setup

1. Git Clone the project with: ```https://gitlab.com/quera_group_3/form-creator.git```.

2. Move to the base directory: ```cd pythonProject1```

3. Create a new python enveronment with: ```python -m venv env```.

4. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.

8. Build the Docker image by running the following command in the base directory:
    
    ```docker build -t django .```.
    
9. Once the image is built, you need to run the container. Use the following command:

    ```docker-compose up --build```.
