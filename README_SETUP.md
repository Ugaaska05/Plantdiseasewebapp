# 🚀 Plant Disease Classifier - One Command Setup

## ⚡ Quick Start (One Command)

```bash
npm run start
```

This will start both your Flask backend and React frontend simultaneously!

## 📋 First Time Setup

### 1. Install Python Dependencies
```bash
# Option 1: Install from requirements file
pip install -r backend/requirements.txt

# Option 2: Install individually
pip install flask flask-cors tensorflow numpy pillow
```

### 2. Install Node Dependencies
```bash
npm install
```

### 3. Add Your AI Models
Create a `models` folder in the root directory and add your model files:
```
models/
├── gatekeeper_model.keras
├── planttype_model.keras
└── tomato_disease_densenet_model.keras
```

## 🎯 Available Commands

### Start Everything (Recommended)
```bash
npm run start
```
- Starts Flask backend on `http://localhost:5000`
- Starts React frontend on `http://localhost:5173`
- Both run simultaneously with live reload

### Individual Commands
```bash
# Backend only
npm run backend

# Frontend only  
npm run dev

# Install backend dependencies
npm run install-backend
```

## 🔧 Project Structure
```
plant-disease-classifier/
├── backend/
│   ├── app.py              # Your Flask application
│   ├── requirements.txt    # Python dependencies
│   └── uploads/           # Temporary image storage
├── models/                # Your AI model files
│   ├── gatekeeper_model.keras
│   ├── planttype_model.keras
│   └── tomato_disease_densenet_model.keras
├── src/                   # React frontend
└── package.json          # Node.js configuration
```

## ✅ What Happens When You Run `npm run start`

1. **Flask Backend Starts** → Port 5000
   - Loads your 3 AI models
   - Sets up `/predict` endpoint
   - Enables CORS for frontend connection

2. **React Frontend Starts** → Port 5173
   - Connects to Flask backend automatically
   - Provides beautiful UI for image upload
   - Shows prediction results with suggestions

3. **Live Development** → Both update automatically
   - Backend: Restarts on Python file changes
   - Frontend: Hot reload on React file changes

## 🎨 Features Working

- ✅ **3-Stage AI Analysis** → Gatekeeper → Plant Type → Disease Detection
- ✅ **Image Upload** → Drag & drop or click to upload
- ✅ **Smart Suggestions** → Treatment recommendations for each disease
- ✅ **Multi-language** → English/Somali interface
- ✅ **Professional Design** → Clean, human-made appearance
- ✅ **Error Handling** → User-friendly error messages

## 🔍 Testing Your Setup

1. **Start the application**: `npm run start`
2. **Open browser**: Go to `http://localhost:5173`
3. **Upload plant image**: Test with tomato leaf images
4. **Check results**: Should show disease detection with confidence

## 🐛 Troubleshooting

### Backend Issues
- **Models not found**: Make sure model files are in `models/` folder
- **Python dependencies**: Run `pip install -r backend/requirements.txt`
- **Port 5000 busy**: Change port in `backend/app.py`

### Frontend Issues
- **Connection failed**: Make sure Flask backend is running on port 5000
- **Node dependencies**: Run `npm install`

## 🚀 Production Deployment

For production, you'll need to:
1. Set up proper database (PostgreSQL)
2. Configure environment variables
3. Use production WSGI server (Gunicorn)
4. Build frontend for production (`npm run build`)

The current setup is perfect for development and testing!