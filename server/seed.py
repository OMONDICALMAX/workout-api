
from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise


from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():

    # Create database tables if they don't exist
    db.create_all()

    # Clear existing data
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # -------------------------
    # Exercises
    # -------------------------

    push_ups = Exercise(
        name="Push Ups",
        category="Strength",
        equipment_needed=False
    )

    squats = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    running = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=False
    )

    bench_press = Exercise(
        name="Bench Press",
        category="Strength",
        equipment_needed=True
    )

    jumping_jacks = Exercise(
        name="Jumping Jacks",
        category="Cardio",
        equipment_needed=False
    )

    db.session.add_all([
        push_ups,
        squats,
        running,
        bench_press,
        jumping_jacks
    ])

    db.session.commit()

    # -------------------------
    # Workouts
    # -------------------------

    workout1 = Workout(
        date=date(2026, 8, 28),
        duration_minutes=45,
        notes="Upper body strength workout"
    )

    workout2 = Workout(
        date=date(2026, 8, 29),
        duration_minutes=30,
        notes="Cardio and conditioning"
    )

    workout3 = Workout(
        date=date(2026, 8, 30),
        duration_minutes=60,
        notes="Full body workout"
    )

    db.session.add_all([
        workout1,
        workout2,
        workout3
    ])

    db.session.commit()

    # -------------------------
    # Workout Exercises
    # -------------------------

    workout_exercise1 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=push_ups.id,
        reps=15,
        sets=3,
        duration_seconds=60
    )

    workout_exercise2 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=bench_press.id,
        reps=10,
        sets=3,
        duration_seconds=90
    )

    workout_exercise3 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=running.id,
        reps=None,
        sets=None,
        duration_seconds=1200
    )

    workout_exercise4 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=jumping_jacks.id,
        reps=30,
        sets=3,
        duration_seconds=60
    )

    workout_exercise5 = WorkoutExercise(
        workout_id=workout3.id,
        exercise_id=squats.id,
        reps=15,
        sets=4,
        duration_seconds=60
    )

    db.session.add_all([
        workout_exercise1,
        workout_exercise2,
        workout_exercise3,
        workout_exercise4,
        workout_exercise5
    ])

    db.session.commit()

    print("Database seeded successfully!")
    print(f"Exercises: {Exercise.query.count()}")
    print(f"Workouts: {Workout.query.count()}")
    print(f"Workout exercises: {WorkoutExercise.query.count()}")
