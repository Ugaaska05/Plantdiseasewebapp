# Flask Backend Integration Guide

## 🚀 Your Flask Backend is Ready to Connect!

The frontend has been adapted to work seamlessly with your Flask backend. Here's how everything connects:

### 📡 API Integration

#### **Your Flask Endpoint**: `/predict`
- **Method**: POST
- **Input**: FormData with 'file' field
- **Output**: JSON with prediction results

#### **Frontend Adaptation**:
```javascript
// Sends image to your Flask backend
const response = await fetch('http://localhost:5000/predict', {
  method: 'POST',
  body: formData // Contains the uploaded image
});
```

### 🔄 Response Transformation

Your Flask backend returns:
```json
{
  "stage": "Tomato Disease",
  "prediction": "This tomato plant has a disease 🦠: Tomato_Early_blight",
  "confidence": "92.34%"
}
```

Frontend transforms it to:
```json
{
  "label": "Tomato_Early_blight",
  "friendly_text": "This tomato plant has a disease 🦠: Tomato_Early_blight",
  "suggestion": "Remove affected leaves, apply fungicide, and ensure proper plant spacing...",
  "confidence": 92.34,
  "stage": "Tomato Disease"
}
```

### 🎯 Smart Suggestions System

The frontend automatically generates treatment suggestions based on your Flask predictions:

- **Bacterial Spot** → "Apply copper-based bactericide..."
- **Early Blight** → "Remove affected leaves, apply fungicide..."
- **Late Blight** → "Remove infected plants immediately..."
- **Healthy** → "Continue with current care routine..."
- **Non-Plant** → "Please upload a clear plant image..."
- **Non-Tomato** → "This system is specialized for tomato plants..."

### 🚀 How to Run

#### 1. Start Your Flask Backend:
```bash
python your_flask_app.py
# Runs on http://localhost:5000
```

#### 2. Start Frontend:
```bash
npm run dev
# Runs on http://localhost:5173
```

### ✅ What Works Now:

1. **Image Upload** → Sends to your Flask `/predict` endpoint
2. **AI Analysis** → Uses your 3-stage model (Gatekeeper → Plant Type → Disease)
3. **Results Display** → Shows prediction with confidence and suggestions
4. **Error Handling** → Handles network errors and invalid responses
5. **Multi-language** → English/Somali interface

### 🔧 Configuration

Update the API base URL in `src/services/api.ts`:
```javascript
const API_BASE_URL = 'http://localhost:5000'; // Your Flask server
```

### 📊 Response Handling

Your Flask backend handles:
- ✅ **Non-plant detection** → "This is NOT a plant 🌵"
- ✅ **Non-tomato plants** → "This is a plant, but NOT a tomato 🪴"
- ✅ **Healthy tomatoes** → "This tomato plant is healthy 🌿"
- ✅ **Disease detection** → "This tomato plant has a disease 🦠"

### 🎨 UI Features

- **Clean Design** → Professional, human-made appearance
- **Working Navigation** → Home, About, Diagnostic all functional
- **Language Toggle** → English/Somali switching
- **Responsive** → Works on all devices
- **Error Messages** → User-friendly error handling

### 🔮 Future Enhancements

When you're ready to add more features:
1. **User Authentication** → Add login/register endpoints to Flask
2. **History Storage** → Save predictions to database
3. **Admin Dashboard** → User management and statistics
4. **Multiple Plant Types** → Extend beyond tomatoes

The frontend is fully prepared for these features and will work seamlessly when you add the corresponding Flask endpoints!