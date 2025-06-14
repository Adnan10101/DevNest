# 🧠 DevNest: Self-Service Infrastructure-as-Code Platform

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

Components Used

- Crossplane	I
- Proxmox Terraform Provider	
- AWS Provider	
- Go Templates	
- Custom Operator (TODO)
- ArgoCD / GitHub Actions	GitOps workflow for resource automation
