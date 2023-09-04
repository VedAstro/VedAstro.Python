from vedastro.objects import Time, LifeEvent, GeoLocation
from vedastro.objects import Gender
import VedAstro.Library as VedAstro


class Person:

    def __init__(self, id: str, name: str, birth_time: Time, gender: Gender, user_id: [str], notes: str,
                 life_event_list: [LifeEvent] = None):
        self.id = id
        self.name = name
        self.birth_time = birth_time
        self.gender = gender
        self.user_id = user_id
        self.notes = notes
        self.lifeEventList = life_event_list

        self.person = VedAstro.Person(id, name, birth_time, gender, user_id, notes, life_event_list)

    def get_birth_location(self):
        return self.person.GetBirthLocation()

    def get_age(self, time: Time = None):
        if time is None:
            return self.person.GetAge()
        return self.person.GetAge(time)

    def get_birthtime(self):
        return self.person.BirthTime()
