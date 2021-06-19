from users.forms import UserRegistrationForm
from users.models import User


class UserAdminRegisterForm(UserRegistrationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'image', 'email', 'password1', 'password2')
