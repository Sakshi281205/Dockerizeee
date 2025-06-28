# 🐳 Dockerized Flask Application

A modern Flask web application containerized with Docker, featuring a beautiful UI and RESTful API endpoints.

## 🚀 Features

- **Modern Flask Application** with RESTful API
- **Beautiful Responsive UI** with gradient design
- **Docker Containerization** with optimized settings
- **Health Check Endpoints** for monitoring
- **Security Best Practices** (non-root user, minimal base image)
- **Production Ready** configuration

## 📋 Prerequisites

- Docker installed on your system
- Git (for cloning the repository)

## 🛠️ Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Dockerizeee
```

### 2. Build the Docker Image
```bash
docker build -t flask-app .
```

### 3. Run the Container
```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

### 4. Access the Application
Open your browser and navigate to: **http://localhost:5000**

## 🔧 Available Commands

### Build the Image
```bash
# Build with default tag
docker build -t flask-app .

# Build with custom tag
docker build -t my-flask-app:v1.0 .
```

### Run the Container
```bash
# Run in detached mode (background)
docker run -d -p 5000:5000 --name flask-container flask-app

# Run in interactive mode (see logs)
docker run -it -p 5000:5000 --name flask-container flask-app

# Run with custom port mapping
docker run -d -p 8080:5000 --name flask-container flask-app
```

### Container Management
```bash
# View running containers
docker ps

# View container logs
docker logs flask-container

# Stop the container
docker stop flask-container

# Remove the container
docker rm flask-container

# Remove the image
docker rmi flask-app
```

### Health Check
```bash
# Check container health
docker inspect flask-container | grep Health -A 10

# Test health endpoint directly
curl http://localhost:5000/api/health
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main application page |
| GET | `/api/health` | Health check endpoint |
| GET | `/api/info` | Application information |
| POST | `/api/echo` | Echo back JSON data |

### Example API Usage

```bash
# Health check
curl http://localhost:5000/api/health

# Get app info
curl http://localhost:5000/api/info

# Echo data
curl -X POST http://localhost:5000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello World"}'
```

## 📁 Project Structure

```
Dockerizeee/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
├── templates/
│   └── index.html        # Main HTML template
└── README.md             # This file
```

## 🔒 Security Features

- **Non-root user**: Application runs as `appuser` instead of root
- **Minimal base image**: Uses Python slim image to reduce attack surface
- **Health checks**: Built-in health monitoring
- **Environment isolation**: Proper environment variable configuration

## 🐛 Troubleshooting

### Container won't start
```bash
# Check container logs
docker logs flask-container

# Check if port is already in use
netstat -tulpn | grep 5000
```

### Permission issues
```bash
# If you encounter permission issues, ensure Docker has proper permissions
sudo usermod -aG docker $USER
```

### Port conflicts
```bash
# Use a different port
docker run -d -p 8080:5000 --name flask-container flask-app
```

## 📸 Screenshot Instructions

To capture a screenshot of the working container:

1. **Start the container** using the commands above
2. **Open your browser** and go to `http://localhost:5000`
3. **Take a screenshot** of the beautiful UI showing:
   - The main page with the gradient background
   - The API endpoints section
   - Test the buttons to show the interactive features

### Video Recording (Optional)
For a video demonstration:
1. Record the process of building and running the container
2. Show the application loading in the browser
3. Demonstrate the API endpoints working
4. Show the container logs and health checks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Dockerizing! 🐳**