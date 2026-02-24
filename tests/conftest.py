import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_data


# Keep an original snapshot of the in-memory activities to restore between tests
_ORIG_ACTIVITIES = copy.deepcopy(activities_data)


@pytest.fixture(autouse=True)
def reset_activities():
    # Reset activities before each test to ensure isolation
    activities_data.clear()
    activities_data.update(copy.deepcopy(_ORIG_ACTIVITIES))
    yield
    # Ensure clean state after test as well
    activities_data.clear()
    activities_data.update(copy.deepcopy(_ORIG_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
