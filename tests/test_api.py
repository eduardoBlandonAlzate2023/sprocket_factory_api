from app.models.factory import Factory
from app.models.sprocket import Sprocket
import pytest
from app import db, app
import base64
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="module")
def test_client():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()

    testing_client = app.test_client()

    yield testing_client

    with app.app_context():
        db.drop_all()


def auth_header(
    username=os.getenv("ADMIN_USERNAME", "admin"),
    password=os.getenv("ADMIN_PASSWORD", "password"),
):
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode("utf-8")
    return {"Authorization": f"Basic {credentials}"}


def test_get_all_factories(test_client):
    with app.app_context():
        factory = Factory(chart_data={"some_key": "some_value"})
        db.session.add(factory)
        db.session.commit()

    response = test_client.get("/factories", headers=auth_header())
    assert response.status_code == 200
    assert b"some_key" in response.data


def test_get_factory_by_id(test_client):
    with app.app_context():
        factory = Factory(chart_data={"some_key": "specific_value"})
        db.session.add(factory)
        db.session.commit()
        factory_id = factory.id

    response = test_client.get(f"/factories/{factory_id}", headers=auth_header())
    assert response.status_code == 200
    assert b"specific_value" in response.data


def test_get_sprocket_by_id(test_client):
    with app.app_context():
        sprocket = Sprocket(
            teeth=12, pitch_diameter=3.5, outside_diameter=5.0, pitch=0.5
        )
        db.session.add(sprocket)
        db.session.commit()
        sprocket_id = sprocket.id

    response = test_client.get(f"/sprockets/{sprocket_id}", headers=auth_header())
    assert response.status_code == 200
    assert b"teeth" in response.data


def test_create_sprocket(test_client):
    sprocket_data = {
        "teeth": 15,
        "pitch_diameter": 4.0,
        "outside_diameter": 6.0,
        "pitch": 0.6,
    }

    response = test_client.post("/sprockets", json=sprocket_data, headers=auth_header())
    assert response.status_code == 201
    assert b"Sprocket created successfully" in response.data


def test_update_sprocket(test_client):
    with app.app_context():
        sprocket = Sprocket(
            teeth=10, pitch_diameter=3.0, outside_diameter=4.5, pitch=0.4
        )
        db.session.add(sprocket)
        db.session.commit()
        sprocket_id = sprocket.id

    updated_data = {"teeth": 16}

    response = test_client.put(
        f"/sprockets/{sprocket_id}", json=updated_data, headers=auth_header()
    )
    assert response.status_code == 200
    assert b"Sprocket updated successfully" in response.data
