def test_get_exercises(client):
    response = client.get("/exercises")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 2
    assert data[0]["name"] == "Push Ups"


def test_get_one_exercise(client):
    response = client.get("/exercises/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["name"] == "Push Ups"


def test_get_nonexistent_exercise(client):
    response = client.get("/exercises/999")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Exercise not found"


def test_create_exercise(client):
    response = client.post(
        "/exercises",
        json={
            "name": "Bench Press",
            "category": "Strength",
            "equipment_needed": True
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Bench Press"
    assert data["category"] == "Strength"
    assert data["equipment_needed"] is True


def test_create_exercise_missing_name(client):
    response = client.post(
        "/exercises",
        json={
            "category": "Strength"
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Exercise name is required"


def test_create_exercise_missing_category(client):
    response = client.post(
        "/exercises",
        json={
            "name": "Bench Press"
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Exercise category is required"


def test_update_exercise(client):
    response = client.patch(
        "/exercises/1",
        json={
            "name": "Modified Push Ups"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["name"] == "Modified Push Ups"


def test_update_nonexistent_exercise(client):
    response = client.patch(
        "/exercises/999",
        json={
            "name": "Unknown"
        }
    )

    assert response.status_code == 404


def test_delete_exercise(client):
    response = client.delete("/exercises/2")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Exercise deleted successfully"


def test_delete_nonexistent_exercise(client):
    response = client.delete("/exercises/999")

    assert response.status_code == 404
