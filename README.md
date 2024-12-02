# Highlander Hub

Welcome to **Highlander Hub**, a social media platform designed to unite UC Riverside Highlanders! This project is in its early stages, providing the foundation for a localized social media experience to foster community and connection within UCR. Built with Django, Highlander Hub is simple to set up and offers room for future growth.

---

## Features

### 🌟 Current Features
- **User Authentication**: Secure login and registration system.
- **Profile Creation**: Create and view profiles for users.
- **Post Sharing**: Create posts to share updates with the community.
- **Dynamic Feed**: View all shared posts in a central feed.

### 🔧 Planned Features
- **Likes and Comments**: Interact with posts through likes and comments.
- **Follow System**: Follow other users to see their updates on your feed.
- **Notifications**: Get alerts for interactions like likes, comments, and follows.
- **Direct Messaging**: Private chat system for one-on-one conversations.
- **Event Board**: Discover and share events happening at UCR.
- **Group Discussions**: Join or create groups based on shared interests.
- **Dark Mode**: Toggle between light and dark themes for a personalized experience.

---

## Prerequisites

- **Python 3.8+**
- **Django 4.x**
- **Virtual Environment** (recommended for isolated development)

---

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/highlander-hub.git
cd highlander-hub
```

### Step 2: Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Configure the Database
```bash
python manage.py migrate
```

### Step 5: Run the Development Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
```bash
http://127.0.0.1:8000/
```

## Usage

1. **Register**: Create an account to get started.
2. **Create Posts**: Share updates by clicking the “Create Post” button.
3. **Explore the Feed**: View posts from other users in the shared feed.

---

## Development

### Creating a Superuser

To access the Django admin panel:

```bash
python manage.py createsuperuser
```
Visit the admin panel at:
```bash
http://127.0.0.1:8000/admin
```