from urllib.parse import quote


def test_remove_success(client):
    email = "remove_me@example.com"
    signup_path = f"/activities/{quote('Chess Club')}/signup"
    del_path = f"/activities/{quote('Chess Club')}/participants"

    # Ensure the participant is signed up
    r = client.post(signup_path, params={"email": email})
    assert r.status_code == 200

    # Now remove
    dr = client.delete(del_path, params={"email": email})
    assert dr.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_remove_nonexistent(client):
    email = "noone@example.com"
    del_path = f"/activities/{quote('Chess Club')}/participants"
    dr = client.delete(del_path, params={"email": email})
    assert dr.status_code == 404
