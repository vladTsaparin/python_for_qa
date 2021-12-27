# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.open_login_page()
    app.login_by_cred(user_email="influencer_1634565141@netfanz.com", user_pass="influencer_1634565141")
