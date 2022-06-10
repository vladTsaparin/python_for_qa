# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.session.login_by_cred(user_email="vlad.caparin51@gmail.com", user_pass="QAtl00584")
