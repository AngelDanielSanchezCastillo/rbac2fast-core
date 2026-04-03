from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PermissionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    permission_category_id: int


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    name: str | None = None
    permission_category_id: int | None = None


class PermissionRead(PermissionBase):
    id: int


# Assignment Schemas

class PermissionRouteCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    permission_id: int
    route_id: int


class UserPermissionCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    permission_id: int


class UserPermissionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    permission_id: int
    entity_type: str
    entity_id: int
