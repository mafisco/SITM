import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import pandas as pd
import random
import webbrowser
import time

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Configuration
COMPANY_NAME = "SolidITMinds"
AGENT_NAME = "SITM (SaiTim)"
EMAIL = "contact@soliditminds.com"
PHONE = "+1 (404) 969-6618"
ADDRESS = "3380 Peachtree Rd NE, Atlanta, GA 30326"

# Sample data
TRAINING_COURSES = {
    "Operating Systems": [
        "Unix: Solaris 11, AIX (7.1 - 7.3)",
        "Linux: Ubuntu (20.04, 22.04), Rocky Linux (8, 9)",
        "Windows Administration"
    ],
    "Databases": [
        "Oracle (19c, 23c)", 
        "MySQL (5.7, 8.0)", 
        "PostgreSQL (11-16)", 
        "DB2 (Version 11)", 
        "SQL Server",
        "MongoDB", 
        "Cassandra"
    ],
    "DevOps": [
        "DevOps Fundamentals", 
        "Docker", 
        "Kubernetes", 
        "Terraform", 
        "Ansible"
    ],
    "Cloud": [
        "AWS Essentials", 
        "AWS Security", 
        "AWS DevOps", 
        "AWS Infrastructure as Code"
    ],
    "SQL": [
        "SQL on MySQL", 
        "SQL on PostgreSQL", 
        "SQL on Oracle (12c, 19c, 23c)", 
        "SQL on MSSQL"
    ]
}

CONSULTING_SERVICES = [
    "Database Design & Implementation",
    "Database Management & Maintenance",
    "Database Upgrades & Migration",
    "OS Installation & Configuration",
    "System Administration",
    "Security & Compliance",
    "AWS Consulting",
    "Cloud Deployment & Management",
    "Hybrid & Multi-Cloud Solutions"
]

JOB_CATEGORIES = [
    "Unix System Administrator",
    "Linux System Administrator",
    "Oracle DBA",
    "MySQL DBA",
    "PostgreSQL DBA",
    "DevOps Engineer",
    "Kubernetes Engineer",
    "Cloud Engineer (AWS)",
    "SQL Developer"
]

# Email configuration (you would replace with your actual credentials)
EMAIL_CONFIG = {
    'sender': 'your_email@example.com',
    'password': 'your_email_password',
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587
}

# Utility functions
def send_email(to_email, subject, body):
    """Send an email using SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender']
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['sender'], to_email, text)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {str(e)}")
        return False

def generate_promo_text():
    """Generate promotional text in George Carlin style"""
    return f"""
    Hey there, tech enthusiast! Tired of making peanuts while Silicon Valley CEOs buy their third yacht? 
    {COMPANY_NAME} can help you crack the code to six figures in just 90-120 days! 
    That's right - we're talking serious cash for your tech skills. 
    No fluff, no BS - just hardcore training that gets you paid. 
    What are you waiting for? Book a session now before your current job puts you to sleep again!
    """

def post_to_social_media(content):
    """Simulate posting to social media"""
    platforms = ["Twitter", "Facebook", "LinkedIn", "Instagram", "Reddit"]
    for platform in platforms:
        time.sleep(1)  # Simulate API delay
        st.success(f"Posted to {platform}: {content[:50]}...")
    return True

def create_payment_link(amount, installments=False):
    """Generate a payment link (simulated)"""
    if installments:
        return f"https://payment.example.com/checkout?amount={amount}&plan=installment"
    else:
        return f"https://payment.example.com/checkout?amount={amount}"

# Page functions
def home_page():
    st.title(f"Welcome to {COMPANY_NAME}")
    st.subheader(f"Your AI-Powered IT Consulting, Training, and Recruitment Partner")
    
    st.image("https://via.placeholder.com/800x400?text=SolidITMinds+Consulting", use_column_width=True)
    
    st.markdown("""
    ### Transform Your IT Career in 90-120 Days
    We specialize in helping professionals like you develop cutting-edge skills in:
    - Database Management
    - Operating Systems
    - DevOps
    - Cloud Platforms (AWS)
    
    **Our promise:** Six-figure salary potential within 90-120 days of training.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Explore Training Programs"):
            st.session_state.page = 'training'
    with col2:
        if st.button("Schedule Free Consultation"):
            st.session_state.page = 'consulting'
    
    st.markdown("---")
    st.subheader("What Our Students Say")
    
    testimonials = [
        {"name": "John D.", "role": "AWS Cloud Engineer", "text": "Went from $65k to $120k in 4 months!"},
        {"name": "Sarah M.", "role": "DevOps Specialist", "text": "The Docker and Kubernetes training changed my career."},
        {"name": "Mike T.", "role": "Oracle DBA", "text": "Best investment I ever made in my professional development."}
    ]
    
    for testimonial in testimonials:
        st.markdown(f"""
        **{testimonial['name']}** - *{testimonial['role']}*  
        "{testimonial['text']}"
        """)
    
    st.markdown("---")
    st.subheader("Ready to Get Started?")
    st.write("Take the first step toward your six-figure IT career today!")
    
    if st.button("Book Your Free Assessment Now"):
        st.session_state.page = 'booking'

