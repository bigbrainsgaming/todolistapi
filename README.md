# todolistapi
 A todolist api endpoint coding exam for lawadvisor

# current statusS
 * the Task models.py is responsible for the logic in updating the positions of affected items in repositioning a todo item.
 * the models.py file has its own test. to run this, python manage.py test tasks.tests.models after doing 'steps to setup.'
 * the api.py file is the test file for testing the DRF API Endpoint. current status is not finished.

#  steps to setup
setup a virtualenvironment for the project

1. python -m venv <path/to/project>
2. cd <path/to/project>
   * run activate to start virtualenv python/pip
3. git clone <github_repo_url> .
4. cd todolistapi
5. pip install -r requirements.txt
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver 0.0.0.0:8000

