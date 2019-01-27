
class EnvItem:
    def __init__(self, name="", value=""):
        self.name = name
        self.value = value

    @staticmethod
    def separator():
        return "==>"

    def change_value(self, value):
        self.value = value

    def __str__(self):
        return f"{self.name} {EnvItem.separator()} {self.value}"
