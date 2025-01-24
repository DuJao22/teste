# Shopping List Application

## Project Overview
This is a Flask web application that manages shopping lists for individual users, featuring an admin panel for user management.

## Features
- User registration and login
- Isolated shopping lists for each user
- Admin panel to manage users and their shopping lists
- Responsive design for mobile, tablet, and desktop

## Directory Structure
```
shopping-list-app/
├── app.py                  # Main Flask app
├── templates/              # HTML templates
│   ├── base.html           # Base layout
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── dashboard.html      # User shopping list
│   ├── admin.html          # Admin panel
│
├── static/                 # CSS and static files
│   ├── styles.css          # Main CSS (responsive design)
│
├── database/               # SQLite3 database files
│   ├── shopping_list.db    # Main database
│
├── utils/                  # Helper utilities
│   ├── auth.py             # Authentication logic
│   ├── admin.py            # Admin-specific logic
│
└── README.md               # Project documentation
```

## Setup Instructions
1. Create a virtual environment:
   ```
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
3. Install dependencies:
   ```
   pip install flask bcrypt
   ```

## Running the Application
Start the Flask server:
```
python app.py
```
Access the application locally at `http://localhost:5000`.

## Usage
- **User Registration**: Navigate to the registration page to create a new account.
- **User Login**: Use the login page to access your shopping list.
- **Admin Panel**: Admin can log in with the credentials (Username: DUJAO22, Password: 20e10) to manage users and their shopping lists.

## Extensions (Optional)
- Add categories for shopping list items.
- Enable sharing of lists between users.
- Implement search or filter functionality in the admin panel.