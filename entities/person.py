class Person:
    def __init__(self, identification, names, age):
        self._identification = identification
        self._names = names
        self._age = age

    def show_info(self):
        return f"ID: {self._identification}, Name: {self._names}, Age: {self._age}"