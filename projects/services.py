from .models import Project
from abc import abstractmethod
from abc import ABC

class ProjectService(ABC):
    @abstractmethod
    def get_all_projects(self, status=None):
        pass
    @abstractmethod
    def get_project_by_id(self, id: str):
        pass
    @abstractmethod
    def create_project(self, data: dict):
        pass
    @abstractmethod
    def update_project(self, id: int, data: dict):
        pass

class ProjectServiceImpl(ProjectService):
    def get_all_projects(self, status=None):
        projects = Project.objects.all()
        if status:
            projects = projects.filter(status=status)
        return projects

    def get_project_by_id(self, id: str):
        projects = Project.objects.get(id=id)
        return projects

    def create_project(self, data: dict):
        project = Project.objects.create(**data)
        return project
    
    def update_project(self, id: int, data: dict):
        project = Project.objects.filter(id=id).update(**data)
        return project
