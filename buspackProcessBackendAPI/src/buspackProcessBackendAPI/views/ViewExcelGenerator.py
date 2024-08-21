from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from excel.UpdateExcel import UpdateExcel


class ViewExcelGenerator(View):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            UpdateExcel.run()
            return HttpResponse("El método de actualizacion de excel se ejecutó con éxito")
        except Exception as e:
                print(f"Error en la vista ViewExcelGenerator: {str(e)}")
                return HttpResponse("Error en la vista ViewExcelGenerator", status=500)