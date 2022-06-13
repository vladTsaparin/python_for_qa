# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.user import User
from datetime import datetime



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_registration_valid(app):
    app.session.registration(User(email=f"for.qa14+{datetime.now().microsecond}@gmail.com", password="QAtl00584", first_name="first_name", last_name="last_name"))
