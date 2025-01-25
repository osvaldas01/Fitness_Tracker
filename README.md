# Fitness Habit Tracker

A web application built with Django that helps users track their fitness habits and maintain consistency in their health journey.

## Features

- User authentication (register, login, logout)
- Create and manage fitness habits
- Daily habit tracking
- Progress visualization with completion rates
- Streak tracking for each habit
- Note-taking for daily completions
- Dashboard with overall statistics
- Mobile-responsive design

## Technologies Used

- Python 3.11
- Django 5.1
- PostgreSQL
- Bootstrap 5
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fitness-tracker
```

2. Create a virtual environment and activate it:
``` bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required dependencies:
``` bash
pip install -r requirements.txt
```

4. Set up the database:
* Install PostgreSQL if you havent already.
* Create a new database named "fitness_tracker_db".
* Update database settings in settings.py with your credentials.

5. Apply migrations:
``` bash
python manage.py makemigrations
pyhon manage.py migrate
```
6. Create a superuser account:
``` bash
python manage.py createsuperuser
```
7. Start the development server:
``` bash
python manage.py runserver
```

## Usage

- Register a new account or login
- Add habits you want to track from the dashboard
- Log your daily progress for each habit
- Add notes to track specific details about your progress
- View your statistics and streaks in the dashboard
- Delete habits you no longer want to track

## Project Structure
```
fitness_tracker/
├── habits/                 # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL configurations
│   └── templates/         # HTML templates
├── templates/             # Base templates
├── static/               # Static files (CSS, JS)
└── manage.py            # Django management script
```

## ## Contributing
Feel free to fork this project and submit pull requests for any improvements.

## Acknowledgments
- Built with Bootstrap for responsive design
- Uses Django's authentication system
- PostgreSQL for reliable data storage