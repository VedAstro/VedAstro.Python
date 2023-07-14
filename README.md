# VedAstro Python
[![License](https://img.shields.io/github/license/VedAstro/VedAstro.Python)](https://github.com/VedAstro/VedAstro.Python/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/VedAstro/VedAstro.Python)](https://github.com/VedAstro/VedAstro.Python/issues)

This is a Python wrapper library for [VedAstro](https://github.com/VedAstro/VedAstro). A powerful tool for astronomical calculations and data analysis. It provides a collection of functions and classes to perform various astronomical calculations, such as celestial object positions, time conversions, coordinate transformations, and more.

## Features

- Calculate the position of celestial objects (planets, stars, etc.) at a given date and time.
- Calculate Dasas
- Calculate Charts ( Rasi , Dasa .. etc)
- Many more ...
## Installation

You can install VedAstro  using pip:

```shell
pip install vedastro
```

## Usage

Here's a simple example.
```python
from vedastro.calculators import SaturnInAries
from vedastro.objects import GeoLocation, Time, Person, Gender

# Create a GeoLocation object for Tokyo, Japan
geolocation = GeoLocation(location="Tokyo", latitude=35.6895, longitude=139.6917).geolocation

# Define the birth date, time, and time offset
date = "07/05/2010"
time = "06:42"
time_offset = "+09:00"

# Create a Time object for the birth date, time, and time offset
time_ob = Time(date, time, time_offset, geolocation).time_object

# Define the person's ID, user ID, notes, name, and gender
id = "1234"
user_id = "123"
notes = ""
name = "John Doe"
gender = Gender.Male

# Create a Person object for John Doe with the provided details
john_doe = Person(id=id, user_id=user_id, name=name, gender=gender, birth_time=time_ob, notes=notes).person

# Create a SaturnInAries calculator object for the given time and person
saturn_aries = SaturnInAries(time_ob, john_doe)

# Calculate the occurrence of Saturn in Aries
occurrence = saturn_aries.occuring

# Get the related celestial body for Saturn in Aries
related_body = saturn_aries.related_body

# Print the results
print("Occurrence of Saturn in Aries:", occurrence)
print("Related celestial body:", related_body)
```

For more examples and detailed documentation, please refer to the [documentation](https://github.com/VedAstro/VedAstro.Python) provided.

## Contributing

Contributions to VedAstro Python are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request. Make sure to read our [contribution guidelines](https://github.com/VedAstro/VedAstro.Python/CONTRIBUTING.md) before getting started.

## License

VedAstro Python is released under the MIT License. See [LICENSE](https://github.com/VedAstro/VedAstro.Python/LICENSE) for more information.


