from django.db import models

class Usuario(models.Model):
    class Tipo(models.TextChoices):
        ALUNO = 'ALUNO', 'Aluno'
        PROFESSOR = 'PROFESSOR', 'Professor'
        ADMIN = 'ADMIN', 'Administrador'

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    
    # Campo opcional (pode ficar vazio)
    biografia = models.TextField(null=True, blank=True)
    
    # Campo obrigatório para o Admin não dar erro
    criado_em = models.DateTimeField(auto_now_add=True)
    
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=Tipo.choices, 
        default=Tipo.ALUNO
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordena primeiro pelo ID da matéria, depois pelo título
        ordering = ['materia', 'titulo']

    def __str__(self):
        return self.titulo