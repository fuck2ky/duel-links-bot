class Action(object):
    def __init__(self):
        pass

    def post_do(self):
        pass

    @classmethod
    def action(self, check_after_do=True):
        if self.post_do():
            self.do()
        if check_after_do:
            return self.after_do()
        return True

    def do(self):
        pass

    def after_do(self):
        pass
