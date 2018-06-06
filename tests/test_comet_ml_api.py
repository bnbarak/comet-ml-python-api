import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../comet_ml_api')))

from unittest import TestCase
import comet_ml_api
import helpers

version = "v1"

class TestGetUrl(TestCase):
    def test_is_string(self):
        comet = comet_ml_api.CometMlApi("test", version)
        expected_url = comet.get_url()
        url = helpers.URLS[version]
        self.assertEqual(expected_url, url)

class TestGetVersion(TestCase):
    def test_is_not_none(self):
        not_default_version = "v2"
        comet = comet_ml_api.CometMlApi("test", not_default_version)
        expected_version = comet.get_version()
        self.assertEqual(expected_version, not_default_version)

    def test_is_none(self):
        comet = comet_ml_api.CometMlApi("test")
        expected_version = comet.get_version()
        self.assertEqual(expected_version, version)
