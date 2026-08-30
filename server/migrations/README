# Workout Tracking API

A RESTful Workout Tracking API built with **Flask**, **SQLAlchemy**, **Flask-Migrate**, and **SQLite**.

The application allows users to manage exercises, workouts, and the exercises performed during each workout. It provides CRUD operations through RESTful API endpoints and uses SQLAlchemy relationships to connect workouts and exercises.

---

## Project Overview

The Workout Tracking API is designed to help users record and manage their fitness activities.

The application manages three main entities:

* **Exercise** — Stores individual exercises.
* **Workout** — Stores workout sessions.
* **WorkoutExercise** — Connects exercises to workouts and records performance details such as repetitions, sets, and duration.

### Relationship

The database follows this relationship:

```text
Workout
   |
   | 1-to-many
   ↓
WorkoutExercise
   ↑
   | many-to-1
   |
Exercise
```

A workout can contain multiple exercises, and an exercise can be included in multiple workouts.

---

## Technologies Used

* Python 3.12
* Flask 2.2.2
* Flask-SQLAlchemy 3.0.3
* Flask-Migrate 3.1.0
* SQLAlchemy
* SQLite
* Marshmallow
* Pytest
* Pipenv

---

## Project Structure

```text
workout-api/
│
├── Pipfile
├── Pipfile.lock
├── README.md
│
└── server/
    ├── app.py
    ├── models.py
    ├── seed.py
    │
    ├── instance/
    │   └── app.db
    │
    ├── migrations/
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   └── script.py.mako
    │
    └── tests/
        ├── __init__.py
        ├── conftest.py
        ├── test_exercises.py
        ├── test_workouts.py
        └── test_workout_exercises.py
```

---

# Installation and Setup

## 1. Clone the repository

```bash
git clone https://github.com/OMONDICALMAX/workout-api.git
cd workout-api
```

## 2. Install dependencies

The project uses Pipenv.

```bash
pipenv install
```

Install development dependencies:

```bash
pipenv install --dev
```

## 3. Activate the virtual environment

```bash
pipenv shell
```

Alternatively, commands can be executed using:

```bash
pipenv run <command>
```

---

# Database Setup

Navigate to the server directory:

```bash
cd server
```

Create the database tables:

```bash
pipenv run flask --app app db upgrade
```

If the database has not yet been created, the application can also create the tables through the Flask application configuration.

---

# Seed the Database

The project includes a seed script containing sample exercises, workouts, and workout-exercise records.

Run:

```bash
pipenv run python seed.py
```

A successful seed operation should display:

```text
Database seeded successfully!
Exercises: 5
Workouts: 3
Workout exercises: 5
```

---

# Running the Application

From the `server` directory:

```bash
pipenv run flask --app app run --port 5555
```

The API will be available at:

```text
http://127.0.0.1:5555
```

Test the application:

```bash
curl http://127.0.0.1:5555/
```

Expected response:

```json
{
  "message": "Workout Tracking API",
  "status": "running"
}
```

---

# API Endpoints

## Exercises

### Get all exercises

```http
GET /exercises
```

Example:

```bash
curl http://127.0.0.1:5555/exercises
```

### Get one exercise

```http
GET /exercises/<id>
```

Example:

```bash
curl http://127.0.0.1:5555/exercises/1
```

### Create an exercise

```http
POST /exercises
```

Example:

```bash
curl -X POST http://127.0.0.1:5555/exercises \
-H "Content-Type: application/json" \
-d '{"name":"Lunges","category":"Strength","equipment_needed":false}'
```

### Update an exercise

```http
PATCH /exercises/<id>
```

Example:

```bash
curl -X PATCH http://127.0.0.1:5555/exercises/1 \
-H "Content-Type: application/json" \
-d '{"name":"Modified Push Ups"}'
```

### Delete an exercise

```http
DELETE /exercises/<id>
```

Example:

```bash
curl -X DELETE http://127.0.0.1:5555/exercises/6
```

---

# Workouts

### Get all workouts

```http
GET /workouts
```

Example:

```bash
curl http://127.0.0.1:5555/workouts
```

### Get one workout

```http
GET /workouts/<id>
```

Example:

```bash
curl http://127.0.0.1:5555/workouts/1
```

### Create a workout

```http
POST /workouts
```

Example:

```bash
curl -X POST http://127.0.0.1:5555/workouts \
-H "Content-Type: application/json" \
-d '{"date":"2026-08-30","duration_minutes":40,"notes":"Evening workout"}'
```

### Update a workout

```http
PATCH /workouts/<id>
```

Example:

```bash
curl -X PATCH http://127.0.0.1:5555/workouts/1 \
-H "Content-Type: application/json" \
-d '{"duration_minutes":50}'
```

### Delete a workout

```http
DELETE /workouts/<id>
```

Example:

```bash
curl -X DELETE http://127.0.0.1:5555/workouts/1
```

---

# Workout Exercises

Workout exercises represent the exercises performed as part of a particular workout.

They contain:

* Workout ID
* Exercise ID
* Repetitions
* Sets
* Duration in seconds

