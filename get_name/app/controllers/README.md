
# Name Controller Overview 🎮

The **controllers** folder contains the logic for handling incoming HTTP requests and returning the appropriate responses. The `name_controller.py` file specifically handles requests related to retrieving a user's friend name.

## Purpose 🎯
The **name_controller.py** is responsible for receiving HTTP requests to fetch the name of a friend based on their email. It acts as the intermediary between the user and the service layer, forwarding the request to the **name_service** for processing and returning the response to the user.

This controller ensures that requests for retrieving a friend's name are handled correctly, and if the necessary data is found, it sends the appropriate response back.

## Functionality 🔧
- **Request Handling**: The controller listens for GET requests on the `/get_name` endpoint, expecting an email query parameter.
- **Validation**: It checks if the email parameter is provided. If not, it returns a `400` status code with an error message.
- **Service Interaction**: Once the email is validated, the controller calls the `fetch_name` function from the **name_service** to retrieve the friend's name.
- **Response Handling**: Based on the result from the service, the controller returns either the name in a `200 OK` response or an error message in case the user is not found.

This controller ensures that requests related to the name retrieval are handled efficiently and that the response is structured appropriately.

## Features ✨
- **Request Validation**: Ensures that the email parameter is present in the request, returning a `400` error if missing.
- **Integration with Name Service**: Forwards the request to the **name_service** to handle the business logic of fetching the friend's name.
- **Response Structuring**: Returns structured JSON responses, including error handling and success cases.

The **name_controller.py** file is an essential component of the application, ensuring smooth and validated interactions between the user and the service layer when retrieving a friend's name.
