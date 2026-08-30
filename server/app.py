

from flask import Flask, jsonify, request
from flask_migrate import Migrate

from models import db, Exercise, Workout, WorkoutExercise


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return {
        "message": "Workout Tracking API",
        "status": "running"
    }


# GET all exercises
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": exercise.id,
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        }
        for exercise in exercises
    ])


# GET one exercise
@app.route("/exercises/<int:exercise_id>", methods=["GET"])
def get_exercise(exercise_id):
    exercise = db.session.get(Exercise, exercise_id)

    if exercise is None:
        return jsonify({
            "error": "Exercise not found"
        }), 404

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed
    })


# POST create a new exercise
@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    name = data.get("name")
    category = data.get("category")
    equipment_needed = data.get("equipment_needed", False)

    if not name:
        return jsonify({
            "error": "Exercise name is required"
        }), 400

    if not category:
        return jsonify({
            "error": "Exercise category is required"
        }), 400

    try:
        exercise = Exercise(
            name=name,
            category=category,
            equipment_needed=equipment_needed
        )

        db.session.add(exercise)
        db.session.commit()

        return jsonify({
            "id": exercise.id,
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        }), 201

    except ValueError as error:
        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 400

# PATCH update an existing exercise
@app.route("/exercises/<int:exercise_id>", methods=["PATCH"])
def update_exercise(exercise_id):
    exercise = db.session.get(Exercise, exercise_id)

    if exercise is None:
        return jsonify({
            "error": "Exercise not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    try:
        if "name" in data:
            exercise.name = data["name"]

        if "category" in data:
            exercise.category = data["category"]

        if "equipment_needed" in data:
            exercise.equipment_needed = data["equipment_needed"]

        db.session.commit()

        return jsonify({
            "id": exercise.id,
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        })

    except ValueError as error:
        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 400

# DELETE an exercise
@app.route("/exercises/<int:exercise_id>", methods=["DELETE"])
def delete_exercise(exercise_id):
    exercise = db.session.get(Exercise, exercise_id)

    if exercise is None:
        return jsonify({
            "error": "Exercise not found"
        }), 404

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise deleted successfully"
    })

# GET all workouts
@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return jsonify([
        {
            "id": workout.id,
            "date": workout.date.isoformat(),
            "duration_minutes": workout.duration_minutes,
            "notes": workout.notes
        }
        for workout in workouts
    ])


# GET one workout
@app.route("/workouts/<int:workout_id>", methods=["GET"])
def get_workout(workout_id):
    workout = db.session.get(Workout, workout_id)

    if workout is None:
        return jsonify({
            "error": "Workout not found"
        }), 404

    return jsonify({
        "id": workout.id,
        "date": workout.date.isoformat(),
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes
    })


# POST create a new workout
@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    workout_date = data.get("date")
    duration_minutes = data.get("duration_minutes")
    notes = data.get("notes")

    if not workout_date:
        return jsonify({
            "error": "Workout date is required"
        }), 400

    if duration_minutes is None:
        return jsonify({
            "error": "Duration is required"
        }), 400

    try:
        from datetime import date

        workout = Workout(
            date=date.fromisoformat(workout_date),
            duration_minutes=duration_minutes,
            notes=notes
        )

        db.session.add(workout)
        db.session.commit()

        return jsonify({
            "id": workout.id,
            "date": workout.date.isoformat(),
            "duration_minutes": workout.duration_minutes,
            "notes": workout.notes
        }), 201

    except ValueError as error:
        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 400


