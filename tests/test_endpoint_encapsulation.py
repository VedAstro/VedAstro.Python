"""The SDK owns request routing; no live requests are made."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

spec = importlib.util.spec_from_file_location('sdk_calculate', Path(__file__).resolve().parents[1] / 'vedastro/calculate.py')
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


class EndpointEncapsulationTests(unittest.TestCase):
    def test_legacy_attribute_cannot_redirect_requests(self):
        self.assertNotIn('base_url', vars(api.Calculate))
        api.Calculate.base_url = 'https://example.invalid'
        response = Mock()
        response.json.return_value = {'Status': 'Pass', 'Payload': {'result': True}}
        try:
            with patch.object(api.requests, 'post', return_value=response) as post:
                self.assertTrue(api.Calculate._make_request('GetAvailableSourceTexts', {}))
            self.assertEqual(post.call_args.args[0], 'https://vedastro.zaishi.net/api/Calculate/GetAvailableSourceTexts')
        finally:
            del api.Calculate.base_url
