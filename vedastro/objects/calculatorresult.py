import VedAstro.Library as libray


class CalculatorResult(libray.CalculatorResult):

    def __init__(self):
        super().__init__()
        self.occuring = super().Occuring
        self.nature_override = super().NatureOverride
        self.description_override = super().DescriptionOverride
