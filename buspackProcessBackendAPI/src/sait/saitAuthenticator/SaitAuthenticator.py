
class SaitAuthenticator:
    def __init__(self):
        self.user = 'bopera.hub.usu'
        self.password = 'bopera.hub.usu'
        self.url = 'https://rest.empresar-sys.com.ar:1433/auth'

    def parametersFormData(self):
            return {
                        "usuario": self.user,
                        "password": self.password
                    }

