from typing import List

import VedAstro.Library as VedAstro

from vedastro.objects import Time, GeoLocation, Person
from vedastro.objects.eventtag import EventTag


class EventManager:
    @staticmethod
    def calculate_events(events_precision: float, start_time: Time, end_time: Time,
                         geo_location: GeoLocation, person: Person, inputed_event_tags: List[EventTag]):
        """
        Calculate the events between the start time and end time with the given precision.
        :param events_precision:
        :param start_time:
        :param end_time:
        :param geo_location:
        :param person:
        :param inputed_event_tags:
        :return:
        """
        event_list = VedAstro.EventManager.CalculateEvents(events_precision, start_time, end_time, geo_location, person,
                                                         inputed_event_tags)
        return event_list
