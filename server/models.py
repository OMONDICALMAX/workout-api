from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint


db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)

    # Database constraints
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    # Relationships
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    workouts = db.relationship(
        "Workout",
        secondary="workout_exercises",
        back_populates="exercises",
        viewonly=True
    )

    # Model validations
    @validates("name")
    def validate_name(self, key, name):
        if not name or not name.strip():
            raise ValueError("Exercise name cannot be empty")
        return name.strip()

    @validates("category")
    def validate_category(self, key, category):
        if not category or not category.strip():
            raise ValueError("Exercise category cannot be empty")
        return category.strip()

    def __repr__(self):
        return f"<Exercise {self.name}>"


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    # Table constraint
    __table_args__ = (
        CheckConstraint(
            "duration_minutes > 0",
            name="check_duration_minutes_positive"
        ),
    )

    # Relationships
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercises",
        back_populates="workouts",
        viewonly=True
    )

    # Model validation
    @validates("duration_minutes")
    def validate_duration(self, key, duration):
        if duration is None or duration <= 0:
            raise ValueError("Workout duration must be greater than 0")
        return duration

    def __repr__(self):
        return f"<Workout {self.id}>"


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    reps = db.Column(db.Integer, nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True)

    # Table constraints
    __table_args__ = (
        CheckConstraint(
            "reps IS NULL OR reps > 0",
            name="check_reps_positive"
        ),
        CheckConstraint(
            "sets IS NULL OR sets > 0",
            name="check_sets_positive"
        ),
        CheckConstraint(
            "duration_seconds IS NULL OR duration_seconds > 0",
            name="check_duration_seconds_positive"
        ),
        db.UniqueConstraint(
            "workout_id",
            "exercise_id",
            name="unique_workout_exercise"
        ),
    )

    # Relationships
    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )

    # Model validations
    @validates("reps")
    def validate_reps(self, key, reps):
        if reps is not None and reps <= 0:
            raise ValueError("Reps must be greater than 0")
        return reps

    @validates("sets")
    def validate_sets(self, key, sets):
        if sets is not None and sets <= 0:
            raise ValueError("Sets must be greater than 0")
        return sets

    @validates("duration_seconds")
    def validate_duration_seconds(self, key, duration_seconds):
        if duration_seconds is not None and duration_seconds <= 0:
            raise ValueError("Duration must be greater than 0")
        return duration_seconds

    def __repr__(self):
        return (
            f"<WorkoutExercise "
            f"workout={self.workout_id} "
            f"exercise={self.exercise_id}>"
        )