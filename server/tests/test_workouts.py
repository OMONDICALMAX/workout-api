def test_get_workouts(client):
    response = client.get("/workouts")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 1
    assert data[0]["duration_minutes"] == 45


def test_get_one_workout(client):
    response = client.get("/workouts/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["date"] == "2026-08-30"


def test_get_nonexistent_workout(client):
    response = client.get("/workouts/999")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Workout not found"


def test_create_workout(client):
    response = client.post(
        "/workouts",
        json={
            "date": "2026-08-31",
            "duration_minutes": 60,
            "notes": "New workout"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["date"] == "2026-08-31"
    assert data["duration_minutes"] == 60
    assert data["notes"] == "New workout"


def test_create_workout_missing_date(client):
    response = client.post(
        "/workouts",
        json={
            "duration_minutes": 45
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Workout date is required"


def test_create_workout_missing_duration(client):
    response = client.post(
        "/workouts",
        json={
            "date": "2026-08-30"
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Duration is required"


def test_create_workout_invalid_duration(client):
    response = client.post(
        "/workouts",
        json={
            "date": "2026-08-30",
            "duration_minutes": 0
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "Workout duration must be greater than 0"
    )


def test_create_workout_invalid_date(client):
    response = client.post(
        "/workouts",
        json={
            "date": "not-a-date",
            "duration_minutes": 45
        }
    )

    assert response.status_code == 400


def test_update_workout(client):
    response = client.patch(
        "/workouts/1",
        json={
            "duration_minutes": 60,
            "notes": "Updated workout"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["duration_minutes"] == 60
    assert data["notes"] == "Updated workout"


def test_update_nonexistent_workout(client):
    response = client.patch(
        "/workouts/999",
        json={
            "duration_minutes": 60
        }
    )

    assert response.status_code == 404


def test_delete_workout(client):
    response = client.delete("/workouts/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Workout deleted successfully"


def test_delete_nonexistent_workout(client):
    response = client.delete("/workouts/999")

    assert response.status_code == 404
