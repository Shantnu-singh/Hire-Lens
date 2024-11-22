import streamlit as st
import pdf2img
import gemini
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="HireLens | AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS 
st.markdown("""
<style>
    /* Custom color palette */
    :root {
        --primary-color: #3498db;
        --secondary-color: #2ecc71;
        --background-color: #f4f6f7;
        --text-color: #2c3e50;
    }

    /* Global styling */
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
        font-family: 'Inter', 'Roboto', sans-serif;
    }

    /* Header styling */
    .stMarkdown h1 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton > button {
        background-color: var(--primary-color);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* Card-like containers */
    .stContainer {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

def process_resume(jobdesc, resume, prompt):
    """Process resume with error handling and validation."""
    if not jobdesc:
        st.error("Please enter the job description")
        return None
    
    if not resume:
        st.error("Please upload your resume")
        return None
    
    # Convert PDF to image
    try:
        resume_img = pdf2img.convert_to_img(upload_pdf=resume)
        
        # Process resume with selected prompt
        with st.spinner('Analyzing your resume...'):
            response = gemini.parse_resume(jobdesc, resume_img, prompt)
        
        return response
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    # Title and description
    st.title("🔍 HireLens: AI Resume Analyzer")
    st.markdown("""
    ### Unlock Your Career Potential
    HireLens uses advanced AI to analyze your resume and provide insights 
    that can help you stand out in your job applications.
    """)

    # Sidebar for inputs
    with st.sidebar:
        st.header("📝 Resume Details")
        
        # Job description input
        jobdesc = st.text_area(
            "Enter Job Description", 
            help="Paste the full job description to get tailored insights"
        )
        
        # Resume upload
        resume = st.file_uploader(
            "Upload Resume", 
            type=['pdf'], 
            help="Upload your PDF resume"
        )
        
        # File upload confirmation
        if resume:
            st.success(f"📄 {resume.name} uploaded successfully")

    # Analysis options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ats_score_btn = st.button("🤖 ATS Score", use_container_width=True)
    
    with col2:
        personality_btn = st.button("👤 Candidate Profile", use_container_width=True)
    
    with col3:
        keywords_btn = st.button("🔑 Missing Keywords", use_container_width=True)

    # Result display area
    result_container = st.container()
    
    # Process based on selected analysis
    if ats_score_btn:
        result = process_resume(jobdesc, resume, gemini.ats_check_promt)
        if result:
            with result_container:
                st.subheader("🤖 ATS Analysis Result")
                st.write(result)
    
    elif personality_btn:
        result = process_resume(jobdesc, resume, gemini.resume_to_personality)
        if result:
            with result_container:
                st.subheader("👤 Candidate Personality Insights")
                st.write(result)
    
    elif keywords_btn:
        result = process_resume(jobdesc, resume, gemini.missing_keyword_prompt)
        if result:
            with result_container:
                st.subheader("🔑 Missing Keywords")
                st.write(result)

if __name__ == "__main__":
    main()