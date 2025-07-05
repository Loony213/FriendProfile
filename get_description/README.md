
# Get Description Microservice Overview 🧑‍🤝‍🧑

The **get_description** microservice is a part of the **FriendProfile** domain, providing the functionality to retrieve the profile description of a user's friend. It allows users to access a friend's description, which could include information such as a bio, interests, and other personal details.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/FriendProfile)

## Purpose 🎯
The **get_description** microservice is designed to fetch the description of a friend's profile based on their email. This service enables users to access specific details about their friends, which can be used for display purposes in the application.

## Architecture Style 🏗️
- **Microservice Architecture**: The service operates independently as a microservice, responsible solely for retrieving the profile description of a user's friend.
- **Design Pattern**: The service uses the **Request-Response** design pattern, where the client sends a request with the friend's email and receives the description as a response.

## Technologies 💻
- **Programming Language**: Python
- **Framework**: Flask (used for the web server)
- **Containerization**: Docker for deploying the service in a containerized environment
- **Database**: SQL Server (used for storing user profiles)

## Project Structure 🧑‍💻
The repository is structured as follows:

```
get_description/
├── app/
│   ├── controllers/
│   │   └── description_controller.py      # Handles incoming requests and calls the service to fetch the description.
│   ├── routes/
│   │   └── description_routes.py          # Defines the routes for the service.
│   ├── services/
│   │   └── description_service.py         # Contains the logic for retrieving the description from the database.
│   └── utils/
│       └── db.py                          # Database utility for connecting to the SQL Server.
│       └── __init__.py                    # Initializes the application.
├── app.py                                  # The entry point for the application.
├── Dockerfile                              # Dockerfile for containerizing the service.
└── requirements.txt                        # Lists the dependencies for the service.
```

### Folder Descriptions 📂
- **app/controllers/**: Contains the controller logic for processing the request related to retrieving a friend's description. It validates the request and calls the appropriate service.
- **app/routes/**: Defines the route for the `/get-description` endpoint, where users can request a friend's description.
- **app/services/**: Contains the core service logic for fetching a friend's description from the database.
- **app/utils/**: Includes utilities such as database connection logic for interacting with the database.
- **requirements.txt**: Specifies the dependencies needed to run the service, such as Flask and SQL Server libraries.
- **Dockerfile**: Defines the configuration for containerizing the application using Docker, making it easy to deploy and scale the service.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/FriendProfile.git
   ```

2. **Install Dependencies:**
   Navigate to the `get_description/` folder and install the required dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Service:**
   Run the Flask application locally:
   ```bash
   python app.py
   ```

4. **Docker Deployment:**
   - Build the Docker image for the service:
     ```bash
     docker build -t kamartinez/get-description .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 kamartinez/get-description
     ```

5. **Access the Service:**
   The service will be accessible at `http://localhost:5000`.

## Features ✨
- **Get Description**: Allows users to fetch a friend's profile description using their email.
- **Modular and Scalable**: The service is designed to be independent, easily scalable, and can be deployed as part of the overall **FriendProfile** system.
- **Containerization**: The service is containerized using Docker, making it easy to deploy and scale.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
