
# Get Name Microservice Overview 🧑‍🤝‍🧑

The **get_name** microservice is part of the **FriendProfile** domain and provides the functionality to retrieve the name of a user's friend based on their profile information. This microservice is essential for fetching the name associated with a particular friend's profile, making it easier for users to access the basic information of their connections.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/FriendProfile)

## Purpose 🎯
The **get_name** microservice is designed to allow users to request the name of a specific friend from their profile. This service provides a simple and efficient way to retrieve this piece of information for integration into larger social features or for display in user interfaces.

## Architecture Style 🏗️
- **Microservice Architecture**: The service is structured as a standalone microservice, responsible for only retrieving the name of a user's friend.
- **Design Pattern**: The service follows the **Request-Response** pattern, where the client sends a request, and the microservice responds with the friend's name.

## Technologies 💻
- **Programming Language**: Python
- **Framework**: FastAPI for creating the API endpoints
- **Database**: SQL or other storage methods for retrieving the friend's data (not shown here but assumed in real implementation)
- **Containerization**: Docker for deployment
- **Testing**: Unit tests can be added to ensure the service works as expected

## Project Structure 🧑‍💻
The repository is structured as follows:

```
get_name/
├── app/
│   ├── controllers/
│   │   └── name_controller.py     # Handles the logic for API requests related to friend names.
│   ├── routes/
│   │   └── name_routes.py         # Defines the routes for the service.
│   ├── services/
│   │   └── name_service.py        # Contains the service logic for retrieving the name.
│   └── utils/
│       └── db.py                  # Database connection utility for the service.
│       └── __init__.py            # Initializes the app and database.
├── app.py                         # The entry point for the application.
├── Dockerfile                     # Dockerfile for containerizing the service.
└── requirements.txt               # Lists the dependencies for the service.
```

### Folder Descriptions 📂
- **app/controllers/**: Contains the controller logic for managing the API requests related to the name retrieval. It ensures that the incoming requests are processed correctly and that the response is generated based on the service layer.
- **app/routes/**: Defines the route for the API endpoint, providing the endpoint for fetching the friend's name.
- **app/services/**: Contains the core logic of the service, specifically retrieving the friend's name from the database or any other underlying storage mechanism.
- **app/utils/**: Includes utilities like the database connection, which the service utilizes to interact with the data storage.
- **requirements.txt**: Specifies the dependencies needed to run the service, such as FastAPI and any database libraries.
- **Dockerfile**: Defines the configuration for containerizing the application using Docker, making it easy to deploy and scale the service.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/FriendProfile.git
   ```

2. **Install Dependencies:**
   Navigate to the `get_name/` folder and install the required dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Service:**
   Run the FastAPI application locally:
   ```bash
   uvicorn app:app --reload
   ```

4. **Docker Deployment:**
   - Build the Docker image for the service:
     ```bash
     docker build -t kamartinez/get-name .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 kamartinez/get-name
     ```

5. **Access the Service:**
   The service will be accessible at `http://localhost:5000`.

## Features ✨
- **Get Name**: Allows users to fetch the name of a specific friend from their profile.
- **Modular and Scalable**: The service is designed to be independent and can easily be scaled or modified as part of the overall **FriendProfile** system.
- **Containerization**: The service is ready to be deployed in Docker containers for easier management and scalability.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
