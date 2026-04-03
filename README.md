# rbac2fast-core

🚀 Core abstract package for Role-Based Access Control (RBAC) in Python/FastAPI. Contains Protocols and Pydantic schemas without database logic.

> [!WARNING]
> **Internal Use Notice**
> 
> This package is designed and maintained by the **Solautyc Team** for internal use. While it is publicly available, it may not work as expected in all environments or use cases outside of our specific infrastructure. We do not provide support or guarantees for external usage, and we are not responsible for any issues that may arise from using this package in other contexts.
> 
> Use at your own risk. Contributions and feedback are welcome, but compatibility with external environments is not guaranteed.

## Features

- 🧩 **Abstract Interfaces**: Defines standard `Protocols` for RBAC models and services.
- 📦 **Pydantic Schemas**: Pre-defined base models for validation and serialization of Roles, Permissions, Routes, and Assignments.
- 🪶 **Lightweight**: Zero database dependencies; relies solely on standard Python abstractions and `pydantic`.
- 🔌 **Pluggable Architecture**: Allows multiple concrete implementations (e.g., standard global RBAC or multi-tenant RBAC) to share a standardized API contract.

## Installation

```bash
pip install rbac2fast-core
```

## Structure

This package exposes abstract definitions that concrete implementations (like `permissions2fast-fastapi`) will fulfill. 

### Protocols (`rbac2fast_core.protocols`)

Defines minimal structural requirements that underlying models must fulfill:
- `RoleProtocol`, `PermissionProtocol`, `RouteProtocol`
...

### Schemas (`rbac2fast_core.schemas`)

Provides validation schemas:
- `RoleBase`, `RoleCreate`, `RoleRead`
- `PermissionBase`, `PermissionCreate`
...

## Usage

This package is not meant to be used standalone to handle permissions, but rather to be imported as a dependency by actual implementation packages or application layers that need to adhere to the standard RBAC design.

Example of implementing a protocol in your ORM model:

```python
from sqlmodel import SQLModel, Field
from rbac2fast_core.protocols.models import RoleProtocol

class Role(SQLModel, table=True):
    # This class structurally fulfills RoleProtocol
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: str | None = None
    is_active: bool = True
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Angel Daniel Sanchez Castillo
