# VolunteerDoctorApp

Volunteer Doctor

## Steps

1. Clone this repository by running `git clone https://github.com/volunteerdoctor/VolunteerDoctorApp.git`.
2. Create a virtualenv by running `virtualenv ../vd-venv --python=python3`.
3. Run `source source ../vd-venv/bin/activate`.
4. Run `pip install -r requirements.txt`.
5. Run `python manage.py makemigrations` to create migrations.
6. Run `python manage.py migrate` to apply migrations.
7. Run `python manage.py runserver` and visit the url `http://127.0.0.1:8000/`.
