#  DevNest: Self-Service Infrastructure-as-Code Platform

**DevNest** is a modular, Kubernetes-native Infrastructure as a Service platform that allows users to request, provision, and manage infrastructure resources—such as VMs, storage, and databases—through declarative claims using a web UI or API.

> Supports both **Proxmox** and **fully AWS-based** provisioning via Crossplane and Terraform.

---

##  Key Features

- **Self-Service Portal** – Request infrastructure (VMs, DBs, buckets) with simple inputs.
- **Composable Infrastructure** – Build reusable pipelines using Crossplane compositions and XRDs.
- **Multi-Cloud Support** – Provision resources on-prem (Proxmox) or in AWS (EC2, S3, RDS, etc.).
- **Secure and Isolated** – IAM-based isolation (AWS) and secret management for credentials.
- **GitOps Ready** – Integrate with ArgoCD or GitHub Actions for continuous provisioning workflows.

---

## Components Used

- Crossplane	I
- Proxmox Terraform Provider	
- AWS Provider	
- Go Templates	
- Custom Operator (TODO)
- ArgoCD / GitHub Actions	GitOps workflow for resource automation

##  Getting Started

1. **Install Crossplane in your Kubernetes cluster**

2. **Install Providers**
   - Terraform Provider (for Proxmox)
   - AWS Provider (`crossplane/provider-aws`)

3. **Create Required Secrets**

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: aws-secret
     namespace: crossplane-system
   type: Opaque
   stringData:
     credentials: |
       [default]
       aws_access_key_id = YOUR_KEY
       aws_secret_access_key = YOUR_SECRET

  4. **Create AWS ProviderConfig**
  
  ```yaml
    apiVersion: aws.crossplane.io/v1beta1
    kind: ProviderConfig
    metadata:
      name: aws-providerconfig
    spec:
      credentials:
        source: Secret
        secretRef:
          name: aws-secret
          key: credentials
          namespace: crossplane-system
  ```

