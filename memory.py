class Memory:
    def __init__(self):
        self.logs = []

    def add(self, entry):
        self.logs.append(entry)

    def get_context(self):
        return "\n".join(self.logs)
