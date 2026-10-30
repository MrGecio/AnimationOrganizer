
from fastapi import FastAPI

from database.database import engine, Base

from model.user import User
from backend.model.rol import Role
from backend.model.groups_tasks import GroupTasks
from backend.model.tasks import Tasks
from backend.model.groups_tasks_views import GroupsTasksViews
from backend.model.views import Views
from backend.model.jwt_auth_users import JWTAuthUsers
from backend.model.permisions import Permissions
from backend.model.permissions_group import PermissionsGroup
from backend.model.groups_tasks import GroupTasks
from backend.model.groups_tasks_views import GroupsTasksViews
from backend.model.files_tasks_type import FilesTasksTypes
from backend.model.files_tasks_groups import FilesTasksGroups

Base.metadata.create_all(bind=engine)

app = FastAPI()

