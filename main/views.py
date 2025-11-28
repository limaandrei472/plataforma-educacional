from django.shortcuts import render, redirect, get_object_or_404
from .models import Materia, Assunto, Usuario

# --- 1. FLUXO DE ENTRADA (O Início do Diagrama) ---

def login_view(request):
    # Se já tiver crachá (sessão), manda direto pra Home
    if 'usuario_id' in request.session:
        return redirect('home')

    # Se clicou no botão "Entrar"
    if request.method == 'POST':
        email_digitado = request.POST.get('email')
        senha_digitada = request.POST.get('senha')

        # Busca no banco
        usuario = Usuario.objects.filter(email=email_digitado, senha=senha_digitada).first()

        if usuario:
            # SUCESSO: Cria a sessão e manda pra Home
            request.session['usuario_id'] = usuario.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'erro': 'Email ou senha incorretos'})

    return render(request, 'login.html')

def cadastro_view(request):
    if request.method == 'POST':
        # Pega dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tipo = request.POST.get('tipo')
        biografia = request.POST.get('biografia')

        # Cria o usuário no banco
        Usuario.objects.create(
            nome=nome, email=email, senha=senha, 
            tipo_usuario=tipo, biografia=biografia
        )
        return redirect('login')

    return render(request, 'cadastro.html')

def logout_view(request):
    request.session.flush() # Limpa tudo
    return redirect('login')


# --- 2. FLUXO INTERNO (Do diagrama: Home -> Menu -> Matéria -> Assunto) ---

def home(request):
    # O PORTEIRO: Se não tiver logado, chuta pro login
    if 'usuario_id' not in request.session: return redirect('login')
    
    # Passamos o usuário para o template mostrar "Olá, Fulano"
    usuario = Usuario.objects.get(id=request.session['usuario_id'])
    return render(request, 'home.html', {'usuario': usuario})

def perfil_view(request):
    # O PORTEIRO
    if 'usuario_id' not in request.session: return redirect('login')
    
    # Pega os dados de QUEM está logado
    id_logado = request.session['usuario_id']
    usuario = get_object_or_404(Usuario, id=id_logado)

    # Se for professor, mostra as aulas que ele criou
    aulas_criadas = Assunto.objects.filter(autor=usuario)

    contexto = {
        'usuario': usuario,
        'aulas': aulas_criadas
    }
    return render(request, 'perfil_usuario.html', contexto)

def materia_lista(request, id_materia):
    # O PORTEIRO
    if 'usuario_id' not in request.session: return redirect('login')

    materia = get_object_or_404(Materia, id=id_materia)
    assuntos = Assunto.objects.filter(materia=materia)

    # Lógica da Busca (Opcional, mas útil)
    busca = request.GET.get('busca')
    if busca:
        assuntos = assuntos.filter(titulo__icontains=busca)

    return render(request, 'materia_lista.html', {'materia': materia, 'assuntos': assuntos})

def aula_detalhe(request, id_assunto):
    # O PORTEIRO
    if 'usuario_id' not in request.session: return redirect('login')

    assunto = get_object_or_404(Assunto, id=id_assunto)
    return render(request, 'aula_detalhe.html', {'assunto': assunto})

def professor_perfil(request, id_professor):
    # O PORTEIRO
    if 'usuario_id' not in request.session: return redirect('login')
    
    professor = get_object_or_404(Usuario, id=id_professor)
    
    # Busca as aulas desse professor específico
    aulas = Assunto.objects.filter(autor=professor)
    
    # Retorna o mesmo template de perfil, mas com os dados dele
    return render(request, 'perfil_usuario.html', {'usuario': professor, 'aulas': aulas})

def professores_lista(request):
    # O PORTEIRO
    if 'usuario_id' not in request.session: return redirect('login')

    # Busca apenas quem é PROFESSOR
    professores = Usuario.objects.filter(tipo_usuario=Usuario.Tipo.PROFESSOR)

    return render(request, 'professores_lista.html', {'professores': professores})