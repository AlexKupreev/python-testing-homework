"""Test pictures operations."""
import pytest

from server.apps.pictures.container import container
from server.apps.pictures.infrastructure.services import placeholder
from server.apps.pictures.logic.usecases import pictures_fetch


@pytest.mark.timeout(10)
def test_pictures_fetch(fetch_pictures) -> None:
    """Test base picture fetching functionality"""

    pictures = fetch_pictures(limit=3)

    assert len(pictures) == 3
    assert all([isinstance(x, placeholder.PictureResponse) for x in pictures])


def test_pictures_fetch_from_mock(mock_fetch_pictures) -> None:
    """Test base picture fetching functionality"""

    pictures = mock_fetch_pictures(limit=2)

    assert len(pictures) == 2
    assert all([isinstance(x, placeholder.PictureResponse) for x in pictures])

