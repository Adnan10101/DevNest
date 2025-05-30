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