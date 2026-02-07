# ZENVIO Contact Management System

Organize, track, and connect with your contacts in one beautiful, intuitive platform.

## 🌟 Features

- **User Authentication** - Secure registration and login system
- **Contact Management** - Create, read, update, and delete contacts
- **CSV Import** - Bulk import contacts from CSV files
- **Search & Filter** - Quickly find contacts with advanced search
- **Responsive Design** - Beautiful UI that works on all devices
- **User Dashboard** - Track your contact statistics
- **Company Grouping** - Organize contacts by company

## 🚀 Tech Stack

- **Backend**: Django 5.0
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (Development) / PostgreSQL (Production Ready)
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Deployment**: Vercel-ready with Gunicorn & WhiteNoise

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/hashmessi/contact-management-.git
   cd contact-management-
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file** (optional for local development)
   ```bash
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## 🌐 Deployment on Vercel

### Quick Deploy

1. **Fork or clone this repository**

2. **Install Vercel CLI** (optional)
   ```bash
   npm install -g vercel
   ```

3. **Deploy to Vercel**
   - Visit [Vercel](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`

4. **Set Environment Variables** in Vercel Dashboard
   ```
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=.vercel.app
   ```

5. **Deploy!**
   - Vercel will automatically build and deploy
   - Your app will be live at `https://your-project.vercel.app`

### Environment Variables (Production)

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for security | `django-insecure-...` |
| `DEBUG` | Debug mode (should be False) | `False` |
| `ALLOWED_HOSTS` | Allowed hosts for Django | `.vercel.app` |

### Post-Deployment

After first deployment, you may need to:
1. Run migrations (automatically handled by `build_files.sh`)
2. Create a superuser for admin access
3. Test all features thoroughly

## 📁 Project Structure

```
contact-management-/
├── accounts/           # User authentication app
├── contacts/           # Contact management app
├── static/            # Static files (CSS, JS)
├── templates/         # HTML templates
├── zenvio/            # Main project settings
├── build_files.sh     # Vercel build script
├── vercel.json        # Vercel configuration
├── requirements.txt   # Python dependencies
└── manage.py          # Django management script
```

## 🎨 Features in Detail

### Contact Management
- Add new contacts with name, email, phone, company, and notes
- Edit existing contacts
- Delete contacts with confirmation
- View detailed contact information

### CSV Import
- Import multiple contacts at once
- Automatic validation of required fields
- Skip invalid entries with detailed feedback

### User Dashboard
- Total contacts count
- Recent contacts (last 7 days)
- Company/group statistics
- Quick access to key features

## 🔒 Security Features

- Secure user authentication
- Password hashing and validation
- CSRF protection
- Environment-based configuration
- Production-ready security settings

## 🛠️ Development

### Running Tests
```bash
python manage.py test
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using Django**
