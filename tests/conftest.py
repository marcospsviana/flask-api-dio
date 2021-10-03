import pytest
from passlib.context import CryptContext

from api.models import Users
from api.app_rest import create_app


@pytest.fixture(scope="session")
def app():

    return create_app()


@pytest.fixture(scope="session")
def db():
    myctx = CryptContext(schemes=["sha256_crypt"])
    password = myctx.hash("teste")
    user = Users(username="devtest", password=password)
    user.save()
    yield user
    user.delete()
