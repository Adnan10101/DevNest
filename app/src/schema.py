from pydantic import BaseModel
from typing import Optional

class Metadata(BaseModel):
    name: str
    namespace: Optional[str]

class VmDetails(BaseModel):
    id: int
    vmname: str
    username: str
    password: str

class CPU(BaseModel):
    cpu_count: int
    core_count: int
    memory: int

class Disk(BaseModel):
    size: int

class Network(BaseModel):
    ipv4_addr: str
    gateway: str

class Compute(BaseModel):
    cpu: CPU
    disk: Disk
    network: Network

class CreateInfraClaim(BaseModel):
    meta: Metadata
    vm: VmDetails
    compute: Compute

