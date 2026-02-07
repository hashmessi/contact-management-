# Quick Start Guide

## 🎯 Get Started in 5 Minutes

### For Local Development

1. **Clone and Setup**
   ```bash
   git clone https://github.com/hashmessi/contact-management-.git
   cd contact-management-
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Run Migrations and Server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. **Access**
   - Homepage: http://localhost:8000
   - Create an account and start managing contacts!

### For Production (Vercel)

1. **One-Click Deploy**
   - Fork the repository on GitHub
   - Go to https://vercel.com/new
   - Import your forked repository
   - Add environment variables:
     - `SECRET_KEY` = (generate a secure key)
     - `DEBUG` = False
     - `ALLOWED_HOSTS` = .vercel.app
   - Click Deploy!

2. **Done!**
   - Your app is live at `https://your-project.vercel.app`

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed information
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment details
- Explore the features and start adding contacts!

---

**Happy coding! 💻**
