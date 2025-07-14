import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
import time
import json
import plotly.express as px
from PIL import Image

# ======================
# 🧩 CUSTOM MODULES
# ======================

class Faker:
    """Custom data generator to avoid external dependencies"""
    def __init__(self):
        self.first_names = ["Alex", "Jamie", "Taylor", "Casey", "Morgan", "Jordan"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
        self.companies = ["Tech", "Solutions", "Global", "Innovations", "Data"]
        self.jobs = ["Cloud Engineer", "DevOps", "DBA", "Solutions Architect"]
        self.cities = ["Atlanta", "New York", "Chicago", "Austin", "London", "Berlin"]
        self.universities = ["Georgia Tech", "NYU", "Stanford", "MIT", "University of Lagos"]
        
    def name(self):
        return f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
    
    def email(self, name=None):
        name = name or self.name().replace(" ", "").lower()
        return f"{name}{random.randint(10,99)}@example.com"
    
    def phone(self):
        return f"{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}"
    
    def company(self):
        return f"{random.choice(self.companies)} {random.choice(['Inc', 'LLC', 'Corp'])}"
    
    def date(self, days=365):
        return (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, days))).strftime("%Y-%m-%d")

class SITM:
    """Core automation engine"""
    def __init__(self):
        self.fake = Faker()
        self.training_programs = {
            "AWS": {"price": 3500, "duration": "12 weeks", "placement": 0.92},
            "DevOps": {"price": 4000, "duration": "14 weeks", "placement": 0.89},
            "Database": {"price": 3200, "duration": "10 weeks", "placement": 0.85}
        }
        self.countries = ["US", "Canada", "UK", "Germany", "Nigeria", "South Africa"]
        self.social_media = ["LinkedIn", "Twitter", "Facebook", "Instagram", "YouTube"]
        self.payment_methods = ["Credit Card", "Affirm", "Klarna", "County Sponsorship"]
        
    def generate_leads(self, n=1000, lead_type="student"):
        leads = []
        for _ in range(n):
            if lead_type == "student":
                leads.append({
                    "Name": self.fake.name(),
                    "Email": self.fake.email(),
                    "Phone": self.fake.phone(),
                    "Location": random.choice(self.fake.cities),
                    "Source": random.choice(["LinkedIn", "University", "Meetup"]),
                    "Interest": random.choice(list(self.training_programs.keys())),
                    "Status": "New"
                })
            else:  # Corporate clients
                leads.append({
                    "Company": self.fake.company(),
                    "Contact": self.fake.name(),
                    "Email": self.fake.email(),
                    "Phone": self.fake.phone(),
                    "Employees": random.randint(50, 5000),
                    "Budget": f"${random.randint(5000, 50000)}",
                    "Needs": random.choice(["Training", "Consulting", "Recruiting"])
                })
        return pd.DataFrame(leads)
    
    def create_content(self, content_type, topic=None):
        templates = {
            "email": {
                "student": f"""Subject: Launch Your {topic} Career in 90 Days!

Hi {{name}},

Our {topic} program at {COMPANY_NAME} has helped 1,200+ students land $100K+ jobs.

Key benefits:
✅ {self.training_programs[topic]['duration']} hands-on training
✅ 92% job placement rate
✅ Flexible payment options

Next cohort starts: {self.fake.date(14)}

Reply to schedule a call!

Best,
{AGENT_NAME}""",
                
                "corporate": f"""Subject: Enterprise {topic} Solutions

Hi {{name}},

We help companies like {{company}} upskill teams in {topic} with:

• Customized training programs
• Certified instructors
• On-site/virtual options

Average results:
• 40% faster deployments
• 30% cost reduction

Available for immediate deployment.

Best,
{AGENT_NAME}"""
            },
            "social": {
                "LinkedIn": f"""🚀 New {topic} Cohort Opening!

{self.training_programs[topic]['duration']} • {self.training_programs[topic]['placement']*100}% Placement • ${random.randint(80,150)}k Avg Salary

📍 {random.choice(self.fake.cities)}
📅 {self.fake.date(14)}

#TechCareers #Learn{topic}""",
                
                "Twitter": f"""Go from beginner to hired in {self.training_programs[topic]['duration']}!

{COMPANY_NAME} {topic} Training → ${random.randint(80,150)}k salary

🔗 soliditminds.com/{topic.lower()}"""
            }
        }
        return templates.get(content_type, {})

# ======================
# 🏗️ SYSTEM CONFIG
# ======================
COMPANY_NAME = "SolidITMinds"
AGENT_NAME = "SITM (SaiTim)"
sitm = SITM()

# Initialize session state
if 'leads' not in st.session_state:
    st.session_state.leads = {}
if 'campaigns' not in st.session_state:
    st.session_state.campaigns = []

