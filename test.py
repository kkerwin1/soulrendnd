import os, re

regex = re.compile("^/home/kris")
_path = os.getcwd()
match = regex.match(_path)
if match:
	DEBUG = True
	SECRET_KEY = 'django-insecure-nr*9bs(t$e(zecn4pr&z6*o==35=n2zjna*4sn9luprw9z4h7v'
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.sqlite3',
		}
    }

# production mode
else:
	regex2 = re.compile("^/home/adjutant")
	match = regex.match(_path)
	if match:
		DEBUG = False
		SECRET_KEY = secret_key
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql',
				'NAME': 'soulrendnd',
				'USER': 'adjutant',
				'PASSWORD': database_password,
				}
			}
	else:
		raise NameError("Program runs in neither the home directories of kris nor adjutant.")
