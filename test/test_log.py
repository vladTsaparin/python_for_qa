# -*- coding: utf-8 -*-

def test_login(app):
    app.session.login_by_cred(user_email="vlad.caparin51@gmail.com", user_pass="QAtl00584")
