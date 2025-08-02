from django.contrib.auth import get_user_model

User = get_user_model()

def run():
    username = "CHIOMA"
    email = "cezeh247@gmail.com"
    password = "Chioma#Ezeh091@.com"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")
    else:
        print("Superuser already exists.")
