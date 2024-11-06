import streamlit as st
import pandas as pd
import time
import os
from PIL import Image
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="UTP ParcelHub", page_icon=":package:", layout="centered")

# Initialize session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'splash_screen'

# Define a placeholder for dynamic content
placeholder = st.empty()

# Splash Screen
if st.session_state.page == 'splash_screen':
    st.markdown("""
        <style>
        .stApp { background-color: #F1F0EC; }
        .centered-content {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            text-align: center;
        }
        h1 { text-align: center; color: #344EAD; }
        p { text-align: center; color: #000000; }
        </style>
    """, unsafe_allow_html=True)

    # Display the splash screen content
    with placeholder.container():
        st.markdown("""
            <div class="centered-content">
                <h1>UTP<br>ParcelHub</h1>
                <p>By student for students</p>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(3)  # Show splash screen for 3 seconds
        st.session_state.page = 'landing'  # Switch to landing page
        placeholder.empty()  # Clear the splash screen

# Landing Page
if st.session_state.page == 'landing':
    placeholder.empty()  # Ensure placeholder is cleared before rendering landing page
    with placeholder.container():
        st.markdown("""
        <style>
        .stApp {
            background-color: #F1F0EC;
        }
        .stButton > button {
            background-color: #091F5B;
            color: white; !important
            font-weight: bold;
            font-size: 20px;
            width: 100%;
            height: 90px;
            padding: 10px;
            border-radius: 10px;
            cursor: pointer;
            border: none;
        }
        .stButton > button:hover {
            opacity: 0.9;
        }
        </style>
        """, unsafe_allow_html=True)

        # Layout: Two columns for buttons
        col1, col2 = st.columns([1, 1])

        # Button for "UTP Student & Staff" navigation
        with col1:
            if st.button('UTP Student & Staff'):
                st.session_state.page = 'user_detail'  # Set page to parcel hub sign up page
                placeholder.empty()  # Clear the landing page before rendering the new one

        # Button for "Parcel Hub Admin" navigation
        with col2:
            if st.button('Parcel Hub Admin'):
                st.session_state.page = 'parcel_hub'  # Set page to 'parcel_hub'
                placeholder.empty()  # Clear the landing page before rendering the new one
        
        # Additional Button for "Parcel Bro Admin"
        if st.button('Parcel Bro Admin'):
            st.session_state.page = 'parcel_bro'  # Set page to 'parcel_bro'
            placeholder.empty()  # Clear the landing page before rendering the new one

# Initialize session state
if 'name' not in st.session_state: 
    st.session_state.name = None
if 'address' not in st.session_state:
    st.session_state.address = None
    
if st.session_state.page == 'user_detail':
    placeholder.empty()
    with placeholder.container():
        st.markdown("""
        <style>
        
        .stApp {
            background-color: #F1F0EC;
        }
        
        h2 {
            text-align: left;
            color: #344EAD;      
        }
        
        p {
            text-align: left;
            color: #000000;
        }
        
        .stButton button {
            color: #ffffff;  
            background-color: #d8a15d;
            display: flex;
            justify-content: center;
            border-radius: 8px;
            padding: 5px 60px;
            font-size: 18px;
            border: 1px solid transparent;  /* Transparent border */
            display: flex;
            justify-content: center;
            margin: auto;  /* Center the button */
        }
        
        .stButton button:hover {
            background-color: #B99058;  /* Change background on hover */
            border: 1px solid white;   /* White border on hover */
            color: white;  /* Keep text color white on hover */
        }    
        </style>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<h2>Personal Details</h2>', unsafe_allow_html=True)

    st.markdown('<p>Get yourself started with Parcel Hub! Fill in the details below.</p>', unsafe_allow_html=True)

    # Input fields for user data
    name = st.text_input("Name", "Enter name on parcel")
    phoneNum = st.text_input("Phone Number", "Enter your Phone Number")
    
    st.divider()

    # Title with new color
    st.markdown('<h2>Address</h2>', unsafe_allow_html=True)

    # Description text
    st.markdown('<p>Kindly select your address for delivery purposes. </p>', unsafe_allow_html=True)

    # Define the selectboxes for each V
    V1 = st.selectbox("V1 options", ["V1", "V1A", "V1B", "V1C"],index=None)
    V2 = st.selectbox("V2 options", ["V2", "V2A", "V2B", "V2C"],index=None)
    V3 = st.selectbox("V3 options", ["V3", "V3A", "V3B", "V3C", "V3D", "V3E", "V3F"],index=None)
    V4 = st.selectbox("V4 options", ["V4", "V4A", "V4B", "V4C", "V4D", "V4E"],index=None)
    V5 = st.selectbox("V5 options", ["V5", "V5A", "V5B", "V5H", "V5K"],index=None)
    V6 = st.selectbox("V6 options", ["V6", "V6A", "V6B"],index=None)
    others = st.text_input("Others", "Your preferred address (if not listed)")

    # Variable to store the selected value
    selected_value = None

    # Determine which selectbox was used and set the selected value based on the actual selection
    if V1 != "Select an option" and V1:
        selected_value = V1
    elif V2 != "Select an option" and V2:
        selected_value = V2
    elif V3 != "Select an option" and V3:
        selected_value = V3
    elif V4 != "Select an option" and V4:
        selected_value = V4
    elif V5 != "Select an option" and V5:
        selected_value = V5
    elif V6 != "Select an option" and V6:
        selected_value = V6
    elif others:  # In case user types in their custom address
        selected_value = others

    # Display the selected value
    if selected_value:
        st.write(f"You selected: {selected_value}")
        st.session_state['address'] = selected_value  # Store the selected value in session state

    # Button to switch page
    if st.button("Continue"):
        st.session_state.page = 'home'
        st.session_state.name = name  # Set name in session state

# Home Page
if st.session_state.page == 'home':
    placeholder.empty()  # Ensure landing page is cleared        
    with placeholder.container():
        st.markdown("""
        <style>
            .stApp {
                background-color: white;
            }
            
            h2, h3, h4, h5 {
            color: #091F5B;  
            }
            
            .text {
                color: black;
            }
            .stButton > button {
                background-color: #091F5B;
                color: white; 
                font-weight: bold;
                font-size: 20px;
                width: 100%;
                height: 90px;
                padding: 10px;
                border-radius: 10px;
                cursor: pointer;
                border: none;
            }
            .stButton > button:hover {
                opacity: 0.9;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # st.subheader(f"Welcome, {st.session_state.name}!")        
        
        st.markdown('<h2 class="header">Welcome, {}</h2>'.format(st.session_state.name), unsafe_allow_html=True)
        st.image("![holiday_notice_image png](https://github.com/user-attachments/assets/7d2c11c4-e935-4c6a-bb4f-230365a9fcc5)")  # Ensure the path is correct
        st.markdown('<h5 class="header">Current Address: {}</h5>'.format(st.session_state.address), unsafe_allow_html=True)

        # st.write(f"Current Address: {st.session_state.address}")  # Display the current address


if st.session_state.page == 'home':
        # Button layout
        left_col, right_col = st.columns([1, 1])
        with left_col:
            if st.button("Information"):
                st.session_state.page = 'information'  # Navigate to 'information' page
                placeholder.empty()

        with right_col:
            if st.button("Delivery"):
                st.session_state.page = 'delivery'  # Navigate to 'delivery' page
                placeholder.empty()

        if st.button("Parcel Availability"):
            st.session_state.page = 'parcel_availability'  # Navigate to 'parcel_availability'
            placeholder.empty()


        if st.button("Need Help? Reach out to us."):
            st.session_state.page = 'cust_service'  # Navigate to 'cust_service'
            placeholder.empty()
        
        if st.button('Back'):
                st.session_state.page = 'landing'  # Set page to 'landing' page
            
            
# Information Page           
if st.session_state.page == 'information':
    placeholder.empty()  # Ensure Home page is cleared
    with placeholder.container():
        st.markdown("""
        <style>
        /* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
                
        /* Global text color to blue */
        h1 {
            color: #344EAD !important;
        }
        
        h2, h3, h4, p {
            color: #000000;
        }
    
        .stButton > button {
            background-color: #344EAD ;
            color: white; !important;
        }
        </style> 
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([8,1])
        
        with col1:
            # Folder where images are stored
            UPLOAD_DIR = "announcement_images"
            ANNOUNCEMENT_FILE = "announcement.txt"

            st.title("Information")

            # Display the latest announcement
            st.subheader("Important Announcement")

            if os.path.exists(ANNOUNCEMENT_FILE):
                with open(ANNOUNCEMENT_FILE, "r") as f:
                    announcement = f.read()
                if announcement:
                    st.write(announcement)
                else:
                    st.write("No announcements at the moment.")
            else:
                st.write("No announcement posted yet.")


            # Check if the folder has any images
            if os.path.exists(UPLOAD_DIR):
                image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

                if image_files:
                    for image_file in image_files:
                        image = Image.open(os.path.join(UPLOAD_DIR, image_file))
                        st.image(image, use_column_width=True)
                else:
                    st.write("No images uploaded yet.")
            else:
                st.write("No images folder found.")
        
        with col2:
            if st.button('Close'):
                st.session_state.page = 'landing'  # Set page to 'landing' page

if st.session_state.page == 'delivery':
    placeholder.empty() # Clear home page content
    with placeholder.container():
        
        st.write("enter code for delivery")
        

if st.session_state.page == 'parcel_availability':
    placeholder.empty()
    with placeholder.container():
        
        col1, col2 = st.columns([8, 1])
        
        with col1:
            # Directory and file setup
            PARCEL_FILE_PATH = "parcel_data.csv"

            # Load parcel data
            def load_parcel_data():
                if os.path.exists(PARCEL_FILE_PATH):
                    return pd.read_csv(PARCEL_FILE_PATH)
                else:
                    return pd.DataFrame(columns=["Tracking Number", "Status", "Arrival Date" "Collection Date", "Image File"])

            # Customer tracking interface
            st.title("Parcel Tracking")
            st.subheader("Enter Tracking Number")

            tracking_num = st.text_input("Parcel Tracking Number")

            if st.button("Check Status"):
                if tracking_num:
                    df = load_parcel_data()
                    parcel = df[df["Tracking Number"] == tracking_num]

                    if not parcel.empty:
                        arrival_date = parcel["Arrival Date"].values[0]
                        status = parcel["Status"].values[0]
                        collection_date = parcel["Collection Date"].values[0]
                        image_file = parcel["Image File"].values[0]
                        
                        st.write(f"**Arrival Date:** {arrival_date}")
                        st.write(f"**Status:** {status}")
                        st.write(f"**Collection Date:** {collection_date}")

                        if image_file and os.path.exists(os.path.join("announcement_images", image_file)):
                            st.image(os.path.join("announcement_images", image_file), caption=tracking_num, width=200)
                    else:
                        st.error("No parcel found with the provided Tracking Number.")
                else:
                    st.warning("Please enter a Tracking Number.")
                    
        with col2:
            if st.button('Close'):
                st.session_state.page = 'home'  # Set page to 'home' page
        
if st.session_state.page == 'cust_service':
    placeholder.empty()
    with placeholder.container():
        st.markdown("""
        <style>
        /* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
                
        /* Global text color to blue */
        h1 {
            color: #344EAD !important;
        }
        
        h2, h3, h4, p {
            color: #000000;
        }
    
        .stButton > button {
            background-color: #344EAD ;
            color: white; !important;
        }
        </style> 
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([8, 1])
        
        with col1: 
            # Directory and file setup
            CUST_SERVICE_FILE = "cust_service.txt"
            
            st.title("Customer Feedback")
            feedback = st.text_area("Please share your feedback or questions with us!")
            
            if st.button("Submit"):
                if feedback:  # Check if feedback is not empty
                    with open(CUST_SERVICE_FILE, "a") as f:  # Append feedback to the file
                        f.write(feedback + "\n")  # Write feedback with a newline
                    st.success("Thank you for your feedback!")  # Confirmation message
                else:
                    st.warning("Please enter feedback before submitting.")

            # Check if feedback file exists and display previous feedback
            if os.path.exists(CUST_SERVICE_FILE):
                st.subheader("Your Previous Feedback")
                with open(CUST_SERVICE_FILE, "r") as f:
                    current_feedback = f.readlines()  # Read all lines from the file
                for line in current_feedback:
                    st.write(line.strip())  # Display each line of feedback

            else:
                st.write("No feedback posted yet.")
        
        with col2: 
            st.write("")
            st.write("")
            if st.button('Close'):
                st.session_state.page = 'home'  # Set page to 'home' page

# Parcel Hub Admin Page
if st.session_state.page == 'parcel_hub':
    placeholder.empty()  # Clear landing page content
    with placeholder.container():
        st.sidebar.title("Admin Pages")
        
        col1, col2 = st.columns([8, 1])
        
        with col1:
            # Create dropdown selection
            ph_admin_page = st.selectbox("Go to", ["Parcel Key-In", "Parcel Key-Out", "Content Management"])
            st.session_state.ph_admin_page = ph_admin_page  # Store selection in session state

            # Directory and file setup
            PARCEL_FILE_PATH = "parcel_data.csv"
            UPLOAD_DIR = "uploaded_images"
            ANNOUNCEMENT_FILE = "announcement.txt"
            
            # Ensure upload directory exists
            if not os.path.exists(UPLOAD_DIR):
                os.makedirs(UPLOAD_DIR)

            # Define functions for handling parcel data
            def load_parcel_data():
                if not os.path.exists(PARCEL_FILE_PATH):
                    df = pd.DataFrame(columns=["Tracking Number", "Phone Number", "Status", "Arrival Date", "Collection Date", "Image File"])
                    df.to_csv(PARCEL_FILE_PATH, index=False)
                return pd.read_csv(PARCEL_FILE_PATH, dtype={"Phone Number": str})

            def save_parcel_data(data):
                data.to_csv(PARCEL_FILE_PATH, index=False)
                
            # Function to add new parcel to the CSV file
            def add_new_parcel(tracking_num, phone_num, arrival_date, image_file_name):
                df = load_parcel_data()
                new_data = pd.DataFrame({
                    "Tracking Number": [tracking_num],
                    "Phone Number": [phone_num],
                    "Status": ["Not Collected"],
                    "Arrival Date": [arrival_date],
                    "Collection Date": [""],
                    "Image File": [image_file_name]
                })
                df = pd.concat([df, new_data], ignore_index=True)
                save_parcel_data(df)
                st.success(f"Parcel added successfully! Tracking Number: {tracking_num}")


            # Parcel Key-In Section
            if st.session_state.ph_admin_page == "Parcel Key-In":
                st.title("Parcel Key-In")
                st.subheader("Add New Parcel")

                # Input fields for new parcel entry
                phone_num = st.text_input("Phone Number")
                tracking_num = st.text_input("Parcel Tracking Number")
                arrival_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Image uploader and camera
                uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
                
                # Button to open the camera
                open_camera = st.button("Open Camera")
                
                # Show the camera input only when the "Open Camera" button is clicked
                if open_camera:
                    captured_image = st.camera_input("Capture an image")

                # Add new parcel on submit
                if st.button("Submit New Parcel"):
                    if phone_num and tracking_num:
                        image_file_name = None
                        
                        # Handle image saving and naming
                        if uploaded_image:
                            image_file_name = f"{tracking_num}_{uploaded_image.name}"
                            with open(os.path.join(UPLOAD_DIR, image_file_name), "wb") as f:
                                f.write(uploaded_image.getbuffer())

                        elif 'captured_image' in locals() and captured_image is not None:
                            image_file_name = f"captured_{tracking_num}.png"
                            with open(os.path.join(UPLOAD_DIR, image_file_name), "wb") as f:
                                f.write(captured_image.getbuffer())

                        # Save parcel to CSV
                        add_new_parcel(tracking_num, phone_num, arrival_date, image_file_name)

                    else:
                        st.warning("Please fill all the fields.")


            # Parcel Key-Out Section
            elif st.session_state.ph_admin_page == "Parcel Key-Out":
                st.title("Parcel Key-Out")
                st.subheader("Mark Parcel as Collected")
                
                # Input field for parcel details (Tracking Number)
                tracking_num = st.text_input("Enter Parcel Tracking Number for Collection", "")
                
                # Button to mark parcel as collected
                if st.button("Confirm Collection"):
                    if tracking_num:
                        df = load_parcel_data()
                        parcel_index = df.index[df["Tracking Number"] == tracking_num].tolist()
                        
                        if parcel_index:
                            df.at[parcel_index[0], "Status"] = "Collected"
                            df.at[parcel_index[0], "Collection Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            save_parcel_data(df)
                            st.success(f"Parcel with Tracking Number {tracking_num} marked as collected!")
                        else:
                            st.error("No parcel found with the provided Tracking Number.")


            # Content Management Section
            elif st.session_state.ph_admin_page == "Content Management":
                st.title("Content Management")
                st.subheader("Manage Images, Announcements, and more")
                
                # Upload Images Section
                with st.expander("Upload Images", expanded=True):
                    uploaded_files = st.file_uploader(
                        "Choose images to upload", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
                    )

                    if uploaded_files:
                        for uploaded_file in uploaded_files:
                            with open(os.path.join(UPLOAD_DIR, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            st.success(f"Uploaded {uploaded_file.name} successfully!")

                # Post Announcements Section
                with st.expander("Post and Manage Announcements", expanded=True):
                    announcement = st.text_area("Write your announcement here:")

                    if st.button("Post Announcement"):
                        with open(ANNOUNCEMENT_FILE, "w") as f:
                            f.write(announcement)
                        st.success("Announcement posted successfully!")

                    if os.path.exists(ANNOUNCEMENT_FILE):
                        st.subheader("Current Announcement")
                        with open(ANNOUNCEMENT_FILE, "r") as f:
                            current_announcement = f.read()
                        st.write(current_announcement)

                        if st.button("Delete Announcement"):
                            os.remove(ANNOUNCEMENT_FILE)
                            st.success("Announcement deleted successfully!")
                    else:
                        st.write("No announcement posted yet.")

                # Manage Uploaded Images Section
                with st.expander("Manage Uploaded Images", expanded=True):
                    st.subheader("Uploaded Images")

                    if os.path.exists(UPLOAD_DIR):
                        image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

                        if image_files:
                            for image_file in image_files:
                                st.write(f"Image: {image_file}")
                                st.image(os.path.join(UPLOAD_DIR, image_file), caption=image_file, use_column_width=True)

                            for image_file in image_files:
                                if st.button(f"Delete {image_file}", key=image_file):
                                    os.remove(os.path.join(UPLOAD_DIR, image_file))
                                    st.success(f"Deleted {image_file} successfully!")
                        else:
                            st.write("No images uploaded yet.")
                            
                
                # Manage Customer Feedback section 
                with st.expander("Manage Customer Feedback", expanded=True):
                    st.subheader("Customer Feedback")
                    
                    # Folder where the text is stored
                    CUST_SERVICE_FILE = "cust_service.txt"

                    if os.path.exists(CUST_SERVICE_FILE):
                        with open(CUST_SERVICE_FILE, "r") as f:
                            feedback = f.read()
                        if feedback:
                            st.write(feedback)
                        else:
                            st.write("No announcements at the moment.")
                    else:
                        st.write("No announcement posted yet.")
                            
        with col2: 
            st.write("")
            st.write("")
            if st.button('Back'):
                st.session_state.page = 'landing'  # Set page to 'landing' page

