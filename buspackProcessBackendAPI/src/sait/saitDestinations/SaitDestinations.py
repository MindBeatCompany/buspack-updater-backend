
class SaitDestinations:
    def __init__(self, tokenResponse, isActive):
        self.activos = isActive
        self.url = 'https://testrest.empresar-sys.com.ar:1434/sait/destinosHabilitados'
        self.token = tokenResponse.json().get('token')

    def parametersFormData(self):
        return {"activos" : self.activos}
    
    def headerToken(self):
        return {"token" : self.token}