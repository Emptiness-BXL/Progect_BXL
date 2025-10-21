from django.shortcuts import render


def visit(request):
    return render(request, 'visit.html')

def hobbies(request):
    return render(request, 'hobbies.html')

def skills(request):
    return render(request, 'skills.html')

def me(request):
    return render(request, 'me.html')

def visit1(request):
    return render(request, 'visit.html')

def visit2(request):
    return render(request, 'visit.html')

def visit3(request):
    return render(request, 'visit.html')