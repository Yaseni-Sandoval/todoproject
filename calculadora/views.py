from django.http import HttpResponse

def index(request):
    return HttpResponse("Realiza tus oraciones aquí...!")


def suma(request, num1, num2):
    calculo = int(num1) + int(num2)
    resultado = f"La suma de {num1} + {num2} = {calculo}"
    return HttpResponse(resultado)

def resta(request, num1, num2):
    calculo = int(num1) - int(num2)
    resultado = f"La resta de {num1} - {num2} = {calculo}"
    return HttpResponse(resultado)

def multiplicacion(request, num1, num2):
    calculo = int(num1) * int(num2)
    resultado = f"La multiplicación de {num1} * {num2} = {calculo}"
    return HttpResponse(resultado)