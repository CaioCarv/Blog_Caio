from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if not comentario:
            self.add_error(
                'comentario', 
                'Comentário deve ser prenchido'
            )



        print(data)

    class Meta: 
        model = Comentario
        fields= ('nome_comentario', 'email_comentario', 'comentario')