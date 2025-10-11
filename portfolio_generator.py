"""
AI-Powered Portfolio Content Generator
Creates professional portfolio descriptions for student projects
"""

import google.generativeai as genai
from typing import Dict, List
from config import Config

class PortfolioGenerator:
    """Generates professional portfolio content from student projects"""
    
    def __init__(self):
        """Initialize with Gemini API"""
        self.model = None
        self.api_available = False
        
        try:
            if Config.GEMINI_API_KEY:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
                self.api_available = True
                print("✅ Portfolio Generator initialized")
            else:
                print("⚠️  AI not available - using template portfolio")
        except Exception as e:
            print(f"⚠️  Warning: Could not initialize AI: {e}")
            self.api_available = False
    
    def generate(self, projects: List[Dict], student_info: Dict) -> str:
        """
        Generate portfolio content
        
        Args:
            projects: List of dicts with keys: name, description, tech_stack, github_url, demo_url
            student_info: Dict with keys: name, bio, skills, email, linkedin, github
        
        Returns:
            Professional portfolio content in markdown
        """
        print("🎨 Creating portfolio content...")
        
        if self.api_available:
            return self._ai_generate(projects, student_info)
        else:
            return self._fallback_generate(projects, student_info)
    
    def _ai_generate(self, projects: List[Dict], student_info: Dict) -> str:
        """Generate portfolio using AI"""
        
        projects_text = "\n".join([
            f"- {p.get('name', 'Unnamed Project')}: {p.get('description', 'No description')} "
            f"(Tech: {p.get('tech_stack', 'N/A')})"
            for p in projects
        ])
        
        prompt = f"""You are a professional portfolio writer for software developers.

TASK: Create an impressive, professional portfolio page content for this student developer.

STUDENT INFO:
Name: {student_info.get('name', 'Student Developer')}
Bio: {student_info.get('bio', 'Passionate student developer')}
Skills: {student_info.get('skills', 'Programming, Problem-solving')}
Email: {student_info.get('email', 'email@example.com')}
LinkedIn: {student_info.get('linkedin', '')}
GitHub: {student_info.get('github', '')}

PROJECTS:
{projects_text}

OUTPUT FORMAT (Use Markdown):

# [Student Name] - Portfolio

## About Me
[Write an engaging, professional 2-3 paragraph introduction highlighting passion, skills, and career goals. Make it authentic and compelling.]

## Technical Skills
[Organize skills into categories: Languages, Frameworks, Tools, etc. Present in a clean format.]

## Featured Projects

### [Project 1 Name]
**Technologies:** [List]
**Description:** [2-3 sentences describing the project, problem solved, and impact. Use strong verbs and metrics if possible.]
**Key Features:**
- [Feature 1 with technical detail]
- [Feature 2 with implementation approach]
- [Feature 3 with result/outcome]

[Include GitHub and Demo links if available]

[Repeat for each project]

## Education
[Format education information professionally]

## Let's Connect
[Format contact information in an inviting way]

REQUIREMENTS:
- Be professional but authentic
- Highlight technical achievements
- Use action-oriented language
- Include specific technologies
- Make each project sound impactful
- Add personality to the "About Me" section"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=2000,
                    temperature=Config.TEMPERATURE_CREATIVE
                )
            )
            return response.text.strip()
        except Exception as e:
            print(f"❌ AI generation failed: {e}")
            return self._fallback_generate(projects, student_info)
    
    def _fallback_generate(self, projects: List[Dict], student_info: Dict) -> str:
        """Generate portfolio without AI"""
        
        name = student_info.get('name', 'Student Developer')
        bio = student_info.get('bio', 'Passionate student developer with a love for creating innovative solutions.')
        skills = student_info.get('skills', 'Python, JavaScript, React, Git')
        email = student_info.get('email', 'your.email@example.com')
        linkedin = student_info.get('linkedin', '')
        github = student_info.get('github', '')
        
        # Generate projects section
        projects_section = ""
        for i, project in enumerate(projects, 1):
            name_p = project.get('name', f'Project {i}')
            desc = project.get('description', 'An innovative software project.')
            tech = project.get('tech_stack', 'Various technologies')
            github_url = project.get('github_url', '')
            demo_url = project.get('demo_url', '')
            
            projects_section += f"""
### {name_p}
**Technologies:** {tech}

{desc}

**Key Features:**
- Implemented core functionality with focus on performance and scalability
- Designed intuitive user interface with modern design principles
- Integrated robust error handling and testing

"""
            if github_url:
                projects_section += f"[View on GitHub]({github_url}) "
            if demo_url:
                projects_section += f"[Live Demo]({demo_url})"
            projects_section += "\n\n"
        
        portfolio = f"""# {name} - Portfolio

## 👋 About Me

{bio}

I'm passionate about leveraging technology to solve real-world problems. With a strong foundation in computer science and hands-on experience in software development, I'm constantly exploring new technologies and best practices.

Currently seeking opportunities to contribute to innovative projects and grow as a developer.

## 🛠️ Technical Skills

**Programming Languages:** {', '.join(skills.split(',')[:4]) if skills else 'Python, JavaScript'}

**Frameworks & Libraries:** React, Node.js, Django, Flask, Express

**Tools & Platforms:** Git, Docker, AWS, VS Code, Linux

**Databases:** PostgreSQL, MongoDB, MySQL

**Methodologies:** Agile, Test-Driven Development, CI/CD

## 🚀 Featured Projects

{projects_section}

## 🎓 Education

**Bachelor of Science in Computer Science**
University Name | Expected Graduation: Year

Relevant Coursework: Data Structures, Algorithms, Software Engineering, Database Systems, Web Development

## 📫 Let's Connect!

I'm always interested in discussing new opportunities, collaborations, or just chatting about technology!

**Email:** {email}
"""
        if linkedin:
            portfolio += f"**LinkedIn:** {linkedin}\n"
        if github:
            portfolio += f"**GitHub:** {github}\n"
        
        portfolio += "\n---\n\n💡 *This portfolio was generated using AI Resume & Portfolio Builder*"
        
        return portfolio


# Convenience function
def quick_portfolio(projects: List[Dict], student_info: Dict) -> str:
    """Generate portfolio in one function call"""
    generator = PortfolioGenerator()
    return generator.generate(projects, student_info)
