from django.shortcuts import render
import re

def home(request):
    return render(request, 'calc/home.html')

def calculate(request):
    expression = request.POST.get('expression', '')
    res = None

    if re.fullmatch(r'[0-9+\-*/.]+', expression):
        try:
            res = eval(expression)
        except ZeroDivisionError:
            res = "Error: Div by 0"
        except Exception:
            res = "Error"
    else:
        res = "Invalid Input"

    return render(request, 'calc/home.html', {'result': res})