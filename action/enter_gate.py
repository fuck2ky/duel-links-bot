from .base_action import Action

class Enter_gate(Action):

    def __init__(self):
        self.locate = Location()
        self.click = Click()
