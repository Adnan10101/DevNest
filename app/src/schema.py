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

class Subnet(BaseModel):
    enabled: bool
    name: str

class VPC(BaseModel):
    enabled: bool
    name: str
    cidr: str

class Database(BaseModel):
    enabled: bool
    db_name: str
    username: str
    password: str
    instance_class: str
    db_type: str
    version: str

class Instance(BaseModel):
    enabled: bool
    instance_name: str
    image_id: str
    instance_type: str

class Bucket(BaseModel):
    enabled: bool
    bucket_name: str

class Resources(BaseModel):
    s3: Bucket
    ec2: Instance
    db: Database
    vpc: VPC
    subnet: Subnet


class CreateCloudClaim(BaseModel):
    meta: Metadata
    region: str
    resources: Resources