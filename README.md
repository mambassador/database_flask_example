# database_flask_example
This repository contains simple Flask project with SQLite to operate a database

### Features
#### 1. Count the number of unique artists
  - URI: http://127.0.0.1:5000/names/
#### 2. Count all tracks
  - URI: http://127.0.0.1:5000/tracks/
#### 3. Count the number of all tracks of specified genre
  - URI: http://127.0.0.1:5000/tracks/<genre>
#### 4. Display all track names and their length
  - URI: http://127.0.0.1:5000/tracks-sec/
##### 5. Count the average track length and total length of all tracks
  - URI: http://127.0.0.1:5000/tracks-sec/statistics/

### Usage

1. Clone this project repository to your destination folder
2. Create a virtual environment by command "python3 -m venv .venv" inside your project folder
3. Activate your new virtual environment by command "source .venv/bin/activate"
4. Install dependencies by command: "pip install -r requirements.txt"
5. Initialize the database with command "flask --app flask_db_app init-db"
6. Run the Flask application by command "flask --app flaskr_db_app run"
7. Switch to endpoints to use results

#### Used Python 3.10.6