# PATCH update an existing workout
@app.route("/workouts/<int:workout_id>", methods=["PATCH"])
def update_workout(workout_id):
    workout = db.session.get(Workout, workout_id)

    if workout is None:
        return jsonify({
            "error": "Workout not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    try:
        from datetime import date

        if "date" in data:
            workout.date = date.fromisoformat(data["date"])

        if "duration_minutes" in data:
            workout.duration_minutes = data["duration_minutes"]

        if "notes" in data:
            workout.notes = data["notes"]

        db.session.commit()

        return jsonify({
            "id": workout.id,
            "date": workout.date.isoformat(),
            "duration_minutes": workout.duration_minutes,
            "notes": workout.notes
        })

    except ValueError as error:
        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 400


# DELETE a workout
@app.route("/workouts/<int:workout_id>", methods=["DELETE"])
def delete_workout(workout_id):
    workout = db.session.get(Workout, workout_id)

    if workout is None:
        return jsonify({
            "error": "Workout not found"
        }), 404

    db.session.delete(workout)
    db.session.commit()

    return jsonify({
        "message": "Workout deleted successfully"
    })

# GET all workout exercises
@app.route("/workout-exercises", methods=["GET"])
def get_workout_exercises():
    workout_exercises = WorkoutExercise.query.all()

    return jsonify([
        {
            "id": workout_exercise.id,
            "workout_id": workout_exercise.workout_id,
            "exercise_id": workout_exercise.exercise_id,
            "reps": workout_exercise.reps,
            "sets": workout_exercise.sets,
            "duration_seconds": workout_exercise.duration_seconds
        }
        for workout_exercise in workout_exercises
    ])

# GET one workout exercise
@app.route("/workout-exercises/<int:workout_exercise_id>", methods=["GET"])
def get_workout_exercise(workout_exercise_id):
    workout_exercise = db.session.get(
        WorkoutExercise,
        workout_exercise_id
    )

    if workout_exercise is None:
        return jsonify({
            "error": "Workout exercise not found"
        }), 404

    return jsonify({
        "id": workout_exercise.id,
        "workout_id": workout_exercise.workout_id,
        "exercise_id": workout_exercise.exercise_id,
        "reps": workout_exercise.reps,
        "sets": workout_exercise.sets,
        "duration_seconds": workout_exercise.duration_seconds
    })

# POST add an exercise to a workout
@app.route("/workout-exercises", methods=["POST"])
def create_workout_exercise():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    workout_id = data.get("workout_id")
    exercise_id = data.get("exercise_id")

    if not workout_id:
        return jsonify({
            "error": "Workout ID is required"
        }), 400

    if not exercise_id:
        return jsonify({
            "error": "Exercise ID is required"
        }), 400

    workout = db.session.get(Workout, workout_id)

    if workout is None:
        return jsonify({
            "error": "Workout not found"
        }), 404

    exercise = db.session.get(Exercise, exercise_id)

    if exercise is None:
        return jsonify({
            "error": "Exercise not found"
        }), 404

    existing_workout_exercise = WorkoutExercise.query.filter_by(
        workout_id=workout_id,
        exercise_id=exercise_id
    ).first()

    if existing_workout_exercise:
        return jsonify({
            "error": "This exercise is already assigned to this workout"
        }), 400

    try:
        workout_exercise = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds")
        )

        db.session.add(workout_exercise)
        db.session.commit()

        return jsonify({
            "id": workout_exercise.id,
            "workout_id": workout_exercise.workout_id,
            "exercise_id": workout_exercise.exercise_id,
            "reps": workout_exercise.reps,
            "sets": workout_exercise.sets,
            "duration_seconds": workout_exercise.duration_seconds
        }), 201

    except ValueError as error:
        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 400

# PATCH update a workout exercise
@app.route("/workout-exercises/<int:workout_exercise_id>", methods=["PATCH"])
def update_workout_exercise(workout_exercise_id):
    workout_exercise = db.session.get(
        WorkoutExercise,
        workout_exercise_id
    )

    if workout_exercise is None:
        return jsonify({
            "error": "Workout exercise not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    try:
        # Update workout_id
        if "workout_id" in data:
            workout = db.session.get(Workout, data["workout_id"])

            if workout is None:
                return jsonify({
                    "error": "Workout not found"
                }), 404

            workout_exercise.workout_id = data["workout_id"]

        # Update exercise_id
        if "exercise_id" in data:
            exercise = db.session.get(Exercise, data["exercise_id"])

            if exercise is None:
                return jsonify({
                    "error": "Exercise not found"
                }), 404

            workout_exercise.exercise_id = data["exercise_id"]

        # Update reps
        if "reps" in data:
            workout_exercise.reps = data["reps"]

        # Update sets
        if "sets" in data:
            workout_exercise.sets = data["sets"]

        # Update duration_seconds
        if "duration_seconds" in data:
            workout_exercise.duration_seconds = data["duration_seconds"]

        db.session.commit()

        return jsonify({
            "id": workout_exercise.id,
            "workout_id": workout_exercise.workout_id,
            "exercise_id": workout_exercise.exercise_id,
            "reps": workout_exercise.reps,
            "sets": workout_exercise.sets,
            "duration_seconds": workout_exercise.duration_seconds
        })

    except ValueError as error:
        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 400

# DELETE a workout exercise
@app.route("/workout-exercises/<int:workout_exercise_id>", methods=["DELETE"])
def delete_workout_exercise(workout_exercise_id):
    workout_exercise = db.session.get(
        WorkoutExercise,
        workout_exercise_id
    )

    if workout_exercise is None:
        return jsonify({
            "error": "Workout exercise not found"
        }), 404

    db.session.delete(workout_exercise)
    db.session.commit()

    return jsonify({
        "message": "Workout exercise deleted successfully"
    })

if __name__ == "__main__":
    app.run(port=5555, debug=True)
