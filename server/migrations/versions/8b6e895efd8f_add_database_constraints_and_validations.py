"""Add database constraints and validations

Revision ID: 8b6e895efd8f
Revises: 06b276aff2a0
Create Date: 2026-08-30 15:31:34.424775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b6e895efd8f'
down_revision = '06b276aff2a0'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("workouts") as batch_op:
        batch_op.create_check_constraint(
            "check_duration_minutes_positive",
            "duration_minutes > 0"
        )

    with op.batch_alter_table("workout_exercises") as batch_op:
        batch_op.create_check_constraint(
            "check_reps_positive",
            "reps IS NULL OR reps > 0"
        )

        batch_op.create_check_constraint(
            "check_sets_positive",
            "sets IS NULL OR sets > 0"
        )

        batch_op.create_check_constraint(
            "check_duration_seconds_positive",
            "duration_seconds IS NULL OR duration_seconds > 0"
        )


def downgrade():
    with op.batch_alter_table("workout_exercises") as batch_op:
        batch_op.drop_constraint(
            "check_duration_seconds_positive",
            type_="check"
        )

        batch_op.drop_constraint(
            "check_sets_positive",
            type_="check"
        )

        batch_op.drop_constraint(
            "check_reps_positive",
            type_="check"
        )

    with op.batch_alter_table("workouts") as batch_op:
        batch_op.drop_constraint(
            "check_duration_minutes_positive",
            type_="check"
        )
