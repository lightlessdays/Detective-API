
# Django Detective API

Welcome to the Django Detective API project! This basic Django project allows you to retrieve and display the names and locations of detectives. Follow the instructions below to get the API up and running on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (3.6 or higher)
- Django (3.0 or higher)
- Django REST framework (3.12 or higher)

## Getting Started

1. **Clone the Repository:**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/lightlessdays/Detective-API
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project folder:

   ```bash
   cd Detective-API
   ```

3. **Set Up a Virtual Environment (Optional but Recommended):**

   It's good practice to use a virtual environment to isolate your project's dependencies. You can create and activate a virtual environment using Python's `venv` module (if not already installed):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Dependencies:**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations:**

   Apply the database migrations to create the necessary database tables:

   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (Optional):**

   If you want to access the Django admin interface, create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up your admin account.

7. **Run the Development Server:**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at [http://localhost:8000](http://localhost:8000). You can access the Django admin interface (if you created a superuser) at [http://localhost:8000/admin](http://localhost:8000/admin).

## Using the API

You can use a tool like [curl](https://curl.se/) or [Postman](https://www.postman.com/) to interact with the API, or you can use a web browser.

- To retrieve the list of detectives, make a GET request to: [http://localhost:8000/api/detectives/](http://localhost:8000/api/detectives/)

- To create a new detective, make a POST request to the same URL with the detective's name and location in the request body as JSON.

- To view, edit, or delete a specific detective, use the appropriate API endpoints and methods (GET, PUT, DELETE) with the detective's ID.

## API Endpoints

- List Detectives: `GET /api/detectives/`
- Create Detective: `POST /api/detectives/`
- Retrieve Detective: `GET /api/detectives/{id}/`
- Update Detective: `PUT /api/detectives/{id}/`
- Delete Detective: `DELETE /api/detectives/{id}/`

## Authentication (Optional)

By default, the API does not require authentication for read-only operations. However, you can configure authentication using Django REST framework's authentication classes for more advanced use cases.

## Conclusion

You've successfully set up and run the Django Detective API project on your local machine. Feel free to explore and modify the code to suit your needs. If you have any questions or encounter any issues, please refer to the Django documentation or seek help in the Django community. Happy coding!
