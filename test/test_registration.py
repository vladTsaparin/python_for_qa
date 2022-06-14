# -*- coding: utf-8 -*-
from model.user import User
from datetime import datetime


def test_registration_new_user(app):
    app.session.registration(User(
        email=f"for.qa14+{datetime.now().microsecond}@gmail.com",
        password="QAtl00584",
        first_name="перший",
        last_name="другий"
    ))


def test_registration_with_existing_email(app):
    app.session.registration(User(
        email=f"for.qa14@gmail.com",
        password="QAtl00584",
        first_name="перший",
        last_name="другий"
    ))
