import gogs_client
import src.env as env
from base64 import b64encode
from json import loads

class GitWrapper():
    def __init__(self):
        self.api = gogs_client.GogsApi(env.GITEA_API_URL)
        self.auth = gogs_client.Token(env.GITEA_TOKEN)

    def get_repo(self):
        repo = self.api.get_user_repos(self.auth, env.GITEA_REPO_OWNER)
        if not self.api.repo_exists(self.auth, env.GITEA_REPO_OWNER, env.REPO_NAME):
            print("Repository does not exist")
        else:
            repo = self.api.get_repo(self.auth, env.GITEA_REPO_OWNER, env.REPO_NAME)
            if repo.fork:
                print("Repository is a fork")
            else:
                print("Repository is not a fork")

    def create_file(self, yaml, file_name, REPO_NAME, FILE_PATH):
        path = f"/repos/{env.GITEA_REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}/{file_name}?ref=main"
        body = {
            "content": b64encode(yaml.encode("utf-8")).decode("utf-8"),
            "message": f"Add {file_name}",
            "branch": "main",  
        }
        content = self.api.post(auth = self.auth, path = path, data = body)
        return loads(content.text)
