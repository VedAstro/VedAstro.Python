from vedastro.objects import Time, LifeEvent
from vedastro.objects import Gender
import VedAstro.Library as libray


class Person(libray.Person):

    def __init__(self, id: str, name: str, birth_time: Time, gender: Gender, user_id: [str], notes: str,
                 life_event_list: [LifeEvent] = None):
        self.id = id
        self.name = name
        self.birth_time = birth_time
        self.gender = gender
        self.user_id = user_id
        self.notes = notes
        self.lifeEventList = life_event_list
        super().__init__(id, name, birth_time, gender, user_id, notes, life_event_list)
