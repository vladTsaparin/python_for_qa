def test_login_by_cred (app):
    app.session.login_by_cred(User(
        email="vlad.caparin51@gmail.com",
        password="dAcsNbONVQwAQkz",
    ))

