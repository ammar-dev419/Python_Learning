class Task:
    def __init__(self, title, description, done=0, user_id=None):
        self.title = title
        self.description = description
        self.done = done
        self.user_id = user_id
        