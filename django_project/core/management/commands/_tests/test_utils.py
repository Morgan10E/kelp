import pytest
import core.management.commands._utils as command_utils

class TestGetUserAgrees:
    def test_user_agrees_lowercase(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "y")
        assert command_utils.get_user_agrees()

    def test_user_agrees_uppercase(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "Y")
        assert command_utils.get_user_agrees()

    def test_user_disagrees(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "n")
        assert command_utils.get_user_agrees() == False

    def test_defaults_to_no(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "")
        assert command_utils.get_user_agrees() == False

    def test_defaults_to_yes(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "")
        assert command_utils.get_user_agrees(default="y")

    def test_uses_default_if_invalid_values_entered(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "invalid")
        assert command_utils.get_user_agrees() == False
