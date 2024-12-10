import os


env_file = '.env'

if os.path.isfile(env_file):
    from dotenv import load_dotenv
    load_dotenv()


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
OPEN_AI_API_KEY = str(os.getenv("OPEN_AI_API_KEY"))
DB_URI = str(os.getenv("DB_URI"))
DB_NAME = str(os.getenv("DB_NAME"))