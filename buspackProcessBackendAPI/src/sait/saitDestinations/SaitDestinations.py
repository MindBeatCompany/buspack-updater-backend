
class SaitDestinations:
    def __init__(self, token):
        self.activos = 1
        self.url = 'https://testrest.empresar-sys.com.ar:1434/sait/destinosHabilitados'
        self.token = token.json().get('token')

    def parametersFormData(self):
        return {"activos" : self.activos}
    
    def headerToken(self):
        return {"token" : self.token}
