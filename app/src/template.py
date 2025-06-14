from jinja2 import Template

infra_claim = '''
---
apiVersion: dnacloud.home/v1alpha1
kind: virtInfra
metadata:
  name: {{ meta.name }}
  {% if meta.namespace %}
  namespace: {{ meta.namespace }}
  {% endif %}
spec:
  vm_details:
    id: {{ vm.id }}
    vmname: {{ vm.vmname }}
    username: {{ vm.username }}
    password: {{ vm.password }}
  compute:
    cpu:
      cpu_count: {{ compute.cpu.cpu_count }}
      core_count: {{ compute.cpu.core_count }}
      memory: {{ compute.cpu.memory }}
    disk:
      size: {{ compute.disk.size }}
    network:
      ipv4_addr: {{ compute.network.ipv4_addr }}
      gateway: {{ compute.network.gateway }}
'''

cloud_claim = '''
---
apiVersion: dnacloud.home/v1alpha1
kind: cloudInfra
metadata:
  name: {{ meta.name }}
  namespace: {{ meta.namespace }}
spec:
  region: {{ region }}
  resources:
    s3:
      enabled: {{ resources.s3.enabled }}
      bucketName: {{ resources.s3.bucket_name }}
    ec2:
      enabled: {{ resources.ec2.enabled }}
      instanceName: {{ resources.ec2.instance_name }}
      imageID: {{ resources.ec2.image_id }}
      instanceType: {{ resources.ec2.instance_type }}
    db:
      enabled: {{ resources.db.enabled }}
      dbName: {{ resources.db.db_name }}
      username: {{ resources.db.username }}
      password: {{ resources.db.password }}
      instanceClass: {{ resources.db.instance_class }}
      dbType: {{ resources.db.db_type }}
      engineVersion: "{{ resources.db.version }}"

    vpc:
      name: {{ resources.vpc.name }}
      enabled: {{ resources.vpc.enabled }}
      cidr: "{{ resources.vpc.cidr }}"
    
    subnet:
      enabled: {{ resources.subnet.enabled }}
      name: {{ resources.subnet.name }} 
'''