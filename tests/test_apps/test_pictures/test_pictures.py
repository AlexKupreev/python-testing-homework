"""Test pictures operations."""
import pytest

from server.apps.pictures.infrastructure.services import placeholder


@pytest.mark.timeout(10)
@pytest.mark.flaky(retries=3, delay=1)
def test_pictures_fetch(fetch_pictures) -> None:
    """Test base picture fetching functionality."""
    pictures = fetch_pictures(limit=3)

    assert len(pictures) == 3
    assert all(
        isinstance(pic, placeholder.PictureResponse) for pic in pictures
    )


def test_pictures_fetch_from_mock(mock_fetch_pictures) -> None:
    """Test base picture fetching functionality."""
    pictures = mock_fetch_pictures(limit=2)

    assert len(pictures) == 2
    assert all(
        isinstance(pic, placeholder.PictureResponse) for pic in pictures
    )
