import streamlit as st
import os

# Set Page Configuration
st.set_page_config(page_title="Manish Choudhary | Portfolio", page_icon="📊", layout="wide")

# Sidebar with Profile Info
with st.sidebar:
    st.image("Profile_Image.jpg")  # Replace with your profile image URL
    st.title("Manish Choudhary")
    st.write("📊 Data Scientist | AI & ML Enthusiast | Data Analyst ")
    st.write("📍 Boston, MA")
    st.write("📧 [choudhary.man@northeastern.edu](mailto:choudhary.man@northeastern.edu)")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/manish-choudhary-bch7/)")
    st.write("💻 [GitHub](https://github.com/manishch7/Finlysis)")

# Main Section
st.title("🚀 Welcome to My Portfolio")

st.markdown("""
# 👨‍💻 About Me

🚀 **Data Enthusiast | AI Explorer | ML Engineer**  

I am a **data-driven innovator** with a passion for **AI, data engineering, and predictive analytics**. Currently pursuing a **Master’s in Data Architecture & Management at Northeastern University**, I specialize in:  

🔹 **Building scalable data pipelines** with Python, SQL, Spark, and Airflow  
🔹 **Designing AI-driven analytics** for business intelligence & automation  
🔹 **Developing predictive models** to uncover hidden insights  
🔹 **Creating interactive dashboards** with Tableau, Power BI & Flask  

⚡ I love solving real-world problems with **machine learning, automation, and big data** to drive efficiency and impact.  

📊 Let’s turn **data into decisions, models into action, and AI into innovation!**  
""", unsafe_allow_html=True)

st.markdown("---")

# Experience Section
st.markdown("## **📌 Work Experience**")

exp_data = [
    {
        "role": "Data Analyst",
        "company": "Kroll, Mumbai",
        "years": "Sep 2022 – Jul 2023",
        "details": [
            "📊 Engineered a **scalable data ingestion pipeline** using Pandas, improving case processing efficiency.",
            "🚀 Designed and deployed a **supervised learning model** integrating statistical analysis and anomaly detection for fraud detection.",
            "📈 Developed **real-time dashboards** in **Tableau and Power BI**, enhancing data accessibility for legal and compliance teams.",
            "✅ Automated compliance report generation using **Python & SQL**, reducing manual effort and ensuring accurate reporting.",
            "🤝 Collaborated with legal, IT, and compliance teams to **reinforce data-driven decision-making** for class action settlements."
        ]
    },
    {
        "role": "Jr. Data Scientist",
        "company": "BLC Logistics, Mumbai",
        "years": "May 2020 – Aug 2022",
        "details": [
            "🔧 Developed a **predictive maintenance model** with Python, SQL, Kafka, and Spark to improve fleet uptime.",
            "🛣️ Built an **ETL pipeline in Airflow** to integrate live traffic and fuel data from Snowflake, optimizing route efficiency.",
            "📦 Applied **statistical forecasting** techniques on supply data to improve warehouse turnover.",
            "📊 Created an **interactive dashboard using Flask & FastAPI**, visualizing fleet KPIs to track efficiency, idle times, and costs.",
            "⚡ Implemented a **comprehensive ETL workflow** with Airflow, AWS, and Spark, automating fleet data processing."
        ]
    },
    {
        "role": "Financial Analyst Intern",
        "company": "Motilal Oswal, Thane",
        "years": "Apr 2019 – Jul 2019",
        "details": [
            "📈 Conducted **data-driven equity research**, analyzing financial statements and automating data extraction using Python & Excel.",
            "📊 Built **predictive models** for investment insights to support decision-making."
        ]
    }
]

for exp in exp_data:
    col1, col2 = st.columns([0.8, 0.2])  # Splitting the section into two columns
    with col1:
        st.subheader(f"{exp['role']} - {exp['company']}")
    with col2:
        st.markdown(f"<p style='text-align: right; font-size: 0.9em; font-style: italic;'>{exp['years']}</p>", unsafe_allow_html=True)
    
    for point in exp["details"]:
        st.write(f"- {point}")

st.markdown("---")

# Projects Section
st.markdown("## **🛠️ Projects**")

