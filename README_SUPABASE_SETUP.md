# 🚀 Complete Supabase PostgreSQL Setup Guide

## ✅ **What You Get:**
- **Complete PostgreSQL Database** with Supabase
- **OTP Email Verification** system
- **Admin Approval Workflow** for new users
- **JWT Authentication** with sessions
- **Secure User Management** with role-based access

## 📋 **Step-by-Step Setup:**

### **1. Create Supabase Project**
1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Create new project
4. Choose region closest to you
5. Set strong database password

### **2. Run Database Migration**
1. In Supabase Dashboard → SQL Editor
2. Copy and paste the entire content from `supabase/migrations/create_complete_schema.sql`
3. Click "Run" to create all tables and functions

### **3. Get Your Supabase Credentials**
1. Go to Project Settings → API
2. Copy these values:
   - **Project URL** (SUPABASE_URL)
   - **Anon Public Key** (SUPABASE_ANON_KEY)
   - **Service Role Key** (SUPABASE_SERVICE_ROLE_KEY)

### **4. Configure Environment Variables**
Create `.env` file in your project root:
```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key-here
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here

# JWT Secret
JWT_SECRET=your-super-secret-jwt-key-here

# Email Configuration (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### **5. Install Backend Dependencies**
```bash
pip install -r backend/requirements.txt
```

## 🎯 **Database Schema Overview:**

### **Tables Created:**
- **`users`** → User accounts with approval system
- **`user_verifications`** → OTP codes for email verification
- **`admin_approvals`** → Admin approval tracking
- **`predictions`** → AI prediction history
- **`user_sessions`** → Active login sessions
- **`system_settings`** → App configuration

### **Security Features:**
- **Row Level Security (RLS)** enabled on all tables
- **Admin-only policies** for user management
- **User-specific data access** policies
- **JWT token authentication**

## 🔄 **User Registration Flow:**

### **1. User Registration**
```
User fills form → Account created with 'pending' status
```

### **2. Email Verification**
```
OTP sent to email → User enters code → Email verified
```

### **3. Admin Approval**
```
Admin reviews account → Approves/Rejects → User notified
```

### **4. Login Access**
```
Approved users can login → JWT token issued → Access granted
```

## 🛠 **API Endpoints:**

### **Authentication:**
- `POST /auth/register` → Register new user
- `POST /auth/verify-otp` → Verify email OTP
- `POST /auth/login` → User login

### **Admin Functions:**
- `GET /admin/pending-users` → Get users awaiting approval
- `POST /admin/approve-user` → Approve/reject users

### **Predictions:**
- `POST /predict` → AI disease prediction (saves to DB if logged in)

## 🎨 **Frontend Integration:**

### **Registration Process:**
1. **Registration Form** → User enters details
2. **OTP Verification** → User enters email code
3. **Pending Approval** → Waiting for admin
4. **Login Access** → Account approved

### **Admin Dashboard:**
- View pending users
- Approve/reject accounts
- Monitor system activity

## 🚀 **Running the Complete System:**

```bash
# Start everything
npm run start
```

This starts:
- **Flask Backend** (Port 5000) with Supabase integration
- **React Frontend** (Port 5173) with auth flow
- **Complete user management** system

## ✅ **Features Working:**

### **🔐 Security:**
- ✅ **OTP Email Verification**
- ✅ **Admin Approval Required**
- ✅ **JWT Authentication**
- ✅ **Role-based Access Control**
- ✅ **Secure Password Hashing**

### **👥 User Management:**
- ✅ **Registration with Approval**
- ✅ **Email Verification**
- ✅ **Admin Dashboard**
- ✅ **User Status Tracking**

### **🤖 AI Integration:**
- ✅ **Disease Prediction**
- ✅ **Prediction History**
- ✅ **User-specific Data**

### **🎨 Professional UI:**
- ✅ **Clean Registration Flow**
- ✅ **OTP Verification Screen**
- ✅ **Pending Approval Status**
- ✅ **Admin Management Interface**

## 📧 **Email Configuration (Optional):**

To enable OTP email delivery, configure your email service in the Flask backend. The system currently logs OTP codes to console for development.

For production, update the `send_otp_email()` function in `backend/app.py` with your email service credentials.

## 🎯 **Default Admin Account:**

A default admin account is created:
- **Email:** admin@plantdisease.com
- **Password:** (Set your own secure password)
- **Role:** admin
- **Status:** approved

Update this in the migration file before running.

Your complete Plant Disease Classifier with PostgreSQL database, OTP verification, and admin approval system is now ready!