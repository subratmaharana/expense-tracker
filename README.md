# 💰 Expense Tracker Pro

A full-stack personal finance management web application built with Django and Bootstrap. 
It helps users manage expenses, income, budgets, transactions and financial reports from one dashboard.

## 🚀 Live Demo

👉 [Expense Tracker Pro](https://expense-tracker-ijhs.onrender.com/)

## ✨ Features

- 🔐 User Registration & Login
- 🔑 Password Change & Password Reset with OTP
- 👤 User Profile with Profile Picture
- 💸 Add, Edit, Delete and Search Expenses
- 💰 Add and Manage Income Sources
- 📊 Monthly Budget Management
- 📈 Dashboard with Financial Analytics
- 📊 Expense Category Charts
- 📉 Income vs Expense Charts
- 📄 Generate Financial Reports
- 📥 Export Reports to PDF and Excel
- 🗂️ Expense Categories
- 🔎 Transaction Filtering
- 📱 Responsive Design for Mobile and Desktop
- 🛡️ Django Admin Panel
- 🚀 Deployed on Render

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
- Chart.js

### Backend
- Python
- Django

### Database
- MySQL (Local Development)
- PostgreSQL (Production)

### Deployment
- Render

## 📊 Dashboard

The dashboard provides:

- Total Income
- Total Expenses
- Remaining Balance
- Monthly Budget
- Budget Usage
- Recent Transactions
- Expense Analytics
- Income vs Expense Analysis

## 🔐 Authentication

The application includes:

- User Registration
- Login / Logout
- Change Password
- Forgot Password
- Email OTP Verification
- Password Reset

## 📄 Reports

Users can view their monthly financial reports and export transaction data in:

- PDF
- Excel

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/subratmaharana/expense-tracker.git
cd expense-tracker
python -m venv env
env\Scripts\activate
pip install -r backend/requirements.txt
cd backend
python manage.py migrate
python manage.py runserver
Open in your browser:

http://127.0.0.1:8000/
