
class SaitAuthenticator:
    def __init__(self):
        self.user = 'bopera.hub.tes'
        self.password = 'bopera.hub.tes'
        self.url = 'https://testrest.empresar-sys.com.ar:1434/auth'

    def parametersFormData(self):
            return {
                        "usuario": self.user,
                        "password": self.password
                    }

