# Keep-Notes

A Django-based note-taking web application that allows users to create, manage, and organize their personal notes securely.

## Features

- **User Authentication**: Secure registration and login system
- **Create Notes**: Add new notes with title and description
- **Edit Notes**: Update existing notes anytime
- **Delete Notes**: Remove notes you no longer need
- **Search Functionality**: Search through your notes by title or description
- **Account Settings**: Update your profile information (username, first name, last name)
- **Pagination**: View notes in organized pages (6 notes per page)
- **User Privacy**: Each user can only view and manage their own notes

## Tech Stack

- **Backend**: Django
- **Database**: SQLite3 (MySQL support available)
- **Frontend**: HTML, CSS, JS, Bootstrap
- **Forms**: Django Crispy Forms with Bootstrap 4
- **Authentication**: Django's built-in authentication system


## Usage

1. **Register**: Create a new account by clicking on the register link
2. **Login**: Sign in with your credentials
3. **Create Notes**: Use the form on the home page to add new notes
4. **View Notes**: All your notes are displayed on the home page with pagination
5. **Search**: Use the search functionality to find specific notes
6. **Edit**: Click on a note to update its content
7. **Delete**: Remove notes you no longer need
8. **Settings**: Update your account information from the settings page
9. **Logout**: Sign out when you're done

## Project Structure

```
Keep-Notes/
├── keepproject/              # Main project directory
│   ├── keepproject/          # Django project settings
│   │   ├── settings.py       # Project configuration
│   │   ├── urls.py          # Main URL configuration
│   │   └── wsgi.py          # WSGI configuration
│   ├── notes/                # Notes application
│   │   ├── models.py        # Note model definition
│   │   ├── views.py         # View functions
│   │   ├── forms.py         # Form definitions
│   │   ├── urls.py          # App URL patterns
│   │   └── admin.py         # Admin configuration
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── home.html
│   │   ├── update.html
│   │   ├── settings.html
│   │   └── loggedout.html
│   ├── static/              # Static files (CSS, JS)
│   │   ├── css/
│   │   └── js/
│   ├── db.sqlite3           # SQLite database
│   ├── manage.py            # Django management script
│   └── requirements.txt     # Python dependencies
├── venv/                    # Virtual environment
└── README.md                # This file
```

## Key Features Explained

### Note Model
- **Title**: Character field (max 45 characters)
- **Description**: Text field for note content
- **Author**: Foreign key linking to User model

### Security
- All note-related views require user authentication (`@login_required` decorator)
- Users can only access their own notes (filtered by `author=request.user`)
- CSRF protection enabled for all forms