# ======================
# 🖥️ STREAMLIT UI
# ======================
st.set_page_config(layout="wide", page_title=f"{AGENT_NAME} | {COMPANY_NAME}")
st.title(f"🚀 {AGENT_NAME} - IT Training Automation Platform")

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://via.placeholder.com/200x50?text=SolidITMinds", width=200)
    st.write(f"**{COMPANY_NAME} Control Panel**")
    
    menu = st.radio("Navigation", [
        "📊 Dashboard", 
        "📈 Lead Engine", 
        "✉️ Campaigns", 
        "💰 Payments",
        "👔 Placements",
        "⚙️ System"
    ])
    
    st.markdown("---")
    st.metric("Total Leads", "1,842,759")
    st.metric("Active Campaigns", "37")
    st.metric("Revenue", "$8.2M", "18% MoM")
    
    if st.button("🔄 Sync All Data"):
        with st.spinner("Syncing 12 systems..."):
            time.sleep(2)
            st.success("All systems synchronized!")

# --- DASHBOARD ---
if menu == "📊 Dashboard":
    st.header("📊 Executive Dashboard")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Students Trained", "8,742", "1,248 this month")
    with col2:
        st.metric("Avg Salary Increase", "$48,500", "12% YoY")
    with col3:
        st.metric("Corporate Clients", "427", "38 new")
    
    # Visualizations
    tab1, tab2 = st.tabs(["Program Performance", "Geographic Reach"])
    with tab1:
        program_data = pd.DataFrame([
            {
                "Program": program,
                "Students": random.randint(500, 2500),
                "Placement Rate": details["placement"]*100,
                "Avg Salary": random.randint(80, 150)
            }
            for program, details in sitm.training_programs.items()
        ])
        st.plotly_chart(px.bar(
            program_data,
            x="Program",
            y=["Students", "Placement Rate"],
            title="Training Program Performance",
            barmode="group"
        ), use_container_width=True)
    
    with tab2:
        geo_data = pd.DataFrame({
            "Country": sitm.countries,
            "Students": [random.randint(1000, 5000) for _ in sitm.countries],
            "Revenue ($M)": [round(random.uniform(0.5, 3.2), 1) for _ in sitm.countries]
        })
        st.plotly_chart(px.choropleth(
            geo_data,
            locations="Country",
            locationmode="country names",
            color="Revenue ($M)",
            hover_name="Country",
            title="Global Training Reach"
        ), use_container_width=True)

