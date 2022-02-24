# Appdog

mkdir appname
cd appname

- make the environment
    apt-get install python3-venv  
    mkdir env
    python3 -m venv env

- to make the env activate 
    source env/bin/avtivate

- install all the dependencies packages and software
    sudo apt-get install python3
    pip3 install django  
    pip3 install djangorestframework
    pip3 install markdown       # Markdown support for the browsable API.    
    pip3 install django-filter  # Filtering support

- Project Setup
    django-admin startproject Appdog   # Note the trailing '.' character
    cd Appdog
    django-admin startapp login
    cd ..


-Add  settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True #added by samyak


urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]

- for postgresql server #as per your database setup
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Appdog',
        'USER': 'samyak3009',
        'PASSWORD': 'samyak',
        'HOST': 'localhost',
        'PORT': '5432',
    }

- Now sync your database for the first time:
    python3 manage.py migrate
    # it should show ok 

- YUP ready to run the server
    python3 manage.py runserver 8000










