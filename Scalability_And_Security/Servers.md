## Servers

- Cloud
- On-Premise

### Cloud Servers:

> Cloud servers are virtual servers hosted and managed by a cloud provider (like AWS, Google Cloud, Azure) in remote data centers.

Virtualization: Physical machines in the provider’s data centers are split into many “virtual” servers using hypervisors; each virtual machine is your “cloud server”.

Access: You control them over the internet via APIs, dashboards, or CLI tools (e.g., create an EC2 instance, start/stop, scale up memory).

Billing model: Usually pay‑as‑you‑go (by vCPU, RAM, disk, bandwidth).

Typical trade‑offs:

✅ Pros:

- Fast scaling (add more servers in minutes).

- Lower upfront cost, no need to buy hardware.

- Built‑in reliability, backups, and global availability.

❌ Cons:

- Ongoing subscription cost.

- You rely on internet connectivity and the provider’s SLAs.

- Less physical control over hardware.

### On-Premise:

> On‑premise servers (often called just “on‑prem”) are physical servers and infrastructure that live inside your own organization, such as in an office basement, server room, or private data center.

Ownership: You buy and own the hardware (racks, servers, storage, networking gear).

Management: Your internal IT / DevOps team installs, configures, maintains, and secures them (OS, patches, backups, network, etc.).

Control & customization: You have full control over hardware, network topology, security policies, and data location, which is important for some regulated industries (e.g., finance, healthcare).

Typical trade‑offs:

✅ Pros:

- No dependence on internet for core operations.

- High control, predictable latency for local apps.

❌ Cons:

- High upfront cost (hardware + space + power + cooling).

- Harder and slower to scale (you must buy new machines).
