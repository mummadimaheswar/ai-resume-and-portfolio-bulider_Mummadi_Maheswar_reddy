"""
AI Resume & Portfolio Builder - Web Interface
Streamlit-based user-friendly interface for students
"""

import streamlit as st
import os
from pathlib import Path
from datetime import datetime
import tempfile

from file_processor import FileProcessor
from resume_optimizer import ResumeOptimizer
from interview_generator import InterviewGenerator
from cover_letter_generator import CoverLetterGenerator
from portfolio_generator import PortfolioGenerator
from config import Config

# Page configuration
st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #D4EDDA;
        border-left: 5px solid #28A745;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        background-color: #D1ECF1;
        border-left: 5px solid #17A2B8;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .feature-card {
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def save_uploaded_file(uploaded_file):
    """Save uploaded file temporarily and return path"""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown('<div class="main-header">🎓 AI Resume & Portfolio Builder</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Empowering Students to Showcase Their Potential</div>', unsafe_allow_html=True)
    
    # Check API configuration
    if not Config.GEMINI_API_KEY:
        st.warning("⚠️ Gemini API key not configured. AI features will be limited. Please set GEMINI_API_KEY in your .env file.")
    
    # Sidebar navigation
    st.sidebar.title("🎯 Select Tool")
    tool = st.sidebar.radio(
        "Navigation Menu",
        ["🏠 Home", "📄 Optimize Resume", "✉️ Cover Letter", "❓ Interview Prep", "🎨 Portfolio Generator"],
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Version:** {Config.APP_VERSION}")
    st.sidebar.markdown(f"**API Status:** {'✅ Connected' if Config.GEMINI_API_KEY else '❌ Not configured'}")
    
    # Route to appropriate tool
    if tool == "🏠 Home":
        show_home()
    elif tool == "📄 Optimize Resume":
        show_resume_optimizer()
    elif tool == "✉️ Cover Letter":
        show_cover_letter_generator()
    elif tool == "❓ Interview Prep":
        show_interview_prep()
    elif tool == "🎨 Portfolio Generator":
        show_portfolio_generator()

def show_home():
    """Show home page"""
    st.markdown("## Welcome! 👋")
    st.markdown("""
    This tool helps students create professional resumes, cover letters, and portfolios 
    tailored to specific job opportunities using AI.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✨ Features
        - **Resume Optimization**: Tailor your resume to job descriptions
        - **Cover Letter Generation**: Create personalized cover letters
        - **Interview Preparation**: Get role-specific interview questions
        - **Portfolio Creation**: Build professional portfolio content
        """)
    
    with col2:
        st.markdown("""
        ### 🚀 How It Works
        1. Upload your resume and job description
        2. Select the tool you need
        3. Fill in any additional information
        4. Generate and download your documents
        """)
    
    st.markdown("---")
    st.info("💡 **Tip**: Start with 'Optimize Resume' to tailor your resume to a specific job!")

def show_resume_optimizer():
    """Resume optimization interface"""
    st.markdown("## 📄 Resume Optimizer")
    st.markdown("Upload your resume and job description to get an ATS-optimized, tailored resume.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        jd_file = st.file_uploader("Upload Job Description", type=['txt', 'pdf', 'docx'], key='resume_jd')
        resume_file = st.file_uploader("Upload Your Resume", type=['txt', 'pdf', 'docx'], key='resume_file')
    
    with col2:
        gpa = st.text_input("GPA (optional, shown if >= 3.0)", key='resume_gpa')
        coursework = st.text_area("Relevant Coursework (optional)", key='resume_coursework')
        include_interview = st.checkbox("Also generate interview questions", value=True)
        job_level = st.selectbox("Job Level", ['entry', 'mid', 'senior'], key='resume_level')
    
    output_format = st.radio("Output Format", ['txt', 'docx'], horizontal=True, key='resume_format')
    
    if st.button("🚀 Optimize Resume", type="primary"):
        if not jd_file or not resume_file:
            st.error("❌ Please upload both job description and resume!")
            return
        
        with st.spinner("🔧 Optimizing your resume..."):
            try:
                # Save uploaded files
                jd_path = save_uploaded_file(jd_file)
                resume_path = save_uploaded_file(resume_file)
                
                # Initialize components
                file_processor = FileProcessor()
                optimizer = ResumeOptimizer()
                
                # Read files
                jd_content = file_processor.read_file(jd_path)
                resume_content = file_processor.read_file(resume_path)
                
                # Prepare student info
                student_info = {}
                if gpa and float(gpa) >= 3.0:
                    student_info['gpa'] = float(gpa)
                if coursework:
                    student_info['coursework'] = coursework
                
                # Optimize
                optimized_resume = optimizer.optimize(resume_content, jd_content, student_info)
                
                # Display result
                st.success("✅ Resume optimized successfully!")
                st.markdown("### 📝 Optimized Resume")
                st.text_area("Result", optimized_resume, height=400, key='resume_result')
                
                # Download button
                st.download_button(
                    label="⬇️ Download Optimized Resume",
                    data=optimized_resume,
                    file_name=f"Optimized_Resume_{datetime.now().strftime('%Y%m%d')}.{output_format}",
                    mime="text/plain"
                )
                
                # Generate interview questions if requested
                if include_interview:
                    with st.spinner("❓ Generating interview questions..."):
                        interview_gen = InterviewGenerator()
                        questions = interview_gen.generate(jd_content, resume_content, job_level)
                        
                        st.markdown("### ❓ Interview Preparation Guide")
                        st.text_area("Interview Questions", questions, height=400, key='interview_result')
                        
                        st.download_button(
                            label="⬇️ Download Interview Prep",
                            data=questions,
                            file_name=f"Interview_Prep_{datetime.now().strftime('%Y%m%d')}.{output_format}",
                            mime="text/plain",
                            key='download_interview'
                        )
                
                # Cleanup
                os.unlink(jd_path)
                os.unlink(resume_path)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

def show_cover_letter_generator():
    """Cover letter generation interface"""
    st.markdown("## ✉️ Cover Letter Generator")
    st.markdown("Create a personalized cover letter for your job application.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        jd_file = st.file_uploader("Upload Job Description", type=['txt', 'pdf', 'docx'], key='cover_jd')
        resume_file = st.file_uploader("Upload Your Resume (optional but recommended)", type=['txt', 'pdf', 'docx'], key='cover_resume')
        
        name = st.text_input("Your Full Name *", key='cover_name')
        email = st.text_input("Your Email *", key='cover_email')
    
    with col2:
        company = st.text_input("Company Name *", key='cover_company')
        position = st.text_input("Position Title *", key='cover_position')
        phone = st.text_input("Your Phone (optional)", key='cover_phone')
        linkedin = st.text_input("LinkedIn URL (optional)", key='cover_linkedin')
    
    output_format = st.radio("Output Format", ['txt', 'docx'], horizontal=True, key='cover_format')
    
    if st.button("✍️ Generate Cover Letter", type="primary"):
        if not jd_file or not name or not company or not position or not email:
            st.error("❌ Please fill in all required fields!")
            return
        
        with st.spinner("✍️  Writing your cover letter..."):
            try:
                # Save and read files
                jd_path = save_uploaded_file(jd_file)
                file_processor = FileProcessor()
                jd_content = file_processor.read_file(jd_path)
                
                resume_content = ""
                if resume_file:
                    resume_path = save_uploaded_file(resume_file)
                    resume_content = file_processor.read_file(resume_path)
                    os.unlink(resume_path)
                
                # Generate cover letter
                generator = CoverLetterGenerator()
                student_info = {
                    'name': name,
                    'company': company,
                    'position': position,
                    'email': email,
                    'phone': phone or '',
                    'linkedin': linkedin or ''
                }
                
                cover_letter = generator.generate(jd_content, resume_content, student_info)
                
                # Display result
                st.success("✅ Cover letter generated successfully!")
                st.markdown("### ✉️ Your Cover Letter")
                st.text_area("Result", cover_letter, height=500, key='cover_result')
                
                # Download button
                st.download_button(
                    label="⬇️ Download Cover Letter",
                    data=cover_letter,
                    file_name=f"Cover_Letter_{company}_{datetime.now().strftime('%Y%m%d')}.{output_format}",
                    mime="text/plain"
                )
                
                # Cleanup
                os.unlink(jd_path)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

def show_interview_prep():
    """Interview preparation interface"""
    st.markdown("## ❓ Interview Preparation")
    st.markdown("Get role-specific interview questions to prepare for your job interview.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        jd_file = st.file_uploader("Upload Job Description", type=['txt', 'pdf', 'docx'], key='interview_jd')
        resume_file = st.file_uploader("Upload Your Resume (optional)", type=['txt', 'pdf', 'docx'], key='interview_resume')
    
    with col2:
        job_level = st.selectbox("Job Level", ['entry', 'mid', 'senior'], key='interview_level')
        output_format = st.radio("Output Format", ['txt', 'docx'], key='interview_format')
    
    if st.button("📝 Generate Interview Questions", type="primary"):
        if not jd_file:
            st.error("❌ Please upload a job description!")
            return
        
        with st.spinner("❓ Generating interview questions..."):
            try:
                # Save and read files
                jd_path = save_uploaded_file(jd_file)
                file_processor = FileProcessor()
                jd_content = file_processor.read_file(jd_path)
                
                resume_content = ""
                if resume_file:
                    resume_path = save_uploaded_file(resume_file)
                    resume_content = file_processor.read_file(resume_path)
                    os.unlink(resume_path)
                
                # Generate questions
                generator = InterviewGenerator()
                questions = generator.generate(jd_content, resume_content, job_level)
                
                # Display result
                st.success("✅ Interview prep guide created!")
                st.markdown("### 📚 Interview Preparation Guide")
                st.text_area("Questions", questions, height=600, key='interview_questions')
                
                # Download button
                st.download_button(
                    label="⬇️ Download Interview Prep",
                    data=questions,
                    file_name=f"Interview_Prep_{datetime.now().strftime('%Y%m%d')}.{output_format}",
                    mime="text/plain"
                )
                
                # Cleanup
                os.unlink(jd_path)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

def show_portfolio_generator():
    """Portfolio generation interface"""
    st.markdown("## 🎨 Portfolio Generator")
    st.markdown("Create professional portfolio content to showcase your projects.")
    
    st.info("💡 **Tip**: This feature generates portfolio content based on your project information. You can use this on GitHub, personal websites, or portfolio platforms.")
    
    # Student Information
    st.markdown("### 👤 Your Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name *", key='portfolio_name')
        email = st.text_input("Email *", key='portfolio_email')
        github = st.text_input("GitHub URL", key='portfolio_github')
    
    with col2:
        bio = st.text_area("Short Bio (2-3 sentences) *", key='portfolio_bio', height=100)
        linkedin = st.text_input("LinkedIn URL", key='portfolio_linkedin')
        skills = st.text_input("Skills (comma-separated) *", key='portfolio_skills')
    
    # Projects
    st.markdown("### 🚀 Your Projects")
    st.markdown("Add at least one project. You can add more projects below.")
    
    num_projects = st.number_input("Number of projects", min_value=1, max_value=10, value=3, key='num_projects')
    
    projects = []
    for i in range(int(num_projects)):
        st.markdown(f"**Project {i+1}**")
        col1, col2 = st.columns(2)
        
        with col1:
            project_name = st.text_input(f"Project Name", key=f'project_name_{i}')
            tech_stack = st.text_input(f"Technologies Used", key=f'project_tech_{i}')
        
        with col2:
            description = st.text_area(f"Description", key=f'project_desc_{i}', height=100)
            github_url = st.text_input(f"GitHub URL (optional)", key=f'project_github_{i}')
        
        if project_name:
            projects.append({
                'name': project_name,
                'description': description or 'No description provided',
                'tech_stack': tech_stack or 'Various technologies',
                'github_url': github_url
            })
    
    if st.button("🎨 Generate Portfolio", type="primary"):
        if not name or not email or not bio or not skills:
            st.error("❌ Please fill in all required personal information!")
            return
        
        if not projects:
            st.error("❌ Please add at least one project!")
            return
        
        with st.spinner("🎨 Creating your portfolio..."):
            try:
                generator = PortfolioGenerator()
                student_info = {
                    'name': name,
                    'email': email,
                    'bio': bio,
                    'skills': skills,
                    'github': github or '',
                    'linkedin': linkedin or ''
                }
                
                portfolio = generator.generate(projects, student_info)
                
                # Display result
                st.success("✅ Portfolio created successfully!")
                st.markdown("### 🎨 Your Portfolio")
                st.markdown(portfolio)
                
                # Download button
                st.download_button(
                    label="⬇️ Download Portfolio (Markdown)",
                    data=portfolio,
                    file_name=f"Portfolio_{name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
