
# FriendProfile Microservices 🧑‍🤝‍🧑

The **FriendProfile** repository is part of the larger **Friends Service** domain, and it provides microservices for fetching profile data for a user's friends. These services allow users to access specific details about their friends, such as their profile description and name.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/FriendProfile)

## Microservices Overview 🚀
### 1. **Get Description**
   - Purpose: Fetches the description of a user's friend profile. This service allows users to access information about their friends, such as bio or personal details.

### 2. **Get Name**
   - Purpose: Retrieves the name of a user's friend. This service is designed to return the name associated with a specific friend's profile.

## Architecture Style 🏗️
- **Microservice Architecture**: Each service operates independently and is designed to handle specific aspects of profile retrieval, ensuring scalability and modularity.
- **Design Pattern**: The system uses a **Request-Response** design pattern, where each request from the user triggers a corresponding response with the requested profile data.

## Technologies 💻
- **Programming Language**: Python
- **API Integration**: REST APIs to fetch the friend's details.
- **Containerization**: Docker (optional for deployment)

## Project Structure 🧑‍💻
The repository is structured as follows:

```
FriendProfile/
├── .github/workflows/         # GitHub Actions workflows for CI/CD automation.
│   └── new.yml                # Configuration for CI/CD pipelines.
│
├── get_description/           # Microservice for retrieving friend's profile description.
│   └── requirements.txt       # Lists dependencies for the get_description service.
│
├── get_name/                  # Microservice for retrieving friend's name.
│   └── requirements.txt       # Lists dependencies for the get_name service.
│
├── README.md                  # This file.
└── requirements.txt           # Lists the global dependencies for the project.
```

### Folder Descriptions 📂
- **.github/workflows/**: Contains GitHub Actions configurations for CI/CD automation.
- **get_description/**: The microservice that retrieves a friend's profile description.
- **get_name/**: The microservice that retrieves a friend's name.
- **requirements.txt**: Specifies the dependencies necessary for the microservices to function.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/FriendProfile.git
   ```

2. **Install Dependencies:**
   Navigate to each service folder (e.g., `get_description/`, `get_name/`) and install the dependencies listed in their `requirements.txt`.

3. **Run the Microservices:**
   - After setting up the dependencies, you can start each microservice individually.
   - Example for running `get_description` service:
     ```bash
     python app.py
     ```

4. **Docker Deployment:**
   - Build the Docker image for each microservice:
     ```bash
     docker build -t kamartinez/get_description .
     docker build -t kamartinez/get_name .
     ```
   - Run the containers:
     ```bash
     docker run -p 5000:5000 kamartinez/get_description
     docker run -p 5001:5000 kamartinez/get_name
     ```

5. **Access the Services:**
   - The services will be accessible at `http://localhost:5000` and `http://localhost:5001` (or different ports depending on your configuration).

## Features ✨
- **Get Description**: Retrieves the description of a user's friend profile.
- **Get Name**: Retrieves the name of a user's friend profile.
- **Modular and Scalable**: The services are modular, allowing easy scalability and integration with other systems.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
