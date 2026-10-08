import os
import tempfile

os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "test.db")

from app import app

client = app.test_client()


def test_post_and_list():
    r = client.post(
        "/", data={"course": "dd2482", "rating": "5", "body": "<script>x</script>"}
    )
    assert r.status_code == 303
    page = client.get("/").text
    assert "DD2482" in page and "&lt;script&gt;" in page and "<script>x" not in page


def test_rejects_bad_input():
    for data in [
        {"course": "nope", "rating": "5", "body": "hi"},
        {"course": "DD2482", "rating": "6", "body": "hi"},
        {"course": "DD2482", "rating": "", "body": "hi"},
        {"course": "DD2482", "rating": "3", "body": ""},
        {"course": "DD2482", "rating": "3", "body": "x" * 2001},
    ]:
        assert client.post("/", data=data).status_code == 400


def test_health():
    assert client.get("/health").text == "ok"
