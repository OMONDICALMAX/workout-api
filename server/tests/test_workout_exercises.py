def test_get_workout_exercises(client):
    response = client.get("/workout-exercises")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 1
    assert data[0]["reps"] == 12
    assert data[0]["sets"] == 3


def test_get_one_workout_exercise(client):
    response = client.get("/workout-exercises/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["workout_id"] == 1
    assert data["exercise_id"] == 1


def test_get_nonexistent_workout_exercise(client):
    response = client.get("/workout-exercises/999")

    assert response.status_code == 404
    assert response.get_json()["error"] == (
        "Workout exercise not found"
    )


def test_create_workout_exercise(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 1,
            "exercise_id": 2,
            "reps": 10,
            "sets": 3,
            "duration_seconds": 60
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["workout_id"] == 1
    assert data["exercise_id"] == 2
    assert data["reps"] == 10
    assert data["sets"] == 3


def test_create_workout_exercise_missing_workout(client):
    response = client.post(
        "/workout-exercises",
        json={
            "exercise_id": 2,
            "reps": 10,
            "sets": 3
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Workout ID is required"


def test_create_workout_exercise_invalid_workout(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 999,
            "exercise_id": 2,
            "reps": 10,
            "sets": 3
        }
    )

    assert response.status_code == 404


def test_create_workout_exercise_invalid_exercise(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 1,
            "exercise_id": 999,
            "reps": 10,
            "sets": 3
        }
    )

    assert response.status_code == 404


def test_create_workout_exercise_invalid_reps(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 1,
            "exercise_id": 2,
            "reps": 0,
            "sets": 3
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "Reps must be greater than 0"
    )


def test_create_workout_exercise_invalid_sets(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 1,
            "exercise_id": 2,
            "reps": 10,
            "sets": 0
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "Sets must be greater than 0"
    )


def test_create_workout_exercise_invalid_duration(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 1,
            "exercise_id": 2,
            "reps": 10,
            "sets": 3,
            "duration_seconds": 0
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "Duration must be greater than 0"
    )


def test_duplicate_workout_exercise(client):
    response = client.post(
        "/workout-exercises",
        json={
            "workout_id": 1,
            "exercise_id": 1,
            "reps": 20,
            "sets": 4
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "This exercise is already assigned to this workout"
    )


def test_update_workout_exercise(client):
    response = client.patch(
        "/workout-exercises/1",
        json={
            "reps": 20,
            "sets": 4
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["reps"] == 20
    assert data["sets"] == 4


def test_update_nonexistent_workout_exercise(client):
    response = client.patch(
        "/workout-exercises/999",
        json={
            "reps": 20
        }
    )

    assert response.status_code == 404


def test_delete_workout_exercise(client):
    response = client.delete("/workout-exercises/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == (
        "Workout exercise deleted successfully"
    )


def test_delete_nonexistent_workout_exercise(client):
    response = client.delete("/workout-exercises/999")

    assert response.status_code == 404
