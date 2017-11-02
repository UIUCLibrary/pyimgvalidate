class ValidationData:
    def __init__(self, filename):
        self.filename = filename
        self.errors = []
        self.valid = None

    def __str__(self) -> str:
        return ("Source: {}\n\n"
                "{}\n"
                "{}").format(self.filename, "Validated" if self.valid else "Errors:", "\n".join(self.errors))

