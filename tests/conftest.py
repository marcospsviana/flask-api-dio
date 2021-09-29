import pytest
from api.app_rest import create_app


@pytest.fixture(scope="module")
def app():
    return create_app()
