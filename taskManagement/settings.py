from decouple import config, Csv
import dj_database_url

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
