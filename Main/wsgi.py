from whitenoise import WhiteNoise
from bakend import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')