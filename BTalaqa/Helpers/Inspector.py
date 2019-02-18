class Inspector:

    """
    Object is created as a collection of checks for a specific uploaded file in
    order to know if it's the correct format needed and everything is as expected
    or not
    """

    def __init__(self, checks):
        self.checks = checks
        self.passed_all_checks = True

    def execute_checks(self):
        """

        :return:
        """
        for check in self.checks:
            check.execute_check()
        for check in self.checks():
            if not check.passed and check.mandatory:
                self.passed_all_checks = False
            elif not check.passed and not check.mandatory:
                print("Warning!! Non-Mandatory check not passed!")





