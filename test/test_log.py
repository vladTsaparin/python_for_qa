# -*- coding: utf-8 -*-
from model.user import User


def test_login(app):
    app.session.login_by_cred(User(email="for.qa14+rozetka@gmail.com", password="1Qaz2wsx0"))
