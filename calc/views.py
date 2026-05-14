from django.shortcuts import render
from django.http import HttpResponse
import re


def home(request):
    return render(request, 'calc/home.html')


def calculate(request):
    expression = request.POST.get('expression', '')

    # 2. Safety Check!
    # We only allow: 0-9, +, -, *, /, and .
    # This prevents people from sending "import os; os.remove('project')"
    if re.fullmatch(r'[0-9+\-*/.]+', expression):
        try:
            # 3. Solve the math string
            res = eval(expression)
        except ZeroDivisionError:
            res = "Error: Div by 0"
        except Exception:
            res = "Invalid Math"
    else:
        # If the string has letters or weird symbols, we block it
        res = "Safety Block: Invalid Input"

    # 4. Send the result back
    return render(request, "calc/home.html", {'result': res})
