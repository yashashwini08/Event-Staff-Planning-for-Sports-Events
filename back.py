import streamlit as st
import pandas as pd
from datetime import datetime
from prettytable import PrettyTable  
from PIL import Image
class staff:
 def add_staff(self,name, role, wage_rate):
    staff_data = pd.DataFrame([[name, role, wage_rate, None, None]], columns=["Name", "Role", "Wage Rate", "Start Time", "Stop Time"])
    return staff_data

 def calculate_working_time(self,start_time, stop_time):
    if isinstance(start_time, str) and isinstance(stop_time, str):
        start = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        stop = datetime.strptime(stop_time, "%Y-%m-%d %H:%M")
        working_time = stop - start
        return working_time.total_seconds() / 3600
    else:
        return 0

 def calculate_wages(self,working_time, wage_rate):
    return working_time * wage_rate

 def set_background(self):
  img = Image.open("background.jpg")
  st.image(
     img , 
     width = 800 ,
     channels = "BGR"
  )

 def display_staff_details(self,staff_data):
    table = PrettyTable()
    table.field_names = ["Name", "Role", "Start Time", "Stop Time", "Working Hours", "Wage"]
    
    for index, row in staff_data.iterrows():
        if row["Start Time"] and row["Stop Time"]:
            working_time = self.calculate_working_time(row["Start Time"], row["Stop Time"])
            wages = self.calculate_wages(working_time, row["Wage Rate"])
            table.add_row([row['Name'], row['Role'], row['Start Time'], row['Stop Time'], f"{working_time:.2f} hours", f"${wages:.2f}"])

    return table
s=staff()
def main():
    s.set_background()

    st.title("Event Staff Management System")
    menu = ["Add Staff", "Automated Scheduling", "Input Start and Stop Time", "Calculate Working Time", "Display Details", "Add Leave", "Show Staff On Leave", "Check Availability", "report problem"]
    choice = st.sidebar.selectbox("Menu", menu)

    try:
        staff_data = pd.read_csv("staff_data.csv")
    except FileNotFoundError:
        staff_data = pd.DataFrame(columns=["Name", "Role", "Wage Rate", "Start Time", "Stop Time"])

    try:
        leave_data = pd.read_csv("leave_data.csv")
    except FileNotFoundError:
        leave_data = pd.DataFrame(columns=["Name", "Leave Date"])

    if choice == "Add Staff":
        st.header("Add Staff")
        name = st.text_input("Name")
        role = st.text_input("Role")
        wage_rate = st.number_input("Wage Rate", min_value=0.0, step=0.01)
        if st.button("Add"):
            new_staff_data = s.add_staff(name, role, wage_rate)
            staff_data = pd.concat([staff_data, new_staff_data], ignore_index=True)
            staff_data.to_csv("staff_data.csv", index=False)
            st.success("Staff added successfully!")

    elif choice == "Input Start and Stop Time":
        st.header("Input Start and Stop Time")
        selected_staff = st.selectbox("Select Staff Member", staff_data["Name"].tolist())
        start_time = st.text_input("Start Time (YYYY-MM-DD HH:MM)")
        stop_time = st.text_input("Stop Time (YYYY-MM-DD HH:MM)")
        if st.button("Update"):
            index = staff_data.index[staff_data["Name"] == selected_staff].tolist()[0]
            staff_data.at[index, "Start Time"] = start_time
            staff_data.at[index, "Stop Time"] = stop_time
            staff_data.to_csv("staff_data.csv", index=False)
            st.success("Time updated successfully!")
            working_time = s.calculate_working_time(start_time, stop_time)
            st.write(f"Total working hours for {selected_staff}: {working_time:.2f} hours")

    elif choice == "Calculate Working Time":
        st.header("Calculate Working Time")
        selected_staff = st.selectbox("Select Staff Member", staff_data["Name"].tolist())
        start_time = staff_data.loc[staff_data["Name"] == selected_staff, "Start Time"].values[0]
        stop_time = staff_data.loc[staff_data["Name"] == selected_staff, "Stop Time"].values[0]
        if start_time and stop_time:
            working_time = s.calculate_working_time(start_time, stop_time)
            st.write(f"{selected_staff} worked for {working_time:.2f} hours.")

    elif choice == "Display Details":
        st.header("Display Details")
        st.write(s.display_staff_details(staff_data))  

    elif choice == "Add Leave":
        st.header("Add Leave")
        selected_staff = st.selectbox("Select Staff Member", staff_data["Name"].tolist())
        leave_date = st.date_input("Leave Date")
        if st.button("Add"):
            leave_data = pd.concat([leave_data, pd.DataFrame([[selected_staff, leave_date]], columns=["Name", "Leave Date"])], ignore_index=True)
            leave_data.to_csv("leave_data.csv", index=False)
            st.success("Leave added successfully!")

    elif choice == "Check Availability":
        st.header("Check Availability")
        check_date = st.date_input("Select Date")
        try:
            leave_data = pd.read_csv("leave_data.csv")
        except FileNotFoundError:
            leave_data = pd.DataFrame(columns=["Name", "Leave Date"])

        leave_staff = leave_data[leave_data["Leave Date"] == str(check_date)]["Name"].tolist()
        available_staff = [staff for staff in staff_data["Name"].tolist() if staff not in leave_staff]
        st.write("Available Staff:")
        for staff in available_staff:
            st.write(staff)
    
    elif choice == "Automated Scheduling":
        st.header("Automated Scheduling")
        event_date = st.date_input("Event Date")
        event_duration = st.number_input("Event Duration (hours)", min_value=1, step=1)
        roles_needed = st.multiselect("Roles Needed", staff_data["Role"].unique())

        if "Leave" not in staff_data.columns:
            staff_data["Leave"] = None

        available_staff = staff_data[
            (staff_data["Leave"] != str(event_date)) & 
            (staff_data["Role"].isin(roles_needed))
        ]

        staff_needed = available_staff["Role"].value_counts()

        schedule = {}
        for role, count in staff_needed.items():
            available_staff_role = available_staff[available_staff["Role"] == role]
            schedule[role] = available_staff_role["Name"].sample(min(count, len(available_staff_role)))

        st.write("Suggested Schedule:")
        for role, staff in schedule.items():
            st.write(f"{role}: {', '.join(staff)}")
    
    elif choice == "Show Staff On Leave":
        st.header("Staff On Leave")
        try:
            leave_data = pd.read_csv("leave_data.csv")
        except FileNotFoundError:
            st.write("No staff are currently on leave.")
        else:
            for index, row in leave_data.iterrows():
                st.write(f"{row['Name']} is on leave on {row['Leave Date']}")
    
    elif choice == "report problem":
        st.header(":mailbox: Get In Touch With Me!")


        contact_form = """
        <form action="https://formsubmit.co/magamyashashwini@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
       """

        st.markdown(contact_form, unsafe_allow_html=True)

        def local_css(file_name):
           with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")   
        

if __name__ == "__main__":
    main()