def consulting_page():
    st.title("IT Consulting Services")
    st.subheader("Expert Solutions for Database, OS, and Cloud Mastery")
    
    st.markdown(f"""
    {COMPANY_NAME} Consulting specializes in providing expert services and support in:
    - Database management
    - Operating systems
    - DevOps
    - Cloud platforms (AWS)
    
    Our team helps businesses optimize their IT infrastructure for seamless operations and data security.
    """)
    
    st.markdown("---")
    st.subheader("Our Core Consulting Services")
    
    for service in CONSULTING_SERVICES:
        st.markdown(f"- {service}")
    
    st.markdown("---")
    st.subheader("Industries We Serve")
    
    industries = [
        "Finance & Banking", 
        "Healthcare", 
        "Retail & E-Commerce", 
        "Education", 
        "Manufacturing", 
        "Government"
    ]
    
    cols = st.columns(3)
    for i, industry in enumerate(industries):
        cols[i%3].markdown(f"- {industry}")
    
    st.markdown("---")
    st.subheader("Schedule a Consultation")
    
    with st.form("consultation_form"):
        name = st.text_input("Your Name")
        company = st.text_input("Company Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        service = st.selectbox("Service Interest", CONSULTING_SERVICES)
        message = st.text_area("Briefly describe your needs")
        
        submitted = st.form_submit_button("Request Consultation")
        if submitted:
            if name and email:
                email_body = f"""
                New consultation request from {name} at {company}.
                
                Contact Information:
                Email: {email}
                Phone: {phone}
                
                Interested in: {service}
                
                Message:
                {message}
                
                Please follow up within 24 hours.
                """
                
                if send_email(EMAIL, f"Consultation Request from {name}", email_body):
                    st.success("Request submitted! We'll contact you within 24 hours.")
                else:
                    st.error("Failed to send request. Please try again or contact us directly.")
            else:
                st.warning("Please provide at least your name and email address.")

def training_page():
    st.title("IT Training Programs")
    st.subheader("Empowering IT Professionals with Cutting-Edge Skills")
    
    st.markdown(f"""
    {COMPANY_NAME} offers comprehensive IT training programs designed to help you:
    - Master in-demand technologies
    - Increase your earning potential
    - Transition to high-paying IT roles
    - Advance your career in just 90-120 days
    """)
    
    st.markdown("---")
    st.subheader("Our Training Categories")
    
    selected_category = st.selectbox(
        "Select a training category to explore:",
        list(TRAINING_COURSES.keys())
    
    st.markdown(f"### {selected_category} Courses")
    
    for course in TRAINING_COURSES[selected_category]:
        with st.expander(course):
            st.markdown(f"""
            **Duration:** {random.randint(4, 8)} weeks  
            **Level:** {random.choice(["Beginner", "Intermediate", "Advanced"])}  
            **Price:** ${random.randint(1000, 3500)} (payment plans available)
            
            This comprehensive course will teach you everything you need to know about {course.split(':')[0]}.
            By the end, you'll be ready for high-paying roles in this technology.
            
            [Learn More](#)
            """)
    
    st.markdown("---")
    st.subheader("Training Program Highlights")
    
    highlights = [
        "Hands-on, project-based learning",
        "Industry-expert instructors",
        "Flexible scheduling (full-time or part-time)",
        "Job placement assistance",
        "Money-back guarantee if you don't land a six-figure job within 6 months"
    ]
    
    for hl in highlights:
        st.markdown(f"- {hl}")
    
    st.markdown("---")
    st.subheader("Ready to Enroll?")
    
    with st.form("training_interest"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        interest = st.selectbox(
            "Which program are you interested in?",
            [course for courses in TRAINING_COURSES.values() for course in courses]
        )
        schedule = st.radio(
            "Preferred schedule:",
            ["Full-time (90 days)", "Part-time (120 days)"]
        )
        
        submitted = st.form_submit_button("Get More Information")
        if submitted:
            if name and email:
                email_body = f"""
                New training interest from {name}.
                
                Interested in: {interest}
                Preferred schedule: {schedule}
                
                Contact Information:
                Email: {email}
                Phone: {phone}
                
                Please send more information about this program.
                """
                
                if send_email(EMAIL, f"Training Interest from {name}", email_body):
                    st.success("Request received! We'll send you more information shortly.")
                else:
                    st.error("Failed to send request. Please try again or contact us directly.")
            else:
                st.warning("Please provide at least your name and email address.")

def recruiting_page():
    st.title("IT Recruitment Services")
    st.subheader("Connecting Top Talent with Leading Companies")
    
    st.markdown(f"""
    {COMPANY_NAME} Recruiting specializes in matching skilled IT professionals with businesses 
    looking for top talent in:
    - Operating systems
    - Databases
    - DevOps
    - Cloud platforms (AWS)
    """)
    
    st.markdown("---")
    st.subheader("Our Recruitment Services")
    
    services = [
        "Resume Help, Writing, and Coaching",
        "Job Search and Placement Assistance",
        "Interview Preparation",
        "Salary Negotiation Coaching",
        "Career Transition Support"
    ]
    
    for service in services:
        st.markdown(f"- {service}")
    
    st.markdown("---")
    st.subheader("Job Categories We Place")
    
    cols = st.columns(3)
    for i, job in enumerate(JOB_CATEGORIES):
        cols[i%3].markdown(f"- {job}")
    
    st.markdown("---")
    st.subheader("Are You a Job Seeker or Employer?")
    
    option = st.radio(
        "I am:",
        ["An IT professional looking for opportunities", 
         "A company looking to hire IT talent"]
    )
    
    if option == "An IT professional looking for opportunities":
        with st.form("job_seeker_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            current_role = st.text_input("Current Job Title")
            experience = st.slider("Years of Experience", 0, 20, 2)
            skills = st.text_area("Technical Skills (comma separated)")
            target_roles = st.multiselect(
                "Roles you're interested in:",
                JOB_CATEGORIES
            )
            resume = st.file_uploader("Upload Resume (PDF or DOCX)")
            
            submitted = st.form_submit_button("Submit Profile")
            if submitted:
                if name and email and (skills or resume):
                    email_body = f"""
                    New job seeker profile: {name}
                    
                    Current Role: {current_role}
                    Experience: {experience} years
                    Skills: {skills}
                    Target Roles: {', '.join(target_roles)}
                    
                    Contact Information:
                    Email: {email}
                    Phone: {phone}
                    
                    Resume: {'Attached' if resume else 'Not provided'}
                    """
                    
                    if send_email(EMAIL, f"Job Seeker Profile: {name}", email_body):
                        st.success("Profile submitted! Our recruiters will review your information and contact you soon.")
                    else:
                        st.error("Failed to submit profile. Please try again or contact us directly.")
                else:
                    st.warning("Please provide at least your name, email, and skills or resume.")
    
    else:  # Employer form
        with st.form("employer_form"):
            company = st.text_input("Company Name")
            contact_name = st.text_input("Your Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            hiring_needs = st.text_area("Describe your hiring needs")
            number_positions = st.number_input("Number of positions to fill", 1, 100, 1)
            target_roles = st.multiselect(
                "Roles you're hiring for:",
                JOB_CATEGORIES
            )
            
            submitted = st.form_submit_button("Request Talent")
            if submitted:
                if company and contact_name and email:
                    email_body = f"""
                    New hiring request from {company}.
                    
                    Contact: {contact_name}
                    Email: {email}
                    Phone: {phone}
                    
                    Hiring Needs:
                    {hiring_needs}
                    
                    Number of Positions: {number_positions}
                    Target Roles: {', '.join(target_roles)}
                    """
                    
                    if send_email(EMAIL, f"Hiring Request from {company}", email_body):
                        st.success("Request submitted! Our recruitment team will contact you within 24 hours.")
                    else:
                        st.error("Failed to submit request. Please try again or contact us directly.")
                else:
                    st.warning("Please provide at least company name, your name, and email address.")

def booking_page():
    st.title("Schedule a Consultation or Assessment")
    
    st.markdown("""
    Book a free consultation or career assessment with one of our experts.
    We'll evaluate your current skills and help you create a roadmap to your six-figure IT career.
    """)
    
    with st.form("booking_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        
        service = st.radio(
            "Service you're interested in:",
            ["Free Career Assessment", 
             "Training Program Consultation",
             "Recruiting Services",
             "Business IT Consulting"]
        )
        
        date = st.date_input(
            "Preferred Date",
            min_value=datetime.date.today(),
            max_value=datetime.date.today() + datetime.timedelta(days=30)
        )
        
        available_times = [
            "9:00 AM - 10:00 AM",
            "10:30 AM - 11:30 AM",
            "1:00 PM - 2:00 PM",
            "2:30 PM - 3:30 PM",
            "4:00 PM - 5:00 PM"
        ]
        
        time_slot = st.selectbox("Preferred Time Slot", available_times)
        
        submitted = st.form_submit_button("Book Appointment")
        if submitted:
            if name and email and date:
                email_body = f"""
                New appointment booking from {name}.
                
                Service: {service}
                Date: {date.strftime('%A, %B %d, %Y')}
                Time: {time_slot}
                
                Contact Information:
                Email: {email}
                Phone: {phone}
                
                Please confirm this appointment via email or phone.
                """
                
                if send_email(EMAIL, f"Appointment Booking from {name}", email_body):
                    st.success("Appointment booked! You'll receive a confirmation shortly.")
                else:
                    st.error("Failed to book appointment. Please try again or contact us directly.")
            else:
                st.warning("Please provide at least your name, email, and select a date.")

def payment_page():
    st.title("Payment Options")
    
    st.markdown("""
    Choose your preferred payment option for our training programs.
    We offer flexible payment plans to make your career transformation affordable.
    """)
    
    program = st.selectbox(
        "Select your training program:",
        [course for courses in TRAINING_COURSES.values() for course in courses]
    )
    
    st.markdown(f"### Pricing for {program.split(':')[0]}")
    
    payment_option = st.radio(
        "Select payment option:",
        ["Full Payment ($3,500 - Save $500)", 
         "3-Month Installment Plan ($1,500 first month, then $1,000/month)"]
    )
    
    if payment_option.startswith("Full"):
        st.markdown("**Total:** $3,500 (one-time payment)")
        payment_link = create_payment_link(3500)
    else:
        st.markdown("""
        **Payment Schedule:**
        - Month 1: $1,500
        - Month 2: $1,000
        - Month 3: $1,000
        **Total:** $3,500
        """)
        payment_link = create_payment_link(1500, installments=True)
    
    st.markdown("---")
    
    if st.button("Proceed to Payment"):
        webbrowser.open_new_tab(payment_link)
        st.success("Redirecting to secure payment portal...")

def social_media_page():
    st.title("Social Media Promotions")
    st.subheader(f"{AGENT_NAME} Social Media Management")
    
    promo_text = generate_promo_text()
    
    st.markdown("### Generated Promo Text (George Carlin Style)")
    st.text_area("Promo Copy", promo_text, height=200)
    
    platforms = st.multiselect(
        "Select platforms to post to:",
        ["Twitter", "Facebook", "LinkedIn", "Instagram", "Reddit"],
        ["Twitter", "Facebook", "LinkedIn"]
    )
    
    if st.button("Post to Selected Platforms"):
        with st.spinner("Posting to social media..."):
            for platform in platforms:
                time.sleep(1)  # Simulate API delay
                st.success(f"Posted to {platform}: {promo_text[:50]}...")
    
    st.markdown("---")
    st.subheader("Social Media Performance")
    
    # Simulated analytics
    data = {
        "Platform": ["Twitter", "Facebook", "LinkedIn", "Instagram", "Reddit"],
        "Posts": [12, 8, 15, 10, 5],
        "Engagement": [345, 420, 580, 390, 210],
        "Leads Generated": [28, 32, 45, 22, 15]
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df)
    
    st.markdown("---")
    st.subheader("Schedule Future Posts")
    
    with st.form("schedule_post"):
        post_content = st.text_area("Post Content", promo_text)
        post_date = st.date_input("Schedule Date")
        post_time = st.time_input("Schedule Time")
        platforms = st.multiselect("Platforms", data["Platform"])
        
        if st.form_submit_button("Schedule Post"):
            st.success(f"Post scheduled for {post_date} at {post_time} on {', '.join(platforms)}")

def admin_dashboard():
    st.title(f"{AGENT_NAME} Admin Dashboard")
    
    st.markdown("### Agent Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Send Follow-up Emails"):
            # Simulate sending follow-ups
            time.sleep(2)
            st.success("Sent 25 follow-up emails to prospective students")
    
    with col2:
        if st.button("Post Daily Promo"):
            post_to_social_media(generate_promo_text())
    
    with col3:
        if st.button("Update Course Listings"):
            st.success("Course listings updated across all platforms")
    
    st.markdown("---")
    st.subheader("Recent Activity")
    
    # Simulated activity log
    activities = [
        {"time": "10:30 AM", "action": "Posted to Twitter", "details": "New AWS course promo"},
        {"time": "9:45 AM", "action": "Sent emails", "details": "15 follow-ups to leads"},
        {"time": "Yesterday", "action": "Processed payments", "details": "3 new enrollments"},
        {"time": "Yesterday", "action": "Scheduled posts", "details": "5 posts for next week"}
    ]
    
    for activity in activities:
        st.markdown(f"""
        **{activity['time']}** - *{activity['action']}*  
        {activity['details']}
        """)

# Main app logic
def main():
    st.sidebar.title(f"{AGENT_NAME} Agent")
    st.sidebar.image("https://via.placeholder.com/150?text=SITM", width=100)
    
    menu_options = {
        "Home": "home",
        "Consulting Services": "consulting",
        "Training Programs": "training",
        "Recruiting Services": "recruiting",
        "Book Appointment": "booking",
        "Payment Options": "payment",
        "Social Media": "social",
        "Admin Dashboard": "admin"
    }
    
    selection = st.sidebar.radio("Navigation", list(menu_options.keys()))
    st.session_state.page = menu_options[selection]
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Contact Information")
    st.sidebar.markdown(f"""
    {COMPANY_NAME}  
    {ADDRESS}  
    {EMAIL}  
    {PHONE}  
    """)
    
    # Display the selected page
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'consulting':
        consulting_page()
    elif st.session_state.page == 'training':
        training_page()
    elif st.session_state.page == 'recruiting':
        recruiting_page()
    elif st.session_state.page == 'booking':
        booking_page()
    elif st.session_state.page == 'payment':
        payment_page()
    elif st.session_state.page == 'social':
        social_media_page()
    elif st.session_state.page == 'admin':
        admin_dashboard()

if __name__ == "__main__":
    main()
