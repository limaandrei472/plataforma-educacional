from .models import Materia

def menu_materias(request):
    return {'materias_globais': Materia.objects.all().order_by('nome')}