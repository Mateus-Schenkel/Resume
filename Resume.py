import streamlit as st
from pathlib import Path
from PIL import Image

# --- Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_EN = current_dir / "assets" /"resume.pdf"
resume_file_PT = current_dir / "assets" /"curriculo.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- General Settings
PAGE_TITLE = "Digital Resume | Mateus Schenkel"
PAGE_ICON = ":wave:"
NAME = "Mateus Schenkel"
DESCRIPTION = """
Data Analyst, assisting enterprises by suporting data-driven decision making
"""
EMAIL = "mateusschenkel@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mateusschenkel",
    "GitHub": "https://github.com/Mateus-Schenkel",
    "Portfólio": "https://bit.ly/mateus-english-portfolio",
}
PROJECTS = {
    "🏆 Sales Dashboard - Python": "https://bi-sales-dashboard.streamlit.app/",
    "🏆 Sales Dashboard - Power BI": "https://bit.ly/dashboarvendasmateus",
    "🏆 Human Resources Dashboard - Power BI": "https://bit.ly/dashboardturnoverstarium",
    "🏆 Logistic Dashboard - Power BI": "https://bit.ly/4jdaesl"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file_EN, "rb") as pdf_file1:
    PDFbyte1 = pdf_file1.read()
with open(resume_file_PT, "rb") as pdf_file2:
    PDFbyte2 = pdf_file2.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small",)
with col1:
    st.caption("#")  # Adicione uma legenda opcional
    st.image(profile_pic, width=230)  # Define a largura da imagem

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume EN",
        data=PDFbyte1,
        file_name=resume_file_EN.name,
        mime="application/octet-stream",
    )
    st.download_button(
    label=" 📄 Download Resume PT",
    data=PDFbyte2,
    file_name=resume_file_PT.name,
    mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- ABOUT ME ---
st.write('#')
st.subheader("About me")
st.write(
"""
Organized and proactive data analyst with over 2 years of experience 
in financial analytics, automation processes, and business intelligence. 
Skilled in leveraging tools like n8n, SQL Server, 
and Power BI for data-driven decision-making. 
Experienced in developing AI-powered automation workflows using OpenAI API and Dokploy, 
optimizing financial operations, and creating insightful dashboards. 
A results-oriented professional, always eager to embrace new challenges and technologies.
"""
)

# --- SKILLS ---
st.write('#')
st.subheader("Hard Skills")
st.write(
"""
👩‍💻 Programming: Python, SQL.
🤖 Automation: n8n, Power Automate.
📊 Data Visualization: Power BI, Plotly, Streamlit.
🗄️ Databases: SQL Server, PostgreSQL, MySQL, Oracle.
🔁 Workflow Optimization: Automating business processes with AI and analytics.
"""
)

# --- CERTIFICATIONS ---
st.write('#')
st.subheader("Certifications")
st.write(
"""
- ► Financial Management (Graduation Degree) - Feevale
- ► Database Administration (Pós Graduation Degree) - Metropolitana
- ► Microsoft Power BI for Business Intelligence and Data Science - Data Science Academy
- ► Diction and Oratory - Conquer
- ► Time Management - Conquer
- ► Leadership Education - Conquer
- ► Managing Team Conflict - PMI
- ► SAP ERP Essential Training - LinkedIn
- ► Python - Hashtag Treinamentos
- ► Git & GitHub - Jornada de Dados
- ► Web Scrapping - Jornada de Dados
"""
)

# --- LANGUAGES ---
st.write('#')
st.subheader("Languages")
st.write(
    """
- ► Portuguese - Native
- ► English - Advanced
"""
)

# --- WORK HISTORY ---
st.write('#')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Nova Capital**")
st.write("Jan'25 - Present")
st.write(
    """
- ► Designed and implemented advanced automation workflows using n8n, Dokploy, 
and OpenAI API, significantly reducing manual processes and improving operational efficiency.
- ► Leveraged SQL Server to develop and optimize complex queries for financial data analysis, 
ensuring accurate and timely insights for decision-making.
- ► Built interactive dashboards in Power BI to visualize key financial metrics.
- ► Collaborated with cross-functional teams to deploy AI agents for predictive analytics, 
streamlining inventory and financial forecasting.
"""
)

# --- JOB 2
st.write("🚧", "**Data Analyst | Multi Armazéns**")
st.write("Ago'22 - Dec'24")
st.write(
    """
- ► Responsible for collecting and analyzing data from the database.
- ► Developed and optimized SQL queries to extract relevant information.
- ► Automated connections with Power Query Online to create Dataflows in Power BI.
- ► Contributed to data-driven decision-making through reports and visualizations.
- ► Led an automation project for clients, encompassing data collection from the database, 
    utilizing data intelligence with M and DAX languages and Power Automate,
    to send inventory information with alerts to clients over email,
    and also share information through MS SharePoint.
- ► Automated end-to-end invoice tracking by integrating data pipelines with Power Query Online, M, 
    and DAX, enabling real-time monitoring and client alerts via email and SharePoint.
"""
)

# --- JOB 3
st.write('#')
st.write("🚧", "**Financial Business Process Outsourcing | DBK**")
st.write("Nov'21 - Apr '22")
st.write(
    """
- ► Performed bank reconciliation of six small companies.
- ► Provided all the support to business partners.
- ► Worked on accounts payable and receivable daily routine.
- ► Managed the process of verifying, logging and mailing checks.
- ► Provided support to the accounting department.
- ► Managed the company credit cards.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Financial Assistant | MVL**")
st.write("Jan'20 - Sept '21")
st.write(
    """
- ► Performed the monthly payroll.
- ► Worked on accounts payable and receivable daily routine.
- ► Managed the process of verifying, logging and mailing checks.
- ► Collaborated with the human resources department, helping with the hiring processes.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")