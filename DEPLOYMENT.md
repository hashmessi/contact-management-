# ZENVIO - Vercel Deployment Guide

## 🚀 Quick Deployment Steps

### 1. Prerequisites
- GitHub account with the repository pushed
- Vercel account (sign up at https://vercel.com)

### 2. Deploy to Vercel

#### Option A: Using Vercel Dashboard (Recommended)

1. **Go to Vercel Dashboard**
   - Visit https://vercel.com/dashboard
   - Click "Add New..." → "Project"

2. **Import Repository**
   - Select "Import Git Repository"
   - Choose your GitHub account
   - Select `hashmessi/contact-management-` repository
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: (leave empty, handled by vercel.json)
   - **Output Directory**: (leave empty)

4. **Set Environment Variables**
   Click "Environment Variables" and add:
   
   ```
   SECRET_KEY = django-insecure-CHANGE-THIS-TO-A-SECURE-RANDOM-STRING
   DEBUG = False
   ALLOWED_HOSTS = .vercel.app
   ```

   **⚠️ Important**: Generate a secure SECRET_KEY using:
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (2-5 minutes)
   - Your app will be live at `https://your-project-name.vercel.app`

#### Option B: Using Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   cd "f:\contact management pj"
   vercel
   ```

4. **Set Environment Variables**
   ```bash
   vercel env add SECRET_KEY
   vercel env add DEBUG
   vercel env add ALLOWED_HOSTS
   ```

5. **Deploy to Production**
   ```bash
   vercel --prod
   ```

### 3. Post-Deployment Setup

After successful deployment:

1. **Access Your Site**
   - Open the deployment URL provided by Vercel
   - You should see the ZENVIO home page

2. **Create Admin Account** (Optional)
   - Unfortunately, you cannot run `createsuperuser` directly on Vercel
   - You'll need to create accounts through the registration page
   - For admin access, you may need to use a different approach or create a management command

3. **Test All Features**
   - User registration and login
   - Contact CRUD operations
   - CSV import functionality
   - Static files loading correctly

### 4. Custom Domain (Optional)

1. **Add Custom Domain**
   - Go to your Vercel project settings
   - Click "Domains"
   - Add your custom domain
   - Follow DNS configuration instructions

2. **Update ALLOWED_HOSTS**
   - Add your custom domain to ALLOWED_HOSTS environment variable
   - Example: `ALLOWED_HOSTS = .vercel.app,yourdomain.com`

## 🔧 Troubleshooting

### Static Files Not Loading
- Check if `whitenoise` is in requirements.txt
- Verify STATIC_ROOT is set correctly in settings.py
- Check browser console for errors

### Server Errors
- Check Vercel deployment logs
- Verify all environment variables are set
- Ensure DEBUG=False in production

### Database Issues
- SQLite works but has limitations on Vercel
- For production, consider using PostgreSQL or another cloud database
- Update DATABASE_URL environment variable accordingly

## 📊 Monitoring

- **View Logs**: Vercel Dashboard → Your Project → Runtime Logs
- **Analytics**: Available in Vercel Dashboard
- **Performance**: Check "Speed Insights" tab

## 🔄 Updating Your Deployment

To deploy updates:

1. **Make Changes Locally**
   ```bash
   # Make your code changes
   git add .
   git commit -m "Your update message"
   git push origin main
   ```

2. **Automatic Deployment**
   - Vercel automatically deploys when you push to main branch
   - Each push creates a new preview deployment
   - Production is updated after successful build

## 📝 Important Notes

1. **Database Persistence**
   - SQLite database is stored in serverless environment
   - Data may be lost between deployments
   - **Recommended**: Use a cloud database for production (PostgreSQL, MySQL)

2. **File Uploads**
   - Vercel serverless functions are stateless
   - Uploaded files may not persist
   - **Recommended**: Use cloud storage (AWS S3, Cloudinary)

3. **Performance**
   - First request may be slow (cold start)
   - Subsequent requests will be faster
   - Consider upgrading Vercel plan for better performance

## 🎯 Production Checklist

Before going live:

- [ ] Set strong SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Test all CRUD operations
- [ ] Test user authentication
- [ ] Test CSV import
- [ ] Check static files loading
- [ ] Set up custom domain (optional)
- [ ] Configure production database (recommended)
- [ ] Set up monitoring and alerts
- [ ] Review security settings

## 🆘 Support

If you encounter issues:
1. Check Vercel deployment logs
2. Review Django error messages
3. Verify environment variables
4. Check GitHub issues
5. Contact support

---

**Good luck with your deployment! 🚀**