project_data = [
    {
        "name": "Asynchronous Twitter Scraper (Jan 2025 – Present)",
        "tech": "Python, Twikit, CSV",
        "desc": "Developed a real-time scraper to fetch and analyze brand mentions (Nike, Adidas, Under Armour). Implemented rate-limit handling, extracted key data points (hashtags, mentions, URLs), and optimized for efficiency with a modular design."
    },
    {
        "name": "Chain of Thought Prompt Pattern Exploration (Jan 2025 – Feb 2025)",
        "tech": "Prompt Engineering, AI, Educational Content",
        "desc": "Developed an interactive website to elucidate the Chain of Thought (CoT) prompt pattern, featuring practical examples and analyses. Created engaging songs to simplify CoT concepts, enhancing accessibility and understanding."
    },
    {
        "name": "Julia's Culinary Companion Bot (Jan 2025 – Feb 2025)",
        "tech": "Python, Perplexity AI",
        "desc": "Developed an AI-powered cooking assistant that provides step-by-step recipes, ingredient substitutions, and meal planning tips. Emulated Julia Child's engaging teaching style to enhance user experience."
    },
    {
        "name": "Financial & News Analysis Chatbot (Dec 2024 – Jan 2025)",
        "tech": "GPT-4o-mini, LSTM, DistilRoBERTa, Neo4j, Streamlit",
        "desc": "Developed an AI-powered chatbot integrating stock trends, news sentiment, and financial data for smart investment insights."
    },
    {
        "name": "Service Request Analytics: Kansas City 311 Calls (Mar 2024 – Apr 2024)",
        "tech": "Alteryx, Power BI, Tableau",
        "desc": "Staged and profiled data with Alteryx, reducing preparation time by **20%**. Built dashboards in Power BI & Tableau, delivering insights that improved efficiency by **30%**."
    },
    {
        "name": "Motor Vehicle Collision Analysis (Jan 2024 – Mar 2024)",
        "tech": "Alteryx, Talend, SQL, Tableau, Power BI",
        "desc": "Processed crash data from multiple cities, creating interactive dashboards that improved data visibility."
    },
    {
        "name": "Dabba On Wheels - Food Delivery Database (Sept 2023 – Dec 2023)",
        "tech": "Oracle, PL/SQL",
        "desc": "Developed a scalable food delivery database with optimized subscription payments and order workflow."
    }
]


for project in project_data:
    with st.expander(f"📌 {project['name']}"):
        st.write(f"**Tech Used:** {project['tech']}")
        st.write(f"**Description:** {project['desc']}")

st.markdown("---")

# Skills Section
st.markdown("## **💡 Skills**")

skills = {
    "Programming & Data Analysis": "Python (Pandas, NumPy), SQL (Oracle, Snowflake), VBA",
    "Machine Learning & AI": "Scikit-learn, TensorFlow, PyTorch, Hugging Face Transformers",
    "Data Engineering & Visualization": "Tableau, Power BI, Plotly, Alteryx, Talend, Spark, Kafka, Seaborn",
    "Cloud & Big Data": "AWS, GCP, Azure, Neo4j, Snowflake",
    "Other Tools": "Git, Streamlit, Airflow, Jupyter Notebooks"
}

for skill, details in skills.items():
    st.write(f"✅ **{skill}:** {details}")

st.markdown("---")

# Education Section
st.markdown("## **🎓 Education**")

edu_data = [
    {
        "degree": "Master of Science in Data Architecture & Management",
        "institution": "Northeastern University, Boston",
        "year": "May 2025",
        "courses": "Parallel ML & AI, Generative AI, Data Engineering, LLM with Knowledge Graphs"
    },
    {
        "degree": "Bachelor of Management Studies",
        "institution": "Mumbai University",
        "year": "April 2021"
    }
]

for edu in edu_data:
    st.subheader(f"{edu['degree']} - {edu['institution']} ")
    if "courses" in edu:
        st.write(f"**Relevant Coursework:** {edu['courses']}")

st.markdown("---")

# Contact Section
st.markdown("## **📞 Let's Connect!**")

contact_info = {
    "📧 Email": "[choudhary.man@northeastern.edu](mailto:choudhary.man@northeastern.edu)",
    "🔗 LinkedIn": "[linkedin.com/in/manish-choudhary-bch7](https://www.linkedin.com/in/manish-choudhary-bch7/)",
    "💻 GitHub": "[github.com/manishch7/Finlysis](https://github.com/manishch7/Finlysis)"
}

for key, value in contact_info.items():
    st.write(f"{key}: {value}")

st.markdown("🚀 **Thanks for visiting my portfolio! Feel free to reach out.**")

st.snow() # Add snow effect to the page
