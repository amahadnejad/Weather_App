<span><img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=green" /></span>

Weather App 🌤️

A simple Django-based web application that provides real-time weather updates for any city. Users can search for a city and view its temperature, humidity, and pressure with dynamic weather icons.

🚀 Features
Search for city-based weather updates
Displays temperature, humidity, and pressure
Uses OpenWeatherMap API for real-time data
Responsive and user-friendly UI

🔧 Installation
```

git clone https://github.com/amahadnejad/Weather_App.git  

cd Weather_App

python -m venv env

source env/bin/activate  # (Windows: env\Scripts\activate)

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.

🌍 Environment Variables
Create a .env file in the project's root and add:

```
SECRET_KEY=your_django_secret_key  
DEBUG=True  
OPENWEATHER_API_KEY=your_api_key
```
Replace your_api_key with your OpenWeatherMap API key.

📂 Project Structure
weather/ → Core weather fetching logic
templates/ → HTML templates
config/ → Django project settings

🤝 Contributing
Fork the repo & create a new branch
Make your changes & commit
Push & open a pull request
