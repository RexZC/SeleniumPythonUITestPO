from business.register_bisiness import RegisterBusiness

class FirstCase(object):
    def __init__(self):
        self.login=RegisterBusiness()
    def test_login_email_error(self):
        self.login.login('34','111','111111','111111')
        #通过assert判断是否为error

    def test_login_user_name_errror(self):
        self.login('34', '111')

    def test_login_code_error(self):
        self.login('34', '111')

    def test_login_success(self):
        self.login('34', '111')

