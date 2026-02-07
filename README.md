<div align="center">

# 🎓 ZENVIO Contact Management System

### A Professional Full-Stack CRUD Application

**Built with Python, Django, HTML, CSS & Bootstrap**

---

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

**[Features](#-features) • [Installation](#-installation) • [Usage](#-usage-guide) • [Documentation](#-project-documentation)**

</div>

---

## 📋 About the Project

**ZENVIO** is a comprehensive **Contact Management System** developed as a college project to demonstrate proficiency in **full-stack web development** using modern technologies. This application showcases the complete implementation of **CRUD operations** (Create, Read, Update, Delete) with a professional, responsive user interface.

### Problem Statement

In today's digital age, managing personal and professional contacts efficiently is crucial. Traditional methods lack organization, search capabilities, and data persistence. This project addresses these challenges by providing a centralized, web-based solution for contact management.

### Solution

A full-featured web application that allows users to:
- Create and manage contact profiles with detailed information
- Search and filter contacts efficiently
- Import multiple contacts via CSV files
- Secure user authentication and data isolation
- Responsive design for all devices

---

## 💻 Technology Stack

This project demonstrates expertise in both **frontend** and **backend** technologies:

### Frontend Technologies
- **HTML5** - Modern semantic markup for structured content
- **CSS3** - Custom styling with flexbox and grid layouts
- **Bootstrap 5** - Responsive framework for mobile-first design
- **JavaScript** - Dynamic interactions and form validations

### Backend Technologies
- **Python 3.9+** - Core programming language
- **Django 5.0** - High-level web framework following MVT architecture
- **SQLite** - Development database
- **Django ORM** - Object-Relational Mapping for database operations

### Additional Tools & Libraries
- **Django Crispy Forms** - Beautiful form rendering
- **Bootstrap 5 Template Pack** - Enhanced form styling
- **Python Decouple** - Environment configuration management
- **Gunicorn** - Production WSGI server
- **WhiteNoise** - Static file serving

---

## ✨ Features

### Core CRUD Operations

#### 🟢 CREATE - Add New Contacts
- User-friendly form with validation
- Fields: Name, Email, Phone, Company, Address, Notes
- Real-time client-side validation
- Server-side data validation
- Success/error feedback messages

#### 🔵 READ - View & Search Contacts
- **Contact List View**
  - Paginated display of all contacts
  - Search functionality by name, email, or phone
  - Filter by company
  - Sort by name or date added
- **Contact Detail View**
  - Complete contact information display
  - Clean, card-based layout
  - Quick action buttons (Edit, Delete)

#### 🟡 UPDATE - Edit Contact Information
- Pre-filled forms with existing data
- All fields editable
- Data validation on update
- Confirmation messages
- Preserves creation timestamp

#### 🔴 DELETE - Remove Contacts
- Confirmation dialog before deletion
- Soft delete option (can be implemented)
- Success notification
- Immediate UI update

### Additional Features

#### 📤 CSV Import
- Bulk contact import from CSV files
- Automatic field mapping
- Validation of required fields (Name, Phone)
- Skip invalid entries with detailed report
- Import summary with success/failure count

#### 🔐 User Authentication
- Secure user registration
- Login/Logout functionality
- Password hashing and validation
- Session management
- User-specific contact isolation

#### 📊 Dashboard
- Total contacts count
- Recent contacts (last 7 days)
- Company grouping statistics
- Quick access to all features

#### 🎨 Responsive Design
- Mobile-first approach
- Works on all screen sizes
- Bootstrap grid system
- Touch-friendly interface
- Modern UI/UX design

---

## 🏗️ System Architecture

### MVT (Model-View-Template) Pattern

```
┌─────────────────────────────────────────────────┐
│                   User Browser                   │
│              (HTML, CSS, Bootstrap)              │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│                Django Framework                  │
│  ┌─────────────────────────────────────────┐   │
│  │           URLs (Routing)                 │   │
│  └──────────────────┬──────────────────────┘   │
│                     │                            │
│  ┌──────────────────▼──────────────────────┐   │
│  │         Views (Business Logic)           │   │
│  │  - Create Contact                        │   │
│  │  - Read Contact List                     │   │
│  │  - Update Contact                        │   │
│  │  - Delete Contact                        │   │
│  └──────────┬──────────────┬────────────────┘   │
│             │              │                     │
│  ┌──────────▼──────┐  ┌───▼──────────────────┐ │
│  │   Models        │  │   Templates           │ │
│  │  - Contact      │  │  - contact_list.html  │ │
│  │  - User         │  │  - contact_form.html  │ │
│  │                 │  │  - contact_detail.html│ │
│  └────────┬────────┘  └───────────────────────┘ │
└───────────┼──────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────┐
│              Database (SQLite)                   │
│  - Users Table                                   │
│  - Contacts Table                                │
└─────────────────────────────────────────────────┘
```

### Database Schema

**Contacts Table:**
- `id` - Primary Key (auto-increment)
- `user_id` - Foreign Key to User
- `name` - VARCHAR (required)
- `email` - VARCHAR (unique, optional)
- `phone` - VARCHAR (required)
- `company` - VARCHAR (optional)
- `address` - TEXT (optional)
- `notes` - TEXT (optional)
- `created_at` - DATETIME (auto)
- `updated_at` - DATETIME (auto)

---

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git (for cloning)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hashmessi/contact-management-.git
   cd contact-management-
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables** (Optional)
   
   Create `.env` file:
   ```bash
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser** (Optional - for admin panel)
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - Homepage: `http://localhost:8000`
   - Admin Panel: `http://localhost:8000/admin`

---

## 📱 Usage Guide

### User Registration & Login

1. Navigate to homepage
2. Click "Register" to create new account
3. Fill in username, email, and password
4. Login with credentials

### Performing CRUD Operations

#### Creating a Contact
1. Click "Add Contact" button
2. Fill in contact details:
   - Name (required)
   - Email (optional)
   - Phone (required)
   - Company (optional)
   - Address (optional)
   - Notes (optional)
3. Click "Save Contact"

#### Reading/Viewing Contacts
1. View all contacts in the contact list
2. Use search bar to find specific contacts
3. Click on any contact to view details

#### Updating a Contact
1. Click on contact to view details
2. Click "Edit" button
3. Modify desired fields
4. Click "Update Contact"

#### Deleting a Contact
1. Click on contact to view details
2. Click "Delete" button
3. Confirm deletion in popup
4. Contact removed from database

### CSV Import

1. Prepare CSV file with headers: `Name,Email,Phone,Company,Address,Notes`
2. Click "Import CSV" button
3. Select your CSV file
4. Review import summary
5. Imported contacts appear in list

---

## 📁 Project Structure

```
contact-management-/
│
├── accounts/                 # User authentication app
│   ├── models.py            # Custom User model
│   ├── views.py             # Login, Register, Logout views
│   ├── forms.py             # Registration and login forms
│   └── urls.py              # Authentication URL patterns
│
├── contacts/                # Main contact management app
│   ├── models.py            # Contact model definition
│   ├── views.py             # CRUD operation views
│   ├── forms.py             # Contact form with validation
│   ├── urls.py              # Contact URL patterns
│   └── admin.py             # Admin panel configuration
│
├── static/                  # Static files
│   ├── css/
│   │   └── styles.css       # Custom CSS styling
│   └── js/                  # JavaScript files
│
├── templates/               # HTML templates
│   ├── base.html            # Base template with Bootstrap
│   ├── home.html            # Landing page
│   ├── accounts/
│   │   ├── login.html       # Login page
│   │   └── register.html    # Registration page
│   └── contacts/
│       ├── contact_list.html    # List view (READ)
│       ├── contact_form.html    # Add/Edit form (CREATE/UPDATE)
│       ├── contact_detail.html  # Detail view (READ)
│       └── contact_import.html  # CSV import page
│
├── zenvio/                  # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
│
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── vercel.json              # Deployment configuration
```

---

## 🎓 Learning Outcomes

### Technical Skills Demonstrated

1. **Backend Development**
   - Django framework fundamentals
   - MVT architecture implementation
   - ORM for database operations
   - User authentication and authorization
   - Form handling and validation
   - File upload and processing

2. **Frontend Development**
   - Semantic HTML5 structure
   - Responsive CSS3 layouts
   - Bootstrap framework integration
   - JavaScript for interactivity
   - Mobile-first design principles

3. **Database Management**
   - Schema design and relationships
   - CRUD operations implementation
   - Data validation and constraints
   - Query optimization

4. **Software Engineering**
   - MVC/MVT design pattern
   - Code organization and modularity
   - Version control with Git
   - Environment configuration
   - Deployment preparation

### Challenges Overcome

- **User Data Isolation**: Implementing user-specific contact filtering
- **Form Validation**: Both client and server-side validation
- **File Handling**: CSV parsing and batch import
- **Responsive Design**: Ensuring mobile compatibility
- **Security**: Password hashing and CSRF protection

---

## 🚀 Future Enhancements

- [ ] **Advanced Search**: Filter by multiple criteria simultaneously
- [ ] **Contact Groups/Tags**: Organize contacts with custom categories
- [ ] **Export Functionality**: Export contacts to CSV/PDF
- [ ] **Contact Photos**: Upload and display profile pictures
- [ ] **Email Integration**: Send emails directly from the app
- [ ] **Activity Logs**: Track all contact interactions
- [ ] **API Development**: RESTful API for mobile apps
- [ ] **PostgreSQL Migration**: For production scalability
- [ ] **Cloud Storage**: S3 integration for file uploads
- [ ] **Advanced Analytics**: Contact statistics and insights

---

## 📸 Screenshots

<div align="center">

### Dashboard
![Dashboard](https://via.placeholder.com/800x400/6366f1/ffffff?text=Dashboard+View)

### Contact List (READ Operation)
![Contact List](https://via.placeholder.com/800x400/10b981/ffffff?text=Contact+List+View)

### Add Contact (CREATE Operation)
![Add Contact](https://via.placeholder.com/800x400/f59e0b/ffffff?text=Add+Contact+Form)

### Contact Details (READ Operation)
![Contact Details](https://via.placeholder.com/800x400/3b82f6/ffffff?text=Contact+Details)

</div>

---

## 🌐 Deployment

### Production Deployment on Vercel

This application is ready for deployment on Vercel with:
- Automated build process
- Static file serving via WhiteNoise
- Production-ready configurations
- Environment variable management

**Quick Deploy**: See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 📚 Project Documentation

- **[README.md](README.md)** - This file, complete project overview
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Detailed deployment instructions
- **[QUICKSTART.md](QUICKSTART.md)** - Quick 5-minute setup guide
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Development summary

---

## 👨‍💻 Author

**Project Developer**: College Project Submission

**Course**: Web Development / Full Stack Development

**Academic Year**: 2025-2026

---

## 🙏 Acknowledgments

- **Django Documentation** - Comprehensive framework guide
- **Bootstrap Team** - Excellent CSS framework
- **Python Community** - Extensive libraries and support
- **Stack Overflow** - Problem-solving assistance
- **GitHub** - Version control and collaboration

---

## 📄 License

This project is developed for educational purposes as part of college coursework.

---

## 📧 Contact & Support

For questions, suggestions, or issues:
- Open an issue on GitHub
- Contact through college email

---

<div align="center">

### ⭐ Key Highlights

**✅ Complete CRUD Implementation** | **✅ Responsive Design** | **✅ Secure Authentication**

**✅ Modern Tech Stack** | **✅ Production Ready** | **✅ Well Documented**

---

**Built with ❤️ using Python & Django**

*A demonstration of full-stack web development skills*

</div>
