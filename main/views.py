from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def home(request):
    """
    Відображення для рендеру головної сторінки (index.html).
    """
    return render(request, 'index.html')

class CalculationView(APIView):
    def post(self, request, *args, **kwargs):
        try:
     
            x = float(request.data.get('x', 0))

            y = x**2
            
            return Response({"x": x, "y": y}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self, request, *args, **kwargs):
        return Response({
            "error": "GET method is not allowed / Метод GET не дозволений",
            "example": {
            "post_body": {
                "x": "value"
            }
            }
        }, status=status.HTTP_400_BAD_REQUEST)