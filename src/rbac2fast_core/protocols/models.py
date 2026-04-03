from typing import Protocol, List, Optional
from datetime import datetime

class RoleProtocol(Protocol):
    id: int
    name: str
    description: Optional[str]
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class PermissionCategoryProtocol(Protocol):
    id: int
    name: str

class PermissionProtocol(Protocol):
    id: int
    name: str
    permission_category_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class RouteProtocol(Protocol):
    id: int
    name: str
    is_active: bool

class UserRoleProtocol(Protocol):
    id: int
    user_id: int
    role_id: int

class PermissionAssignmentProtocol(Protocol):
    id: int
    permission_id: int
    entity_type: str
    entity_id: int

class PermissionRouteProtocol(Protocol):
    id: int
    permission_id: int
    route_id: int
