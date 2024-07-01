
class SaitDestinations:
    def __init__(self, tokenResponse, isActive):
        self.activos = isActive
        self.url = 'https://rest.empresar-sys.com.ar:1433/sait/destinosHabilitados'
        self.token = tokenResponse.json().get('token')

    def parametersFormData(self):
        return {"activos" : self.activos}
    
    def headerToken(self):
        return {"token" : self.token}