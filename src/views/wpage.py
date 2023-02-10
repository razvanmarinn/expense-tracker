from UI.wpage import Ui_AcccountsFrame


class WelcomeFrame(Ui_AcccountsFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.l_username.setText(self.parent.user.username)