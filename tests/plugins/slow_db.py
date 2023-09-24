"""This plugin adds timeout to all tests decorated with `@pytest.mark.django_db()`.

 That's necessary because local DB is a bit slow.
 """
import pytest

DB_TIMEOUT = 8 # seconds


def pytest_collection_modifyitems(
    items: list[pytest.Item],
) -> None:
    for item in items:
        db_marker = item.get_closest_marker(name='django_db')
        if db_marker:
            item.add_marker(pytest.mark.timeout(DB_TIMEOUT))
