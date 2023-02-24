"""Updating informations in the UI"""


class Refresh:
    """This class refreshes the UI"""
    def __init__(self, parent):
        self.parent = parent

    def refresh(self):
        """This function refreshes the transactions"""
        try:
            self.parent.accounts_form.set_data()
            self.parent.welcome_form.get_total_balance()
            self.parent.welcome_form.get_this_month_spending()
            self.parent.insights_form.get_next_month_spending()
        except Exception:
            print("Error in refreshing")
