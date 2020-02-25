from db.data_models import Post, Room, House
from db.data_access import nuke_db, initialize_orm, create_post, create_house
import pytest
import datetime


@pytest.fixture
def test_db():
    test_db = initialize_orm("sqlite:///test-openparlour-db.sqlite")
    yield test_db
    nuke_db("sqlite:///test-openparlour-db.sqlite")


def test_post_to_dict():
    r = Room(id=1, name="Den")
    p = Post(id=1, room=1, date=datetime.datetime(2020,2,1), title="Test Post",
             body="This is a test of the emergency post system.")

    assert r.to_dict() == {'id': 1, 'name': "Den"}
    assert p.to_dict() == {'id':1, 'room': 1,'date': datetime.datetime(2020,2,1), 'title': "Test Post",
                            'body': "This is a test of the emergency post system."}


def test_room_to_dict():
    r = Room(id=1, name="Crematorium")
    assert r.to_dict() == {'id': 1, 'name': "Crematorium"}


def test_house_to_dict():
    h = House(id=1,address="http://nyi.nyi")
    assert h.to_dict() == {'id': 1, 'address': "http://nyi.nyi"}


def test_create_post(test_db):
    assert create_post(test_db, room=1, date="2020-12-01", title="Test Title", body="Test post body yeah yeah yeah!") == 1


def test_create_house(test_db):
    assert create_house(test_db, address="https://nyi.nyi") == 1
