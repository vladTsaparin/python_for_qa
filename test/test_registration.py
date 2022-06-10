# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_registration_valid(app):
    app.session.registration(User(email="vlad.caparin51+1@gmail.com", password="QAtl00584", first_name="first_name", last_name="last_name"))
