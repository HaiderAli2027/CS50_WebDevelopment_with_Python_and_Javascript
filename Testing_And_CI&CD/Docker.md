# 🐳 Docker — Complete Notes

---

## 1. What is Docker?

Docker is an **open-source platform** that allows you to **build, ship, and run applications** inside lightweight, portable units called **containers**.

Instead of worrying about _"it works on my machine"_ problems, Docker packages your application along with **everything it needs** — code, runtime, libraries, config files — into a single container that runs consistently **anywhere**.

> Think of Docker as a way to box up your app so it behaves the same on your laptop, your teammate's machine, and a production server.

Docker was released in **2013** by Solomon Hykes and is built on top of Linux kernel features like **namespaces** and **cgroups**.

---

## 2. Docker vs Virtual Machines (VMs)

Both Docker containers and VMs are used to isolate applications, but they work very differently under the hood.

| Feature            | Docker (Container)    | Virtual Machine     |
| ------------------ | --------------------- | ------------------- |
| **OS**             | Shares host OS kernel | Has its own full OS |
| **Size**           | MBs (lightweight)     | GBs (heavy)         |
| **Startup Time**   | Seconds               | Minutes             |
| **Performance**    | Near-native           | Some overhead       |
| **Isolation**      | Process-level         | Hardware-level      |
| **Portability**    | Highly portable       | Less portable       |
| **Resource Usage** | Low                   | High                |

### How it looks architecturally:

```
Virtual Machines:               Docker Containers:
┌──────────────────┐            ┌──────────────────┐
│   App A  App B   │            │   App A  App B   │
│   Libs   Libs    │            │   Libs   Libs    │
│   OS     OS      │            ├──────────────────┤
├──────────────────┤            │   Docker Engine  │
│    Hypervisor    │            ├──────────────────┤
├──────────────────┤            │    Host OS       │
│    Host OS       │            ├──────────────────┤
├──────────────────┤            │    Hardware      │
│    Hardware      │            └──────────────────┘
└──────────────────┘
```

**Key takeaway:** VMs virtualize hardware. Docker virtualizes the OS. Docker is faster and lighter, but VMs offer stronger isolation.

---

## 3. What is a Container?

A **container** is a **running instance of a Docker image**. It is an isolated process on your host machine that:

- Has its own **filesystem**
- Has its own **network interface**
- Has its own **process space**
- But **shares the host OS kernel**

### Container vs Image

| Term          | Description                                         |
| ------------- | --------------------------------------------------- |
| **Image**     | A read-only blueprint/template to create containers |
| **Container** | A live, running instance created from an image      |

> An **image** is like a class in OOP. A **container** is like an object (instance) of that class.

### Container Lifecycle

```
docker pull  →  Image downloaded
docker run   →  Container created & started
docker stop  →  Container stopped
docker rm    →  Container removed
```

---

## 4. Important Docker Concepts

### 4.1 Dockerfile

A `Dockerfile` is a **text file with instructions** to build a Docker image. Docker reads it top to bottom.

```dockerfile
# Start from an official base image
FROM node:18-alpine

# Set working directory inside container
WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the source code
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["node", "server.js"]
```

**Common Dockerfile instructions:**

| Instruction | Purpose                               |
| ----------- | ------------------------------------- |
| `FROM`      | Base image to start from              |
| `WORKDIR`   | Set working directory                 |
| `COPY`      | Copy files from host to container     |
| `RUN`       | Execute a command during build        |
| `EXPOSE`    | Document which port the app uses      |
| `CMD`       | Default command when container starts |
| `ENV`       | Set environment variables             |
| `ARG`       | Build-time variables                  |

---

### 4.2 Docker Image

- A **read-only, layered template** built from a Dockerfile
- Each instruction in a Dockerfile creates a **layer**
- Layers are **cached** — only changed layers are rebuilt (makes builds fast)
- Stored locally or on **Docker Hub** (a public registry)

```bash
docker build -t my-app:1.0 .     # Build image from Dockerfile
docker images                     # List local images
docker pull nginx                 # Pull image from Docker Hub
docker push my-app:1.0           # Push image to registry
```

---

### 4.3 Docker Hub / Registry

- **Docker Hub** is the default public registry at `hub.docker.com`
- You can pull official images (nginx, postgres, node, python, etc.)
- You can push your own images to share or deploy
- Private registries also exist (AWS ECR, GitHub Container Registry, etc.)

---

