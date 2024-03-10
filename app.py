import os

from flask.cli import with_appcontext

from apps import create_app, db
from apps.config import config_dict


# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
print(app_config.DB_PASS)
@app.cli.command("init_db")
@with_appcontext
def initialize():
    # 执行初始化工作
    db.create_all()

if __name__ == "__main__":
    app.run()