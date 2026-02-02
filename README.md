# Chemical Equipment Parameter Visualizer  
**Hybrid Web + Desktop Application**

This project is developed as part of an internship screening task.  
It is a hybrid analytics application that runs both as a **Web Application** and a **Desktop Application**, powered by a common Django REST backend.

The system allows users to upload chemical equipment data in CSV format and visualize analytical insights such as averages, distributions, tabular data, and downloadable reports.

---

## Project Overview

The Chemical Equipment Parameter Visualizer processes and analyzes chemical equipment data containing parameters like flowrate, pressure, and temperature.

A single Django REST API backend is shared by:
- A **React.js web frontend**
- A **PyQt5 desktop application**

Both frontends consume the same APIs, ensuring consistency in analytics and results.

---

## Features

### Core Features
- CSV file upload (Web & Desktop)
- Data analysis using Pandas
- Summary statistics:
  - Total equipment count
  - Average temperature
  - Average pressure
  - Average flowrate
- Equipment type distribution visualization
- Tabular view of equipment data
- PDF report generation
- Basic authentication (login/logout)
- Dataset history (last 5 uploads)

### Visualization
- **Web**: Chart.js (bar charts)
- **Desktop**: Matplotlib (bar charts)

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- Pandas
- SQLite
- ReportLab (PDF generation)

### Frontend (Web)
- React.js
- Chart.js
- Axios
- HTML / CSS

### Frontend (Desktop)
- PyQt5
- Matplotlib
- Requests

### Version Control
- Git & GitHub

---

## Sample Data

A sample CSV file is provided for testing and demonstration:

# Chemical Equipment Parameter Visualizer  
**Hybrid Web + Desktop Application**

This project is developed as part of an internship screening task.  
It is a hybrid analytics application that runs both as a **Web Application** and a **Desktop Application**, powered by a common Django REST backend.

The system allows users to upload chemical equipment data in CSV format and visualize analytical insights such as averages, distributions, tabular data, and downloadable reports.

---

## Project Overview

The Chemical Equipment Parameter Visualizer processes and analyzes chemical equipment data containing parameters like flowrate, pressure, and temperature.

A single Django REST API backend is shared by:
- A **React.js web frontend**
- A **PyQt5 desktop application**

Both frontends consume the same APIs, ensuring consistency in analytics and results.

---

## Features

### Core Features
- CSV file upload (Web & Desktop)
- Data analysis using Pandas
- Summary statistics:
  - Total equipment count
  - Average temperature
  - Average pressure
  - Average flowrate
- Equipment type distribution visualization
- Tabular view of equipment data
- PDF report generation
- Basic authentication (login/logout)
- Dataset history (last 5 uploads)

### Visualization
- **Web**: Chart.js (bar charts)
- **Desktop**: Matplotlib (bar charts)

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- Pandas
- SQLite
- ReportLab (PDF generation)

### Frontend (Web)
- React.js
- Chart.js
- Axios
- HTML / CSS

### Frontend (Desktop)
- PyQt5
- Matplotlib
- Requests

### Version Control
- Git & GitHub

---

## Sample Data

A sample CSV file is provided for testing and demonstration:

sample_equipment_data.csv

**CSV Columns**
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

---

## Project Structure

```text
chemical-equipment-visualizer/
│
├── backend/          # Django backend
│   ├── accounts/
│   ├── equipment/
│   ├── config/
│   └── manage.py
│
├── web/              # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
│
├── desktop/          # PyQt5 desktop application
│   ├── app.py
│   ├── login_window.py
│   └── dashboard_window.py
│
├── sample_data/      # Sample CSV file
├── screenshots/      # UI screenshots
├── demo_video/       # Demo recording
└── README.md

```

###Setup Instructions
##1. Backend Setup (Django)

-cd backend
-python -m venv venv
-venv\Scripts\activate      # Windows
-pip install -r requirements.txt
-python manage.py migrate
-python manage.py runserver

---

Backend will run at:
http://127.0.0.1:8000/

2. Web Frontend Setup (React)

cd web
npm install
npm start

Web application will run at:
http://localhost:3000/

3. Desktop Application Setup (PyQt5)

cd desktop
pip install PyQt5 matplotlib requests
python app.py

API Endpoints

| Endpoint           | Method | Description                     |
| ------------------ | ------ | ------------------------------- |
| `/api/upload/`     | POST   | Upload CSV and receive analysis |
| `/api/history/`    | GET    | Fetch last 5 uploaded datasets  |
| `/api/report/pdf/` | GET    | Download latest PDF report      |
| `/api/auth/login/` | POST   | User authentication             |


Demo Video

A short demo video (2–3 minutes) demonstrates:

Login flow

CSV upload

Data analysis and visualization

PDF report generation

Web and Desktop application usage

Notes

Both Web and Desktop applications use the same backend APIs.

The project strictly follows the screening task requirements.

UI is intentionally kept simple and professional.

Focus is on correctness, clarity, and maintainability.

Author

Suriyaganesh

Computer Science and Engineering

Internship Screening Project
