from sample_app import sample


def test_index():
    client = sample.test_client()

    response = client.get("/")

    print(f"Status Code de /: {response.status_code}")

    assert response.status_code == 200