import os
from dotenv import load_dotenv

load_dotenv()

GITEA_API_URL = os.getenv("GITEA_API_URL")
GITEA_TOKEN = os.getenv("GITEA_TOKEN")
GITEA_REPO_OWNER = os.getenv("GITEA_REPO_OWNER")
REPO_NAME = os.getenv("GITEA_REPO_NAME")
INFRA_FILE_PATH = os.getenv("INFRA_FILE_PATH")
CLOUD_FILE_PATH = os.getenv("CLOUD_FILE_PATH")