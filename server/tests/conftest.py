
import pytest

from app import app
from models import db, Exercise, Workout, WorkoutExercise


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.app_context():
        # Start with a completely clean database for every test
        db.drop_all()
        db.create_all()

        # Seed test exercises
        exercise1 = Exercise(
            name="Push Ups",
            category="Strength",
            equipment_needed=False
        )

        exercise2 = Exercise(
            name="Running",
            category="Cardio",
            equipment_needed=False
        )

        # Seed test workout
        from datetime import date

        workout = Workout(
            date=date(2026, 8, 30),
            duration_minutes=45,
            notes="Test workout"
        )

        db.session.add_all([
            exercise1,
            exercise2,
            workout
        ])

        db.session.commit()

        # Seed workout exercise
        workout_exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_id=exercise1.id,
            reps=12,
            sets=3,
            duration_seconds=60
        )

        db.session.add(workout_exercise)
        db.session.commit()

        yield app.test_client()

        # Clean up after every test
        db.session.remove()
        db.drop_all()