### 4.4 Docker Volumes

Containers are **ephemeral** — data inside them is lost when the container is removed. **Volumes** solve this.

- Volumes are **persistent storage** managed by Docker
- They exist outside the container's lifecycle
- Used for databases, file uploads, logs, etc.

```bash
docker volume create mydata
docker run -v mydata:/var/lib/mysql mysql    # Mount volume to container
docker run -v $(pwd):/app my-app            # Bind mount (local folder)
```

---

### 4.5 Docker Networking

Docker creates isolated networks for containers. By default:

| Network Type | Description                                               |
| ------------ | --------------------------------------------------------- |
| `bridge`     | Default. Containers on same bridge can talk to each other |
| `host`       | Container shares host's network directly                  |
| `none`       | No network access                                         |
| Custom       | Create your own named networks for isolation              |

```bash
docker network create my-network
docker run --network my-network my-app
```

---

### 4.6 Docker Commands Cheat Sheet

```bash
# Images
docker build -t name:tag .       # Build image
docker images                    # List images
docker rmi image-name            # Remove image

# Containers
docker run -d -p 8080:3000 my-app   # Run container in background
docker ps                            # List running containers
docker ps -a                         # List all containers (including stopped)
docker stop container-id             # Stop a container
docker rm container-id               # Remove a container
docker logs container-id             # View logs
docker exec -it container-id bash    # Enter running container

# Cleanup
docker system prune                  # Remove unused stuff
```

**Common `docker run` flags:**

| Flag           | Meaning                                  |
| -------------- | ---------------------------------------- |
| `-d`           | Detached (run in background)             |
| `-p 8080:3000` | Map host port 8080 → container port 3000 |
| `-v`           | Mount a volume                           |
| `--name`       | Give container a name                    |
| `-e KEY=VALUE` | Set environment variable                 |
| `--rm`         | Auto-remove container when it stops      |

---

## 5. Docker Compose

### What is it?

**Docker Compose** is a tool for defining and running **multi-container Docker applications** using a single `docker-compose.yml` file.

Instead of running multiple `docker run` commands manually, you describe all your services, networks, and volumes in one file and start everything with **one command**.

> Docker Compose is perfect for local development and staging environments where you need multiple services (e.g., app + database + cache) to work together.

---

### docker-compose.yml Example

```yaml
version: "3.8"

services:
  web:
    build: . # Build from local Dockerfile
    ports:
      - "8080:3000" # Host:Container port mapping
    environment:
      - NODE_ENV=development
      - DB_HOST=db
    depends_on:
      - db
    volumes:
      - .:/app # Live code reload

  db:
    image: postgres:15 # Use official Postgres image
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data # Persist DB data

  redis:
    image: redis:alpine

volumes:
  pgdata: # Named volume declaration
```

---

### Key Docker Compose Concepts

| Key           | Description                             |
| ------------- | --------------------------------------- |
| `services`    | Each container is defined as a service  |
| `build`       | Build image from a local Dockerfile     |
| `image`       | Use a pre-built image from a registry   |
| `ports`       | Map ports between host and container    |
| `environment` | Set environment variables               |
| `volumes`     | Mount volumes or bind mounts            |
| `depends_on`  | Start order dependency between services |
| `networks`    | Define custom networks for services     |

---

### Docker Compose Commands

```bash
docker compose up           # Start all services
docker compose up -d        # Start in background (detached)
docker compose down         # Stop and remove containers
docker compose down -v      # Also remove volumes
docker compose ps           # List running services
docker compose logs         # View logs of all services
docker compose logs web     # View logs of specific service
docker compose build        # Rebuild images
docker compose exec web sh  # Enter a running service container
docker compose restart      # Restart services
```

---

## 6. Docker Architecture Overview

```
┌─────────────────────────────────────────┐
│              Docker Client              │
│         (docker CLI commands)           │
└──────────────────┬──────────────────────┘
                   │ REST API
┌──────────────────▼──────────────────────┐
│              Docker Daemon              │
│             (dockerd)                   │
│                                         │
│  ┌──────────┐  ┌──────────┐            │
│  │  Images  │  │Containers│            │
│  └──────────┘  └──────────┘            │
│  ┌──────────┐  ┌──────────┐            │
│  │ Volumes  │  │ Networks │            │
│  └──────────┘  └──────────┘            │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│             Docker Registry             │
│           (Docker Hub, ECR)             │
└─────────────────────────────────────────┘
```
