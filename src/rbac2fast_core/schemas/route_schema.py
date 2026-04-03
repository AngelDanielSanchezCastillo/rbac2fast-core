from pydantic import BaseModel, ConfigDict

class RouteBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    is_active: bool = True

class RouteCreate(RouteBase):
    pass

class RouteRead(RouteBase):
    id: int
