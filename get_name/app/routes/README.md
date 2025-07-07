
# Routes Folder Overview 🌐

The **routes** folder contains the routing logic for the application. The `name_routes.py` file specifically handles the routing related to retrieving a user's friend name. It acts as the point of entry for the request and directs the flow to the appropriate controller for processing.

## Purpose 🎯
The **name_routes.py** file defines the routes of the microservice. It sets up the URL endpoint `/get-name` and associates it with the **name_controller** function, which handles the logic for retrieving a friend's name.

The routes are crucial for setting up the web service and ensuring that incoming HTTP requests are directed to the appropriate functionality for processing.

## Functionality 🔧
- **Blueprint Definition**: The routes are encapsulated within a Flask `Blueprint`. This allows the routes to be modular and reusable across different parts of the application.
- **Request Handling**: It listens for GET requests at the `/get-name` endpoint, directing these requests to the `get_name` controller.
- **Integration with Controller**: The controller (`name_controller.py`) is responsible for the logic that fetches the friend's name.

This routing mechanism ensures that all requests for retrieving a friend's name are properly directed and processed, maintaining a clean separation between routing, controllers, and services.

## Features ✨
- **Modular Routing**: The routes are managed in a Flask `Blueprint`, making it easy to add or remove routes without affecting other parts of the application.
- **Integration with Controllers**: Directly connects the route to the controller function (`get_name`), ensuring that the correct logic is executed for each request.
- **Simple Route Management**: Handles the GET request for the `/get-name` endpoint and integrates seamlessly with the rest of the application.

The **name_routes.py** file is an essential part of the application, ensuring that HTTP requests are correctly routed to the appropriate controller for processing in the **FriendProfile** domain.
