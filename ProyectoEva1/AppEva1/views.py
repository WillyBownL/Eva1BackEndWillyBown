from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'AppEva1/index.html')

def MH(request):
    data = {'img': 'MH.jfif',
            'nombre': 'Monster Hunter World',
            'descripcion':'Juego de cazar monstruos',
            'genero':'ARPG'
            }
    return render(request,'AppEva1/detalles.html',data)
def P3R(request):
    data = {'img': 'P3R.jpg',
            'nombre': 'Persona 3 reload',
            'descripcion':'Clasico del rpg re creado al estlo de la quinta entrega',
            'genero': 'RPG'}
    return render(request,'AppEva1/detalles.html',data)
def DS3(request):
    data = {'img': 'DS3.jpg',
            'nombre': 'Dark Souls 3',
            'descripcion':'Juego desafiante que genero un culto alrededor de su dificultad',
            'genero': 'ARPG - hack and slash'}
    return render(request,'AppEva1/detalles.html',data)
