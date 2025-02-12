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

st.markdown("## **About Me**")
st.write(
    "I am a passionate **Data Analyst & Jr. Data Scientist** with expertise in **data engineering, machine learning, "
    "and AI-driven analytics**. With a Master's degree in **Data Architecture and Management** from **Northeastern University**, "
    "I specialize in **predictive modeling, data visualization, and automation** to drive business efficiency and insights."
)

st.markdown("---")

# Experience Section
st.markdown("## **📌 Work Experience**")

exp_data = [
    {
        "role": "Data Analyst",
        "company": "KROLL, Mumbai",
        "years": "1 year",
        "details": [
            "📊 Automated data pipeline reducing case processing time by **40%**.",
            "🚀 Developed fraud detection models, improving accuracy by **25%**.",
            "📈 Designed interactive **Tableau and Power BI dashboards**, enhancing real-time data access by **60%**.",
            "✅ Automated compliance report generation with Python & SQL, reducing manual work by **70%**."
        ]
    },
    {
        "role": "Jr. Data Scientist",
        "company": "BLC Logistics, Mumbai",
        "years": "2 years",
        "details": [
            "🔧 Developed **predictive maintenance models**, reducing breakdowns by **18%**.",
            "🛣️ Built **ETL pipeline in Airflow**, reducing fuel costs by **12%**.",
            "📦 Designed **demand forecasting models**, improving warehouse efficiency by **20%**.",
            "📊 Created real-time dashboards to track fleet KPIs, optimizing operations by **10%**."
        ]
    },
    {
        "role": "Research Analyst Intern",
        "company": "Motilal Oswal Financial Services, Mumbai",
        "years": "3 months",
        "details": [
            "📊 Conducted **data-driven equity research** by analyzing financial statements.",
            "🛠 Built **predictive models** to enhance investment insights.",
            "🔄 Automated **data extraction using Python and Excel**, improving research efficiency."
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
        "name": "Financial & News Analysis Chatbot",
        "tech": "GPT-4o-mini, LSTM, DistilRoBERTa, Neo4j, Streamlit",
        "desc": "Developed an AI-powered chatbot integrating stock trends, news sentiment, and financial data for smart investment insights."
    },
    {
        "name": "Chain of Thought Prompt Pattern Exploration",
        "tech": "Prompt Engineering, AI, Educational Content",
        "desc": "Developed an interactive website to elucidate the Chain of Thought (CoT) prompt pattern, featuring practical examples and analyses. Created engaging songs to simplify CoT concepts, enhancing accessibility and understanding."
    }
    {
        "name": "Motor Vehicle Collision Analysis",
        "tech": "Alteryx, Talend, SQL, Tableau, Power BI",
        "desc": "Processed crash data from multiple cities, creating interactive dashboards that improved data visibility by **30%**."
    },
    {
        "name": "Dabba On Wheels - Food Delivery Database",
        "tech": "Oracle, PL/SQL",
        "desc": "Developed a scalable food delivery database with optimized subscription payments and order workflow."
    }
    {
        "name": "Asynchronous Twitter Scraper",
        "tech": "Python, Twikit, CSV",
        "desc": "Developed a real-time scraper to fetch and analyze brand mentions (Nike, Adidas, Under Armour). Implemented rate-limit handling, extracted key data points (hashtags, mentions, URLs), and optimized for efficiency with a modular design."
    }
    {
        "name": "Service Request Analytics: Kansas City 311 Calls",
        "tech": "Alteryx, Power BI, Tableau",
        "desc": "Staged and profiled data with Alteryx, reducing preparation time by **20%**. Built dashboards in Power BI & Tableau, delivering insights that improved efficiency by **30%**."
    }
    {
        "name": "Julia's Culinary Companion Bot",
        "tech": "Python, Perplexity AI",
        "desc": "Developed an AI-powered cooking assistant that provides step-by-step recipes, ingredient substitutions, and meal planning tips. Emulated Julia Child's engaging teaching style to enhance user experience."
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
