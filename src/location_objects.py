class Chest:
    def __init__(self, name, description, contents):
        self.name = name
        self.description = description
        self.contents = contents
        self.is_open = False
        self.is_locked = False

    def __str__(self):
        return self.name

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def is_open(self):
        return self.is_open

    def is_locked(self):
        return self.is_locked

    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

    def get_contents(self):
        return self.contents
