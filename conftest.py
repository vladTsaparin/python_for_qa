from fixture.application import Application
import pytest

from model.user import User

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login_by_cred(User(email="vlad.caparin51@gmail.com", password="dAcsNbONVQwAQkz"))
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login_by_cred(User(email="vlad.caparin51@gmail.com", password="dAcsNbONVQwAQkz"))
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
