"""Test xoinvader.weapon module."""

import pytest

import xoinvader
from xoinvader import weapon


# pylint: disable=missing-docstring
@pytest.mark.skip
def test_weapon(monkeypatch):
    monkeypatch.setattr(weapon, "CONFIG", {})

    # pytest.raises(KeyError, lambda:
    weapon.Weapon(ammo=10, max_ammo=10, cooldown=0.5)
