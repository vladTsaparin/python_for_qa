from fixture.application import Application
import pytest

from model.user import User


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login_by_cred(User(email="for.qa14+rozetka@gmail.com", password="1Qaz2wsx0"))
    request.addfinalizer(fixture.destroy)
    return fixture
