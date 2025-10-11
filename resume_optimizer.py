"""
AI-Powered Resume Optimization Engine
Tailored for students to highlight projects, skills, and experiences
"""

import re
import google.generativeai as genai
from typing import List, Dict
from config import Config

class ResumeOptimizer:
    """Optimizes student resumes for job descriptions using AI"""
    
    def __init__(self):
        """Initialize the resume optimizer with Gemini API"""
        self.model = None
        self.api_available = False
        
        try:
            if Config.GEMINI_API_KEY:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
                self.api_available = True
                print("✅ AI Resume Optimizer initialized")
            else:
                print("⚠️  AI not available - using fallback optimization")
        except Exception as e:
            print(f"⚠️  Warning: Could not initialize AI: {e}")
            self.api_available = False
    
    def optimize(self, resume_content: str, jd_content: str, student_info: Dict = None) -> str:
        """
        Optimize resume based on job description
        
        Args:
            resume_content: Raw resume text
            jd_content: Job description text
            student_info: Optional dict with GPA, coursework, etc.
        
        Returns:
            Optimized resume text
        """
        print("🔍 Analyzing job requirements...")
        keywords = self._extract_keywords(jd_content)
        
        print("🎯 Optimizing resume for target role...")
        if self.api_available:
            optimized = self._ai_optimize(resume_content, jd_content, keywords, student_info)
        else:
            optimized = self._fallback_optimization(resume_content, keywords, student_info)
        
        return optimized
    
    def _extract_keywords(self, jd_content: str) -> List[str]:
        """Extract critical keywords from job description"""
        
        if not self.api_available:
            return self._fallback_keyword_extraction(jd_content)
        
        prompt = f"""Extract the most important keywords from this job description.
Focus on:
- Programming languages (Python, Java, JavaScript, etc.)
- Frameworks & libraries (React, Django, TensorFlow, etc.)
- Tools & platforms (AWS, Docker, Git, etc.)
- Soft skills (Leadership, Communication, Teamwork, etc.)
- Required qualifications and certifications

Job Description:
{jd_content[:1000]}

Return ONLY a comma-separated list of keywords (15-20 keywords maximum).
Example: Python, AWS, React, Agile, Leadership, SQL"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=200,
                    temperature=0.3
                )
            )
            keywords_text = response.text.strip()
            keywords = [k.strip() for k in keywords_text.split(',') if k.strip()]
            return keywords[:20]  # Limit to 20 keywords
        except Exception as e:
            print(f"⚠️  Keyword extraction error: {e}")
            return self._fallback_keyword_extraction(jd_content)
    
    def _fallback_keyword_extraction(self, jd_content: str) -> List[str]:
        """Extract keywords without AI using pattern matching"""
        common_keywords = {
            # Programming Languages
            'Python', 'Java', 'JavaScript', 'TypeScript', 'C++', 'C#', 'Go', 'Ruby', 'PHP', 'Swift', 'Kotlin',
            # Web Technologies
            'React', 'Angular', 'Vue', 'Node.js', 'Django', 'Flask', 'Spring', 'Express', 'HTML', 'CSS',
            # Data & AI
            'Machine Learning', 'AI', 'Data Science', 'TensorFlow', 'PyTorch', 'Pandas', 'NumPy', 'SQL',
            # Cloud & DevOps
            'AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 'CI/CD', 'Jenkins', 'Git', 'Linux',
            # Databases
            'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Elasticsearch',
            # Methodologies
            'Agile', 'Scrum', 'REST', 'API', 'Microservices', 'GraphQL',
            # Soft Skills
            'Leadership', 'Communication', 'Teamwork', 'Problem-solving', 'Analytical'
        }
        
        jd_lower = jd_content.lower()
        found_keywords = []
        
        for keyword in common_keywords:
            if keyword.lower() in jd_lower:
                found_keywords.append(keyword)
        
        return found_keywords[:15]
    
    def _ai_optimize(self, resume: str, jd: str, keywords: List[str], student_info: Dict = None) -> str:
        """Generate optimized resume using AI"""
        
        gpa_info = ""
        if student_info and student_info.get('gpa', 0) >= 3.0:
            gpa_info = f"GPA: {student_info['gpa']}"
        
        coursework_info = ""
        if student_info and student_info.get('coursework'):
            coursework_info = f"Relevant Coursework: {student_info['coursework']}"
        
        prompt = f"""You are an expert resume writer specializing in student resumes for tech roles.

TASK: Optimize this student's resume for the target job while maintaining 100% truthfulness.

