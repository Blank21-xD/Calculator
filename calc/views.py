from django.shortcuts import render
from django.http import HttpResponse
import re


def home(request):
    return render(request, 'calc/home.html')


def calculate(request):
    expression = request.POST.get('expression', '')
    res = None  # Start with None instead of an empty string

    if re.fullmatch(r'[0-9+\-*/.]+', expression):
        try:
            res = eval(expression)
            # If the result is 0.0 or 0, Python stores it as 0
        except ZeroDivisionError:
            res = "Error: Div by 0"
        except Exception:
            res = "Invalid Math"
    else:
        res = "Error"

    return render(request, "calc/home.html", {'result': res})
