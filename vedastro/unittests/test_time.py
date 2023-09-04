import unittest
from vedastro.datetime_offset import DateTimeOffset
import VedAstro.Library as VedAstro
from vedastro.time import Time
from vedastro.geolocation import GeoLocation


class TestTime(unittest.TestCase):
    def setUp(self):
        self.geolocation = GeoLocation(location="Tokyo", latitude=35.6895, longitude=-139.6917)
        self.date = "07/05/2010"
        self.time = "06:42"
        self.time_offset = "+05:30"

    def test_init(self):
        # Test with valid arguments
        time_obj = Time(self.date, self.time, self.time_offset, self.geolocation)
        self.assertEqual(time_obj.date, self.date)
        self.assertEqual(time_obj.time, self.time)
        self.assertEqual(time_obj.geolocation, self.geolocation)
        self.assertIsInstance(time_obj, VedAstro.Time)

        # Test with invalid arguments
        with self.assertRaises(TypeError):
            Time(123, self.time, self.time_offset, self.geolocation)
        with self.assertRaises(TypeError):
            Time(self.date, 123, self.time_offset, self.geolocation)
        with self.assertRaises(TypeError):
            Time(self.date, self.time, 123, self.geolocation)
        with self.assertRaises(TypeError):
            Time(self.date, self.time, self.time_offset, "invalid_geolocation")

    def test_add_years(self):
        years = 7

        # Create a Time object
        time_obj = Time(self.date, self.time, self.time_offset, self.geolocation)

        # Test with valid arguments
        new_time = time_obj.add_years(years)

        self.assertEqual(new_time.date, "07/05/2017")
        self.assertIsInstance(new_time, VedAstro.Time)

        # Test with invalid argument
        with self.assertRaises(TypeError):
            time_obj.add_years("invalid_years")


if __name__ == '__main__':
    unittest.main()
