# TuneTrove

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)

## Introduction
TuneTrove is a music recommendation web app that provides personalized music recommendations to users based on their listening history. The app uses content-based filtering and cosine similarity for its recommendation algorithm, and it fetches music data from the Spotify API using Spotipy.

## Features
- User authentication and registration
- Fetch music data from Spotify API
- Personalized music recommendations using content-based filtering and cosine similarity
- Interactive and appealing user interface

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask, SQLAlchemy, MySQL
- **API Integration:** Spotify API using Spotipy
- **Authentication:** Flask-Login, Flask-Bcrypt

## Architecture
The application is structured into different modules for better maintainability and scalability:
- **app/__init__.py:** Application factory and initialization.
- **app/config.py:** Configuration settings.
- **app/models.py:** Database models.
- **app/auth.py:** Authentication routes.
- **app/routes.py:** Main application routes.
- **app/recommendations.py:** Recommendation logic.
- **templates/**: HTML templates.
- **static/**: CSS and JavaScript files.

## License
- This project is sponsored under the MIT License.

## Contributors
- Mukeli Kavivya

## Acknowledgments
- Thanks to Spotify for their awesome API.
- Thanks to Flask for being a great web framework.

