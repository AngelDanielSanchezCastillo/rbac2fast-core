from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    description: str | None = None
    is_active: bool = True


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class RoleRead(RoleBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None


# Assignment Schemas

class RolePermissionCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    permission_id: int


class UserRoleCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    role_id: int


class UserRoleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    role_id: int
