from vedastro.objects import Time
from vedastro.objects.eventname import EventName
from vedastro.objects.eventnature import EventNature


class Prediction:
    def __init__(self, name:EventName, nature:EventNature, description:str, strength:str, startTime:Time, endTime:Time):
        self.name = name
        self.nature = nature
        self.description = description
        self.strength = strength
        self.startTime = startTime
        self.endTime = endTime
        super().__init__(name, nature, description, strength, startTime, endTime)


    def get_duration_minutes(self):
        return super().GetDurationMinutes()
