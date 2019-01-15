
class EnvItem:
    def __init__(self, name="", value="Not found"):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"

