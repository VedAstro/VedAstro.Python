import VedAstro.Library as libray

from vedastro.objects import Person


class EventChartTools(libray.EventChartTools):

    def __init__(self):
        super().__init__()

    @staticmethod
    def auto_calculate_time_range(input_person: Person, time_preset_raw: str, output_timezone: TimeSpan):
        return super().auto_calculate_time_range(input_person, time_preset_raw, output_timezone)