# --- LEAD ENGINE ---
elif menu == "📈 Lead Engine":
    st.header("⚡ Multi-Source Lead Generation")
    
    tab1, tab2, tab3 = st.tabs(["Students", "Corporate", "Government"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("University Outreach")
            if st.button("🎓 Scrape 50K Student Leads"):
                with st.spinner("Generating leads..."):
                    st.session_state.leads['students'] = sitm.generate_leads(50000)
                    st.success(f"Generated {len(st.session_state.leads['students'])} student leads!")
            
            if st.button("📱 Extract Phone Numbers"):
                st.warning("This would integrate with Twilio API in production")
        
        with col2:
            st.subheader("Lead Management")
            if 'students' in st.session_state.leads:
                st.dataframe(st.session_state.leads['students'].head(10))
                if st.button("📤 Export Student Leads"):
                    st.success("Exported to CRM!")
    
    with tab2:
        st.subheader("Corporate Lead Generation")
        if st.button("🏢 Generate 10K Client Leads"):
            st.session_state.leads['corporate'] = sitm.generate_leads(10000, "corporate")
            st.dataframe(st.session_state.leads['corporate'].head(10))
    
    with tab3:
        st.subheader("Government Partnerships")
        st.write("Automated county outreach system")
        if st.button("🏛️ Contact 500+ Counties"):
            counties = pd.DataFrame([{
                "County": f"{county} County",
                "Contact": sitm.fake.name(),
                "Email": sitm.fake.email(),
                "Phone": sitm.fake.phone(),
                "Unemployment Rate": f"{random.uniform(3.5, 9.2):.1f}%",
                "Status": random.choice(["Pending", "Contacted", "Approved"])
            } for county in ["Fulton", "Gwinnett", "Cobb", "DeKalb", "Broward", "Harris"]])
            st.session_state.leads['government'] = counties
            st.dataframe(counties)

# --- CAMPAIGNS ---
elif menu == "✉️ Campaigns":
    st.header("📢 Multi-Channel Campaign Manager")
    
    tab1, tab2, tab3 = st.tabs(["Email", "Social", "SMS"])
    with tab1:
        st.subheader("Email Campaigns")
        campaign_type = st.radio("Audience", ["Students", "Corporate"], horizontal=True)
        program = st.selectbox("Program", list(sitm.training_programs.keys()))
        
        template = sitm.create_content("email", "student" if campaign_type == "Students" else "corporate").get(program, "")
        st.text_area("Email Template", template, height=300)
        
        if st.button("🚀 Launch to 50K Contacts"):
            st.session_state.campaigns.append({
                "type": "email",
                "audience": campaign_type,
                "program": program,
                "sent": datetime.datetime.now().strftime("%Y-%m-%d")
            })
            st.success(f"Email campaign launched to {random.randint(45000,55000)} contacts!")
    
    with tab2:
        st.subheader("Social Media Automation")
        platform = st.selectbox("Platform", sitm.social_media)
        program = st.selectbox("Program", list(sitm.training_programs.keys()))
        
        post = sitm.create_content("social", platform).get(program, "")
        st.text_area("Post Content", post, height=200)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save Draft"):
                st.success("Draft saved!")
        with col2:
            if st.button("📅 Schedule Post"):
                st.session_state.campaigns.append({
                    "type": "social",
                    "platform": platform,
                    "program": program,
                    "scheduled": datetime.datetime.now().strftime("%Y-%m-%d")
                })
                st.success(f"Post scheduled for {platform}!")
    
    with tab3:
        st.subheader("SMS Blasting")
        st.write("Integrated with Twilio API in production")
        sms_template = st.text_area("SMS Template", 
            "Hi {name}! Our {program} training can help you earn ${salary}k. Reply YES for info!")
        
        if st.button("📲 Send to 10K Contacts"):
            st.session_state.campaigns.append({
                "type": "sms",
                "contacts": random.randint(9500,10500),
                "sent": datetime.datetime.now().strftime("%Y-%m-%d")
            })
            st.success(f"SMS sent to {random.randint(9500,10500)} contacts!")

# --- PAYMENTS ---
elif menu == "💰 Payments":
    st.header("💳 Integrated Payment Processing")
    
    with st.form("payment_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            program = st.selectbox("Program", list(sitm.training_programs.keys()))
        with col2:
            amount = st.number_input("Amount", value=sitm.training_programs[program]["price"])
            method = st.selectbox("Payment Method", sitm.payment_methods)
            if method in ["Affirm", "Klarna"]:
                st.write(f"Monthly payment: ${amount/6:.2f} for 6 months")
        
        if st.form_submit_button("💳 Process Payment"):
            payment = {
                "id": f"TX-{random.randint(100000,999999)}",
                "name": name,
                "email": email,
                "program": program,
                "amount": amount,
                "method": method,
                "status": "Approved",
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            st.session_state.campaigns.append({"type": "payment", "data": payment})
            st.json(payment)
            st.balloons()
            st.success("Enrollment confirmed!")

# --- PLACEMENTS ---
elif menu == "👔 Placements":
    st.header("📊 Job Placement Analytics")
    
    # Generate fake placement data
    placements = []
    for _ in range(500):
        program = random.choice(list(sitm.training_programs.keys()))
        placements.append({
            "Name": sitm.fake.name(),
            "Program": program,
            "Company": sitm.fake.company(),
            "Position": f"{program} {random.choice(['Engineer', 'Architect', 'Specialist'])}",
            "Salary": f"${random.randint(80, 180)}k",
            "Hired": sitm.fake.date(180),
            "Location": random.choice(sitm.fake.cities)
        })
    
    df = pd.DataFrame(placements)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        program_filter = st.multiselect("Filter by Program", list(sitm.training_programs.keys()))
    with col2:
        salary_range = st.slider("Salary Range", 80, 180, (100, 150))
    with col3:
        location_filter = st.multiselect("Location", sitm.fake.cities)
    
    # Apply filters
    if program_filter:
        df = df[df["Program"].isin(program_filter)]
    df = df[df["Salary"].str.replace('k','').astype(int).between(*salary_range)]
    if location_filter:
        df = df[df["Location"].isin(location_filter)]
    
    # Display
    st.dataframe(df.head(20))
    
    # Visualizations
    fig = px.box(
        df.assign(Salary=df["Salary"].str.replace('k','').astype(int)),
        x="Program",
        y="Salary",
        color="Program",
        title="Salary Distribution by Program"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- SYSTEM ---
elif menu == "⚙️ System":
    st.header("⚙️ System Configuration")
    
    tab1, tab2 = st.tabs(["API Connections", "Automation Rules"])
    with tab1:
        st.subheader("Third-Party Integrations")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**CRM Integration**")
            st.selectbox("CRM System", ["Salesforce", "HubSpot", "Zoho"])
            st.toggle("Sync Contacts", True)
            
            st.write("**Payment Processors**")
            st.multiselect("Enabled Gateways", ["Stripe", "PayPal", "Affirm", "Klarna"])
        
        with col2:
            st.write("**Communication APIs**")
            st.selectbox("SMS Provider", ["Twilio", "Plivo", "Vonage"])
            st.selectbox("Email Service", ["SendGrid", "Mailchimp", "AWS SES"])
            
            st.write("**Calendar Integration**")
            st.selectbox("Scheduling System", ["Calendly", "Microsoft Bookings"])

