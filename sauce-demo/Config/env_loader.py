import os
from dotenv import load_dotenv

def load_env(env_name):
    env_file = f'config/.env.{env_name}'
    load_dotenv(env_file)

def get_env(key):
    return os.getenv(key)