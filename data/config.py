from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# Database
DB_NAME = env.str("DATABASE_NAME")
DB_HOST = env.str("DATABASE_HOST")
DB_PASSWORD = env.str("DATABASE_PASSWORD")
DB_USER = env.str("DATABASE_USER")
DB_ENGINE = env.str("DATABASE_ENGINE")

ENGINE_URL = '{0}://{1}:{2}@{3}/{4}'.format(DB_ENGINE, DB_USER,
                                            DB_PASSWORD, DB_HOST, DB_NAME)