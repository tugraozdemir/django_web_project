from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50,label = "Ad")
    last_name = forms.CharField(max_length=50,label = "Soyad")
    username = forms.CharField(max_length=50,label = "Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı doğrula",widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    
    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm  and password !=confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        values = {
            "username" : username,
            "first_name" : first_name,
            "last_name" : last_name,
            "password" : password,
            "email" : email,
            
            
        }
        return values
        
        