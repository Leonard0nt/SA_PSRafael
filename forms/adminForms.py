from django import forms
from AppAdmin.models import User, Cavalas
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class UserFormBase(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rut', 'nombres', 'apellidos', 'telefono', 'direccion', 'tipo_usuario', 'estado']
    
    rut = forms.CharField(max_length=12)
    password = forms.PasswordInput()
    nombres = forms.CharField(max_length=40)
    apellidos = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(widget=forms.Textarea, required=False)
    tipo_usuario = forms.ChoiceField(choices=User.TIPO_USUARIO_CHOICES)
    estado = forms.BooleanField(required=False)

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut:
            raise forms.ValidationError('El RUT es obligatorio')
        return rut

class ClienteForm(UserFormBase):
    class Meta:
        model = User
        fields = ['rut','password','nombres', 'apellidos', 'telefono', 'direccion', 'estado']
    # Puedes añadir validaciones o personalizar campos específicos para clientes si es necesario.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('estado', None)  # Remueve el campo 'estado' si existe
        self.fields['tipo_usuario'].required = False
        self.fields['tipo_usuario'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['rut']  # Establece el username como el rut

         # Establece la contraseña utilizando set_password
        password = self.cleaned_data.get('password')
        user.set_password(password)

        user.rut = self.cleaned_data['rut'].replace(".", "")
        
        if commit:
            user.save()
        return user



class ContadorForm(UserFormBase):
    class Meta:
        model = User
        fields = ['rut','password', 'nombres', 'apellidos', 'telefono', 'direccion', 'estado']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('estado', None)  # Remueve el campo 'estado' si existe
        self.fields['tipo_usuario'].required = False
        self.fields['tipo_usuario'].widget = forms.HiddenInput()

class CabaleroForm(UserFormBase):
    class Meta:
        model = User
        fields = ['rut','password', 'nombres', 'apellidos', 'telefono', 'direccion', 'estado']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('estado', None)  # Remueve el campo 'estado' si existe
        self.fields['tipo_usuario'].required = False
        self.fields['tipo_usuario'].widget = forms.HiddenInput()


class CavalaForm(forms.ModelForm):
    class Meta:
        model = Cavalas
        fields = ['idCavala', 'sectorCavala']

    idCavala = forms.IntegerField()
    sectorCavala = forms.CharField(max_length=100)

    def clean_idCavala(self):
        id_cavala = self.cleaned_data.get('idCavala')
        if not id_cavala:
            raise forms.ValidationError('El ID de la cavala es obligatorio')
        return id_cavala
    



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="RUT", max_length=255)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    # Aquí puedes añadir validaciones personalizadas si es necesario.
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Puedes agregar validaciones personalizadas, por ejemplo, comprobar si el usuario está activo.
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Credenciales incorrectas.")
        return cleaned_data
