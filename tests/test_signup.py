from urllib.parse import quote


def test_signup_success(client):
    email = "testuser@example.com"
    path = f"/activities/{quote('Chess Club')}/signup"
    resp = client.post(path, params={"email": email})
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")

    # Verify the participant is present
    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_duplicate(client):
    email = "dup@example.com"
    path = f"/activities/{quote('Chess Club')}/signup"
    r1 = client.post(path, params={"email": email})
    assert r1.status_code == 200

    # Duplicate attempt
    r2 = client.post(path, params={"email": email})
    assert r2.status_code == 400
    assert "already signed up" in r2.json().get("detail", "").lower()
