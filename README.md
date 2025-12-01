
🧘‍♀ MoodMate: AI-Powered Mood & Wellness Web App

🌟 Overview

MoodMate is a Django-based wellness web application that detects the user’s mood through an interactive quiz and provides personalized relaxation tips, motivational quotes, and music suggestions.
It also stores user history in a MySQL database and displays a beautiful analytics dashboard with mood charts and tables.


---

💡 Features

✅ Mood Detection Quiz – Answer 7 short questions to detect your mood.
✅ Dynamic Result Page – Colorful, mood-based themes (Happy, Calm, Stressed, Sad).
✅ Personalized Suggestions – Yoga, music, and positive thoughts for each mood.
✅ Mood History Dashboard – Track your emotional trends with a Chart.js graph.
✅ MySQL Integration – Stores user mood history securely using Django ORM.
✅ Modern UI – Built with Bootstrap 5, CSS animations, and motivational design.
✅ Responsive Design – Works beautifully on both desktop and mobile devices.


---

🧩 Tech Stack

Category	Technologies

Frontend	HTML5, CSS3, Bootstrap 5, JavaScript (Chart.js)
Backend	Django (Python 3.x)
Database	MySQL
Visualization	Chart.js (Mood Analytics)
Version Control	Git & GitHub



---

🗂 Project Structure

MoodMate/
│
├── moodmate/
│   ├── settings.py
│   ├── urls.py
│
├── moodapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── moodapp/
│   │       ├── index.html
│   │       ├── quiz.html
│   │       ├── result.html
│   │       └── history.html
│   └── static/moodapp/
│       ├── css/style.css
│       └── music/*.mp3
│
└── manage.py


---

⚙ Setup Instructions

⿡ Clone Repository

git clone https://github.com/yourusername/MoodMate.git
cd MoodMate

⿢ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # (Windows)
source venv/bin/activate  # (Mac/Linux)

⿣ Install Dependencies

pip install -r requirements.txt

⿤ Database Setup (MySQL)

Create a database in MySQL:

CREATE DATABASE moodmate_db;

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moodmate_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


⿥ Apply Migrations

python manage.py makemigrations
python manage.py migrate

⿦ Run the Server

python manage.py runserver

Then open:
👉 http://127.0.0.1:8000/


---

📸 Screenshots (Optional)

You can add screenshots of:

1. 🏠 Home Page – Calm gradient background with motivational quotes


2. 🎯 Quiz Page – 7 questions, yes/no answers


3. 🌈 Result Page – Dynamic mood background + activity list


4. 📊 History Page – Bar chart & mood table




---

✨ Future Enhancements

🧠 Integrate AI-based facial emotion recognition

🎵 Add Spotify or YouTube API for mood-based song playlists

🧘‍♀ Add yoga video tutorials and breathing exercises

📱 Deploy on Render / AWS / PythonAnywhere for online access



---

👩‍💻 Author

Neha Kamadi
🎓 MSc Computer Science | Passionate about AI, Psychology & Web Development


---

⭐ GitHub Tags

#django #python #mysql #chartjs #bootstrap #mood-detection #ai #wellness #mentalhealth #fullstack
