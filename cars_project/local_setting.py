# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i-cb1s+ki!z6lsj1_ie-n=3h#)fyzbgj2!&&ua9e1d!^s-v19$'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'flyhigh20',
        'OPTIONS': {
            'autocommit': True
            }     
    }
}
