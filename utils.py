import os
from getpass import getpass


def set_keys():
    with open('.env', 'a') as env_file:
        env_file.write("OPENAI_API_KEY=" + getpass(prompt="OpenAI API Key: ") + "\n")
        env_file.write("ELASTIC_CLOUD_ID=" + getpass(prompt="ES Cloud ID: ") + "\n")
        env_file.write("ELASTIC_CLOUD_PASSWORD=" + getpass(prompt="ES Cloud Password: "))


def set_env():
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["LINE_PRINT"] = "============================================"
