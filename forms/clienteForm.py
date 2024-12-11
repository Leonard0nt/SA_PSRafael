from django import forms
from AppAdmin.models import User

class ClientesForm(forms.ModelForm):
    """
    Formulario para registrar nuevos usuarios como clientes.
    """
    # Campos personalizados para contraseña y confirmación
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        label="Contraseña",
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}),
        label="Confirmar Contraseña",
        required=True
    )

    class Meta:
        model = User
        fields = [
            'rut', 'nombres', 'apellidos', 'email', 'telefono', 'direccion', 'tipo_usuario', 'password'
        ]
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': 'RUT (ej: 12345678-9)'}),
            'nombres': forms.TextInput(attrs={'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electrónico'}),
            'telefono': forms.NumberInput(attrs={'placeholder': 'Teléfono'}),
            'direccion': forms.Textarea(attrs={'placeholder': 'Dirección', 'rows': 2}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'rut': 'RUT',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'tipo_usuario': 'Tipo de Usuario',
            'password': 'Contraseña',
        }

    def clean_rut(self):
        """
        Validación personalizada para el campo RUT.
        """
        rut = self.cleaned_data.get('rut')
        if User.objects.filter(rut=rut).exists():
            raise forms.ValidationError("Este RUT ya está registrado.")
        return rut

    def clean(self):
        """
        Validación para asegurarse de que las contraseñas coincidan.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self, commit=True):
        """
        Guarda el usuario asegurándose de encriptar la contraseña y asignar tipo_usuario como 'cliente'.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.tipo_usuario = 'cliente'  # Fija el tipo de usuario como 'cliente'
        if commit:
            user.save()
        return user
