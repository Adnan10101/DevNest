import yaml
from jinja2 import Template
from src.git_client import GitWrapper
from src.template import (
    infra_claim
)

class gitea():
    def __init__(self):
        self.git = GitWrapper()
    
    def git_create(self, yaml_contents, file_name, FILE_PATH, REPO_NAME):
        self.git.create_file(yaml_contents, file_name,  REPO_NAME, FILE_PATH,)

    def render_template(request, template_):
        template = Template(template_)
        rendered_yaml = template.render(request.dict())
        file_name = f'{request.meta.name}.yaml'
        return rendered_yaml, file_name

class Infra(gitea):
    def __init__(self, FILE_PATH, REPO_NAME):
        super().__init__() 
        self.file_path = FILE_PATH
        self.repo = REPO_NAME

    def create_claim(self, request, claim):
        if claim == "infra_claim":
            template = infra_claim
        yaml_contents, file_name = gitea.render_template(request, template)
        super().git_create(yaml_contents, file_name, self.file_path, self.repo)
        # response = CreatePVResponse(
        #     meta = request.meta,
        #     message = "Created and Pushed PV to gitea!"
        # )
        # return response
