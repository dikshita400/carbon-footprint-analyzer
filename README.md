# 🌱 AI-Based Carbon Footprint Analyzer for Websites

## 📌 Overview
This project is an AI/ML-based web application that estimates the carbon footprint of a website. It analyzes key parameters such as page size, number of requests, and load time, and predicts CO₂ emissions using a Machine Learning model.

The system also provides optimization suggestions to help reduce environmental impact and promote sustainable web development.

---

## 🎯 Features
- 🌐 Analyze any website using URL
- 🤖 AI-based carbon emission prediction
- 📊 Real-time data processing
- 💡 Optimization suggestions
- 🎨 Simple and aesthetic user interface

---

## 🧠 How It Works
1. User enters a website URL  
2. Flask backend fetches website data  
3. Extract features:
   - Page size (KB)
   - Number of requests
   - Load time (seconds)  
4. Machine Learning model predicts CO₂ emission  
5. Suggestions are generated and displayed  

---

## 🏗️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** Scikit-learn (Linear Regression)  
- **Libraries:** Requests, Pandas  

---

## 📂 Project Structure
CarbonFootprint_Estimator_AI/
│── app.py
│── model.py
│── data.csv
│── templates/
│ └── index.html

