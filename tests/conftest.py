"""tests config"""

import pytest

from my_project import create_app


@pytest.fixture
def client():
    """
    Test client fixture
    """
    test_app = create_app()
    with test_app.test_client() as client:
        yield client
