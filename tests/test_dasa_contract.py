"""Generated Dasa request contracts; run with python -m unittest discover -s tests."""
import importlib.util
import inspect
from pathlib import Path
import unittest
from unittest.mock import Mock, patch


def load_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROOT = Path(__file__).resolve().parents[1] / 'vedastro'
api = load_file('generated_calculate', ROOT / 'calculate.py')
types = load_file('sdk_types', ROOT / 'vedastro.py')


class DasaContractTests(unittest.TestCase):
    def test_sdk_owns_service_address(self):
        self.assertNotIn('base_url', vars(api.Calculate))
        api.Calculate.base_url = 'https://example.invalid'
        response = Mock()
        response.json.return_value = {'Status': 'Pass', 'Payload': {'result': True}}
        try:
            with patch.object(api.requests, 'post', return_value=response) as post:
                api.Calculate._make_request('GetAvailableSourceTexts', {})
            self.assertEqual(post.call_args.args[0], 'https://vedastro.zaishi.net/api/Calculate/GetAvailableSourceTexts')
        finally:
            del api.Calculate.base_url

    def test_life_serializes_birth_system_and_depth(self):
        birth = types.Time('14:20 16/10/1918 +05:30', types.GeoLocation('Bangalore', 77.5833, 12.9667))
        response = Mock()
        response.json.return_value = {'Status': 'Pass', 'Payload': {'DasaForLife': {'Periods': []}}}
        with patch.object(api.requests, 'post', return_value=response) as post:
            result = api.Calculate.DasaForLife(birth, 'VimshottariJanma', depth=2)

        body = post.call_args.kwargs['json']
        self.assertEqual(body['birthTime'], birth.to_json())
        self.assertEqual(body['system'], 'VimshottariJanma')
        self.assertEqual(body['depth'], 2)
        self.assertNotIn('levels', body)
        self.assertNotIn('precisionHours', body)
        self.assertEqual(result, {'Periods': []})

    def test_default_system_and_removed_methods(self):
        for method in ('DasaAtTime', 'DasaForLife'):
            signature = inspect.signature(getattr(api.Calculate, method))
            self.assertEqual(signature.parameters['system'].default, 'Vimshottari')

        for name in ('DasaForNow', 'DasaAtTimes', 'DasaAtRange', 'DasaApplicability',
                     'DasaPeriodBoundaries', 'SpecialDasaAtTime'):
            self.assertFalse(hasattr(api.Calculate, name), name)


if __name__ == '__main__':
    unittest.main()
