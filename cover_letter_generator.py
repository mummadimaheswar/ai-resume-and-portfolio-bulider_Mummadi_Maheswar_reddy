
import google.generativeai as genai
from typing import Dict
from config import Config

class CoverLetterGenerator:
    """Generates personalized cover letters for job applications"""
    
    def __init__(self):
        """Initialize with Gemini API"""
        self.model = None
        self.api_available = False
        
        try:
            if Config.GEMINI_API_KEY:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
                self.api_available = True
                print("✅ Cover Letter Generator initialized")
            else:
                print("⚠️  AI not available - using template cover letter")
        except Exception as e:
            print(f"⚠️  Warning: Could not initialize AI: {e}")
            self.api_available = False
    
    def generate(self, jd: str, resume: str, student_info: Dict) -> str:
        """
        Generate tailored cover letter
        
        Args:
            jd: Job description text
            resume: Student's resume text
            student_info: Dict with keys: name, company, position, why_interested
        
        Returns:
            Professional cover letter
        """
        print("✍️  Writing cover letter...")
        
        if self.api_available:
            return self._ai_generate(jd, resume, student_info)
        else:
            return self._fallback_generate(jd, student_info)
    
    def _ai_generate(self, jd: str, resume: str, student_info: Dict) -> str:
        """Generate cover letter using AI"""
        
        prompt = f"""You are an expert career counselor and cover letter writer for students and recent graduates.

TASK: Write a compelling, personalized cover letter for this job application.

JOB DESCRIPTION:
{jd[:1500]}

STUDENT'S RESUME:
{resume[:1000]}

STUDENT INFO:
Name: {student_info.get('name', 'Student Name')}
Company: {student_info.get('company', 'Company Name')}
Position: {student_info.get('position', 'Software Developer')}
Why Interested: {student_info.get('why_interested', 'Passionate about the company mission')}

REQUIREMENTS:
1. Professional yet authentic tone (student-appropriate)
2. Length: 3-4 paragraphs (300-400 words)
3. Structure:
   - Opening: Hook + position interest + how you learned about role
   - Body Paragraph 1: Highlight 2-3 relevant skills/projects matching job requirements
   - Body Paragraph 2: Show company knowledge + cultural fit + enthusiasm
   - Closing: Call to action + availability + thanks
4. Connect specific projects/coursework to job requirements
5. Show passion and eagerness to learn
6. Use metrics and achievements where possible
7. Avoid clichés like "I'm a hard worker" - show it with examples
8. Don't repeat the resume - complement it with context and personality

FORMAT:
[Student Name]
[Email] | [Phone] | [LinkedIn]
[Date]

[Hiring Manager Name / Hiring Team]
{student_info.get('company', 'Company Name')}

Dear Hiring Team,

[Opening paragraph]

[Body paragraph 1 - Technical fit]

[Body paragraph 2 - Cultural fit and enthusiasm]

[Closing paragraph]

Sincerely,
[Student Name]

Write in first person. Be specific. Be memorable."""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=1500,
                    temperature=Config.TEMPERATURE_CREATIVE
                )
            )
            return response.text.strip()
        except Exception as e:
            print(f"❌ AI generation failed: {e}")
            return self._fallback_generate(jd, student_info)
    
    def _fallback_generate(self, jd: str, student_info: Dict) -> str:
        """Generate cover letter without AI"""
        
        name = student_info.get('name', 'Your Name')
        company = student_info.get('company', 'Company Name')
        position = student_info.get('position', 'Software Developer Position')
        email = student_info.get('email', 'your.email@example.com')
        phone = student_info.get('phone', '(XXX) XXX-XXXX')
        linkedin = student_info.get('linkedin', 'linkedin.com/in/yourprofile')
        
        # Extract some keywords from JD for customization
        jd_lower = jd.lower()
        tech_mentioned = []
        for tech in ['Python', 'JavaScript', 'React', 'Java', 'AWS', 'Docker', 'Machine Learning']:
            if tech.lower() in jd_lower:
                tech_mentioned.append(tech)
        
        tech_str = ', '.join(tech_mentioned[:3]) if tech_mentioned else 'software development'
        
        from datetime import datetime
        today = datetime.now().strftime("%B %d, %Y")
        
        letter = f"""{name}
{email} | {phone} | {linkedin}
{today}

Hiring Team
{company}

Dear Hiring Team,

I am writing to express my strong interest in the {position} at {company}. As a motivated computer science student with hands-on experience in {tech_str} and a passion for building innovative solutions, I am excited about the opportunity to contribute to your team.

Through my academic projects and internships, I have developed strong technical skills that align well with your requirements. For instance, I have built full-stack applications using modern frameworks, implemented efficient algorithms for data processing, and collaborated with cross-functional teams using Agile methodologies. My recent project involved developing a web application that improved user engagement by 40% through responsive design and optimized performance. I am confident that my problem-solving abilities and enthusiasm for learning new technologies would make me a valuable addition to your team.

What particularly excites me about {company} is your commitment to innovation and impact in the industry. I have followed your recent work and am impressed by your approach to solving real-world challenges. The opportunity to work alongside talented professionals while contributing to meaningful projects aligns perfectly with my career goals. I am eager to bring my fresh perspective, technical skills, and collaborative spirit to your organization.

I would welcome the opportunity to discuss how my background and enthusiasm can contribute to {company}'s continued success. Thank you for considering my application. I look forward to the possibility of speaking with you soon.

Sincerely,
{name}

---
💡 This cover letter was generated using AI Resume & Portfolio Builder. 
   Customize it with your specific experiences and achievements!
"""
        return letter


# Convenience function
def quick_cover_letter(jd: str, resume: str, student_info: Dict) -> str:
    """Generate cover letter in one function call"""
    generator = CoverLetterGenerator()
    return generator.generate(jd, resume, student_info)
