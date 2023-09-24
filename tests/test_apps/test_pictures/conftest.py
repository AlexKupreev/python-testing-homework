"""Fixtures for pictures."""
import pytest
from server.apps.pictures.container import container
from server.apps.pictures.logic.usecases import pictures_fetch


@pytest.fixture(scope='function')
def fetch_pictures():
    """Fixture for fetching pictures from real API."""
    return container.instantiate(pictures_fetch.PicturesFetch)

@pytest.fixture(scope='function')
def mock_fetch_pictures(fetch_pictures, monkeypatch):
    """Fixture for fetching pictures from emulated API."""
    monkeypatch.setattr(
        fetch_pictures._settings,
        'PLACEHOLDER_API_URL',
        'http://localhost:4242')

    # fetch_pictures._settings.PLACEHOLDER_API_URL = "http://localhost:4242"
    return container.instantiate(pictures_fetch.PicturesFetch)