### Get all workout exercises

```http
GET /workout-exercises
```

Example:

```bash
curl http://127.0.0.1:5555/workout-exercises
```

### Get one workout exercise

```http
GET /workout-exercises/<id>
```

Example:

```bash
curl http://127.0.0.1:5555/workout-exercises/1
```

### Create a workout exercise

```http
POST /workout-exercises
```

Example:

```bash
curl -X POST http://127.0.0.1:5555/workout-exercises \
-H "Content-Type: application/json" \
-d '{"workout_id":3,"exercise_id":1,"reps":15,"sets":3,"duration_seconds":60}'
```

### Update a workout exercise

```http
PATCH /workout-exercises/<id>
```

Example:

```bash
curl -X PATCH http://127.0.0.1:5555/workout-exercises/1 \
-H "Content-Type: application/json" \
-d '{"reps":20,"sets":4}'
```

### Delete a workout exercise

```http
DELETE /workout-exercises/<id>
```

Example:

```bash
curl -X DELETE http://127.0.0.1:5555/workout-exercises/1
```

---

# Database Models

## Exercise

The `Exercise` model stores information about individual exercises.

Fields:

| Field              | Description                   |
| ------------------ | ----------------------------- |
| `id`               | Primary key                   |
| `name`             | Exercise name                 |
| `category`         | Exercise category             |
| `equipment_needed` | Whether equipment is required |

Example:

```json
{
  "id": 1,
  "name": "Push Ups",
  "category": "Strength",
  "equipment_needed": false
}
```

---

## Workout

The `Workout` model stores individual workout sessions.

Fields:

| Field              | Description                    |
| ------------------ | ------------------------------ |
| `id`               | Primary key                    |
| `date`             | Date of the workout            |
| `duration_minutes` | Workout duration               |
| `notes`            | Additional workout information |

Example:

```json
{
  "id": 1,
  "date": "2026-08-28",
  "duration_minutes": 45,
  "notes": "Upper body strength workout"
}
```

---

## WorkoutExercise

The `WorkoutExercise` model connects workouts and exercises.

Fields:

| Field              | Description                  |
| ------------------ | ---------------------------- |
| `id`               | Primary key                  |
| `workout_id`       | Foreign key to Workout       |
| `exercise_id`      | Foreign key to Exercise      |
| `reps`             | Number of repetitions        |
| `sets`             | Number of sets               |
| `duration_seconds` | Duration for timed exercises |

Example:

```json
{
  "id": 1,
  "workout_id": 1,
  "exercise_id": 1,
  "reps": 15,
  "sets": 3,
  "duration_seconds": 60
}
```

---

# Validation

The API validates incoming data to prevent invalid records.

Examples include:

* Exercise name is required.
* Exercise category is required.
* Workout date is required.
* Workout duration must be valid.
* Referenced workout must exist.
* Referenced exercise must exist.
* Repetitions and sets must contain valid values.
* Workout exercises cannot create duplicate workout/exercise combinations.

Invalid requests return appropriate HTTP error responses.

---

# Testing

The project uses **Pytest** for automated testing.

Run the complete test suite from the project root:

```bash
pipenv run pytest -v
```

The current test suite contains **37 tests** covering:

* Exercise CRUD operations
* Workout CRUD operations
* WorkoutExercise CRUD operations
* Validation
* Missing resources
* Invalid data
* Duplicate workout exercises

Current test result:

```text
37 passed
```

---

# Sample Seed Data

The database is seeded with five exercises:

| ID | Exercise      | Category | Equipment |
| -: | ------------- | -------- | --------- |
|  1 | Push Ups      | Strength | No        |
|  2 | Squats        | Strength | No        |
|  3 | Running       | Cardio   | No        |
|  4 | Bench Press   | Strength | Yes       |
|  5 | Jumping Jacks | Cardio   | No        |

Three sample workouts are included:

| ID | Date       | Duration | Notes                       |
| -: | ---------- | -------: | --------------------------- |
|  1 | 2026-08-28 |   45 min | Upper body strength workout |
|  2 | 2026-08-29 |   30 min | Cardio and conditioning     |
|  3 | 2026-08-30 |   60 min | Full body workout           |

---

# API Testing with cURL

Example commands:

```bash
# Check API
curl http://127.0.0.1:5555/

# Get exercises
curl http://127.0.0.1:5555/exercises

# Get workouts
curl http://127.0.0.1:5555/workouts

# Get workout exercises
curl http://127.0.0.1:5555/workout-exercises
```

---

# Database Migrations

Flask-Migrate is used to manage database schema changes.

Create a migration:

```bash
pipenv run flask --app app db migrate -m "Describe migration"
```

Apply migrations:

```bash
pipenv run flask --app app db upgrade
```

---

# Development

For development and debugging, activate the Pipenv environment:

```bash
cd ~/workout-api
pipenv shell
cd server
```

Run the application:

```bash
flask --app app run --port 5555
```

Run tests:

```bash
pipenv run pytest -v
```

---

# Author

**Calmax Omondi**

---

# License

This project is intended for educational purposes.

