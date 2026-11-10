# Weather App Backend
This is a weather app backend only which lets you search for weather from any city and then it also saves your past searches.

## Tech Stack
1. FastAPI
2. Uvicorn
3. SQLAlchemy
4. Requests
5. python-dotenv
6. Pydantic
7. SQLite (database)
8. OpenWeatherMap API (weather data)

## Features
1. by typing a city name you can search weather
2. it shows current weather like temp, conditions, humidity, wind.
3. Shows 5-day forecast
4. Saves every search you make into a database
5. can look back at old searches
6. can update a saved search to get fresh weather
7. It can delete a saved search

# Setup/How to Run

1. Clone this repository
```
git clone https://github.com/jawariahassan2001-cmd/weather-app-backend.git
cd weather-app-backend
```

2. Create a virtual environment
python -m venv venv

3. Virtual environment (Windows) Activation
venv\Scripts\Activate.ps1

4. Required packages Installation
pip install -r requirements.txt

5. Set your `.env` file
   - Copy `.env.example` and rename it to `.env`
   - Add your own OpenWeatherMap API key inside it

6. Running the server
 uvicorn app.main:app --reload

7. Open your browser and go to:
http://127.0.0.1:8000/docs


## API endpoints

## GET /about
{
  "developer": "Jawaria Hassan",
  "pm_accelerator_description": "The Product Manager Accelerator Program is designed to support PM professionals through every stage of their careers. From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations. Our Product Manager Accelerator community are ambitious and committed. Through our program they have learnt, honed and developed new PM and leadership skills, giving them a strong foundation for their future endeavors. Learn more at https://www.pmaccelerator.io/"
}

## GET /searches
Returns a list of all saved past searches.

## POST /searches
Takes a city name then fetches real weather data, and saves it.

## PUT /searches
Refetches fresh weather for a saved search and then update it.

## DELETE /searches
Removes already saved search from the database. 

# Structure of Weather App Project:
# app 
## __init__.py 
 makes this folder a proper Python package

## main.py
API routes

## database.py 
database connection

## models.py
 database table

## schemas.py 
input/output validation

## crud.py
 create/read/update/delete logic

## weather_service.py
 talks to the weather API

## requirements.txt
 list of packages needed

## .env.example
 template showing what environment variables are needed

## .gitignore
  tells git what not to upload

## README.md 
this file

# Note
 .env, venv/, and weather.db are excluded from this repo (see .gitignore) — venv/ gets recreated when you install requirements, weather.db gets created automatically when the app runs, and .env needs to be set up manually with your own API key.




