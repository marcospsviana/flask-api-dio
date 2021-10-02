import pytest
import sys


from api.models import Users
import os


from api.app_rest import create_app


@pytest.fixture(scope="module")
def app():
    
    return create_app()


@pytest.fixture
def db():
    user = Users(id=1, username="devpro", password="devnull")
    return user