KEY REQUIREMENTS:
1. ✅ KEEP ALL FACTS TRUTHFUL - Never invent experience
2. 🎯 Highlight projects and academic work prominently  
3. 💡 Reframe existing experiences to match job requirements
4. 📊 Add quantifiable achievements (e.g., "improved performance by 30%")
5. 🔑 Naturally incorporate these keywords: {', '.join(keywords[:10])}
6. 🎓 Emphasize relevant coursework and academic projects
7. 🛠️ Use strong action verbs (Built, Developed, Implemented, Designed, Led)

TARGET JOB DESCRIPTION:
{jd[:1200]}

CURRENT RESUME:
{resume}

{gpa_info}
{coursework_info}

OUTPUT FORMAT:
Return a well-structured ATS-friendly resume with these sections:

# [Student Name]
[Email] | [Phone] | [LinkedIn] | [GitHub] | [Portfolio]

## PROFESSIONAL SUMMARY
[2-3 compelling sentences highlighting key strengths, relevant projects, and career goals]

## TECHNICAL SKILLS
Programming Languages: [List]
Frameworks & Libraries: [List]
Tools & Platforms: [List]
Databases: [List]

## PROJECTS
### [Project Name] | [Technologies Used] | [Date]
• [Achievement-focused bullet using action verb and quantifiable result]
• [Highlight technical challenges solved]
• [Demonstrate impact or outcome]

## EXPERIENCE (Academic, Internships, Part-time)
### [Position] | [Organization] | [Date]
• [Action verb + specific task + quantifiable result]
• [Highlight relevant technical skills]

## EDUCATION
[Degree] in [Major] | [University] | [Graduation Date]
{gpa_info}
{coursework_info}

## CERTIFICATIONS & ACHIEVEMENTS (if applicable)
• [List relevant certifications, hackathons, competitions]

REMEMBER: Be honest, highlight projects, use metrics, match keywords naturally!"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=2000,
                    temperature=Config.TEMPERATURE_FACTUAL
                )
            )
            return response.text.strip()
        except Exception as e:
            print(f"❌ AI optimization failed: {e}")
            return self._fallback_optimization(resume, keywords, student_info)
    
    def _fallback_optimization(self, resume: str, keywords: List[str], student_info: Dict = None) -> str:
        """Simple optimization without AI"""
        
        sections = self._parse_resume_sections(resume)
        
        gpa_text = ""
        if student_info and student_info.get('gpa', 0) >= 3.0:
            gpa_text = f"\nGPA: {student_info['gpa']}"
        
        optimized = f"""# OPTIMIZED RESUME
{'='*60}

## PROFESSIONAL SUMMARY
{sections.get('summary', 'Motivated student seeking opportunities to apply technical skills and contribute to innovative projects.')}

## TECHNICAL SKILLS
{', '.join(keywords)}

## PROJECTS
{sections.get('projects', 'Academic and personal projects demonstrating technical proficiency.')}

## EXPERIENCE
{sections.get('experience', 'Relevant internships, part-time work, and academic experiences.')}

## EDUCATION
{sections.get('education', 'Bachelor of Science in Computer Science')}{gpa_text}

---
📌 Keywords optimized for ATS: {', '.join(keywords[:10])}
✅ Ready for submission!
"""
        return optimized
    
    def _parse_resume_sections(self, resume: str) -> Dict[str, str]:
        """Parse resume into sections"""
        sections = {}
        lines = resume.split('\n')
        
        # Extract name (usually first line)
        sections['name'] = lines[0] if lines else "Your Name"
        
        # Simple pattern matching for sections
        current_section = None
        section_content = []
        
        for line in lines[1:]:
            line_lower = line.lower().strip()
            
            # Detect section headers
            if any(kw in line_lower for kw in ['summary', 'objective']):
                if current_section:
                    sections[current_section] = '\n'.join(section_content)
                current_section = 'summary'
                section_content = []
            elif any(kw in line_lower for kw in ['project', 'portfolio']):
                if current_section:
                    sections[current_section] = '\n'.join(section_content)
                current_section = 'projects'
                section_content = []
            elif any(kw in line_lower for kw in ['experience', 'work', 'employment']):
                if current_section:
                    sections[current_section] = '\n'.join(section_content)
                current_section = 'experience'
                section_content = []
            elif any(kw in line_lower for kw in ['education', 'academic']):
                if current_section:
                    sections[current_section] = '\n'.join(section_content)
                current_section = 'education'
                section_content = []
            elif current_section and line.strip():
                section_content.append(line)
        
        # Save last section
        if current_section:
            sections[current_section] = '\n'.join(section_content)
        
        return sections

