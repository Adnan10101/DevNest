import yaml
from jinja2 import Template
from src.git_client import GitWrapper
from src.template import (
    infra_claim,
    cloud_claim
)
from src.schema import(
    CreateCloudClaim
)

class RenderFile():
    def __init__(self, ):
        self.git = GitWrapper()
        
    def git_create(self, yaml_contents, file_name, FILE_PATH, REPO_NAME):
        self.git.create_file(yaml_contents, file_name,  REPO_NAME, FILE_PATH,)

    def render_template(self, request, template_):
        template = Template(template_)
        rendered_yaml = template.render(request.dict())
        file_name = f'{request.meta.name}.yaml'
        return rendered_yaml, file_name
    
    
class Infra(RenderFile):
    def __init__(self, FILE_PATH, REPO_NAME, template):
        super().__init__()
        self.file_path = FILE_PATH
        self.repo = REPO_NAME
        self.template = template

    def create_cloud(self, request: CreateCloudClaim):
        yaml_contents, file_name = self.render_template(request, self.template)
        self.git_create(yaml_contents, file_name, self.file_path, self.repo)
