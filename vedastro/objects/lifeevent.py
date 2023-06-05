from VedAstro.Library import LifeEvent


class LifeEvent(LifeEvent):
    """
     Simple data type to hold info on life events of a person
     This event is to mark important moments in a persons life
     This is used later by calculators like Dasa to show against astrological predictions
    """""

    def __init__(self):
        self.Name: str
        self.Description: str
        self.StartTime: str
        self.Location: str
        self.Nature: str
        self.Timezone: str = ""
        super.__init__(self)

