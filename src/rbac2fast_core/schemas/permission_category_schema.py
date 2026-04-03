from pydantic import BaseModel, ConfigDict

class PermissionCategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str

class PermissionCategoryCreate(PermissionCategoryBase):
    pass

class PermissionCategoryRead(PermissionCategoryBase):
    id: int
