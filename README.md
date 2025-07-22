# 👥 Event Staff Management System (Streamlit App)

This is a Streamlit-based web application developed during my Python internship. It helps manage event staff efficiently by providing features like staff registration, scheduling, time tracking, leave management, and automated wage calculation — all through an interactive interface.

---

## 🧩 Features

- ✅ Add and manage staff details (name, role, wage rate)
- ⏱️ Track start and stop time to calculate working hours
- 💰 Automatically compute wages based on hours worked
- 📆 Record and manage staff leaves
- 🤖 Auto-schedule staff based on availability and roles
- 📊 Display detailed staff reports using PrettyTable
- 📨 Contact form for reporting problems or giving feedback

---

## 📂 Project Structure

📁 event-staff-management/
├── back.py # Main Streamlit backend application
├── staff_data.csv # Stores staff details and time logs
├── leave_data.csv # Stores staff leave records
├── background.jpg # Background image for Streamlit UI (optional)
├── style/
│ └── style.css # Custom styling for the contact form


---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – Web framework for the UI
- **Pandas** – Data manipulation and CSV handling
- **PrettyTable** – Tabular data presentation
- **Pillow (PIL)** – Image handling
- **HTML & CSS** – Contact form and UI customization

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/event-staff-management.git
cd event-staff-management

Install Dependencies
pip install streamlit pandas prettytable pillow

Run the Application
streamlit run back.py

📩 Contact / Feedback
You can reach me at:
📧 yashumagam@gmail.com

Or use the “Report Problem” section in the app to send direct feedback via the embedded contact form.

🙌 Developed By
Yashashwini Magam
As part of a hands-on learning experience during my Python internship.

🌱 Future Improvements
Add login system for admin/staff

Shift analytics dashboard (attendance, wages, roles)

Use Firebase or SQLite for persistent data storage

Calendar integration for event-based planning

📄 License
This project is licensed under the MIT License.



