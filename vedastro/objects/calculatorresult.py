class CalculatorResult:

    def __init__(self, parent_class):
        super().__init__()
        self.occuring = parent_class.Occuring
        self.nature_override = parent_class.NatureOverride
        self.description_override = parent_class.DescriptionOverride
        self.related_body = parent_class.RelatedBody
