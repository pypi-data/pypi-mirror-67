"""Pytest configuration."""

from unittest import mock

import pytest

from eaf.app
from eaf.state import State

import xoinvader.app


@pytest.fixture
def mock_application(request):

    app = None

    def inner():
        nonlocal app

        app = MockedApplication()
        return app

    request.addfinalizer(MockedApplication._finalize)
    return inner


@pytest.fixture
def mock_state(request, mock_application):

    app = None

    def inner(mock_app=False):
        nonlocal app

        if mock_app:
            # We need to create reference or object will be collected by gc
            app = mock_application()
        else:
            app = xoinvader.app.current()

        app.register(MockedState)
        return app.state

    def stop():
        app.deregister(MockedState.__name__)

    request.addfinalizer(stop)

    return inner


class MockedApplication(xoinvader.app.XOInvader):

    @staticmethod
    def _finalize():
        try:
            app = xoinvader.app.current()
            app.stop()
            del app
        except:
            pass


class MockedState(State):
    pass
