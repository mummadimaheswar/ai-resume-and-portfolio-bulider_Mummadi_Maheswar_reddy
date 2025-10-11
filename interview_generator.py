"""
AI-Powered Interview Question Generator
Tailored for students preparing for job interviews
"""

import google.generativeai as genai
import re
from typing import List, Dict
from config import Config

class InterviewGenerator:
    """Generates targeted interview questions for job preparation"""
    
    def __init__(self):
        """Initialize with Gemini API"""
        self.model = None
        self.api_available = False
        
        try:
            if Config.GEMINI_API_KEY:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
                self.api_available = True
                print("✅ Interview Question Generator initialized")
            else:
                print("⚠️  AI not available - using fallback questions")
        except Exception as e:
            print(f"⚠️  Warning: Could not initialize AI: {e}")
            self.api_available = False
    
    def generate(self, jd: str, resume: str = "", level: str = "entry") -> str:
        """
        Generate comprehensive interview questions
        
        Args:
            jd: Job description text
            resume: Student's resume text (optional)
            level: Job level (entry, mid, senior)
        
        Returns:
            Formatted interview preparation guide
        """
        print("📝 Analyzing job requirements for interview prep...")
        
        # Extract key information
        tech_stack = self._extract_keywords(jd, 'technical')
        soft_skills = self._extract_keywords(jd, 'soft')
        
        if self.api_available:
            questions = self._ai_generate(jd, resume, tech_stack, soft_skills, level)
        else:
            questions = self._fallback_generate(tech_stack, soft_skills, level)
        
        return self._format_guide(questions, tech_stack, soft_skills)
    
    def _extract_keywords(self, text: str, category: str) -> List[str]:
        """Extract keywords by category"""
        
        if category == 'technical':
            patterns = [
                r'\b(python|java|javascript|typescript|c\+\+|c#|go|ruby|php|swift|kotlin)\b',
                r'\b(react|angular|vue|django|flask|spring|express|node\.?js)\b',
                r'\b(aws|azure|gcp|docker|kubernetes|git|jenkins|ci/cd)\b',
                r'\b(sql|nosql|mongodb|postgresql|mysql|redis)\b',
                r'\b(machine learning|ai|data science|tensorflow|pytorch)\b'
            ]
        else:  # soft skills
            patterns = [
                r'\b(leadership|communication|teamwork|collaboration)\b',
                r'\b(problem.solving|analytical|critical thinking)\b',
                r'\b(agile|scrum|project management)\b',
                r'\b(creative|innovative|adaptable|flexible)\b'
            ]
        
        keywords = set()
        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            keywords.update(matches)
        
        return list(keywords)[:10]
    
    def _ai_generate(self, jd: str, resume: str, tech: List[str], skills: List[str], level: str) -> Dict:
        """Generate questions using AI"""
        
        prompt = f"""You are an expert technical interviewer. Generate interview questions for a {level}-level candidate.

JOB REQUIREMENTS:
{jd[:1200]}

CANDIDATE RESUME:
{resume[:600]}

KEY TECHNOLOGIES: {', '.join(tech[:5]) if tech else 'general programming'}
KEY SKILLS: {', '.join(skills[:3]) if skills else 'teamwork, communication'}

GENERATE EXACTLY:
1. {Config.TECHNICAL_QUESTIONS} Technical Questions - Focus on {', '.join(tech[:3]) if tech else 'programming fundamentals, data structures, algorithms'}
2. {Config.BEHAVIORAL_QUESTIONS} Behavioral Questions - Use STAR method format, focus on student experiences
3. {Config.SITUATIONAL_QUESTIONS} Situational Questions - Real workplace scenarios
4. 3 Company-Specific Questions - About role and organization

REQUIREMENTS:
- Make questions student-friendly (internships, academic projects, extracurriculars count as experience)
- Include coding/technical challenges appropriate for {level} level
- Questions should be specific to the technologies mentioned
- Behavioral questions should allow discussion of academic projects
- Avoid asking about extensive work experience

FORMAT YOUR RESPONSE AS:

## TECHNICAL QUESTIONS
1. [Question]
2. [Question]
...

## BEHAVIORAL QUESTIONS (Use STAR Method)
1. [Question]
2. [Question]
...

## SITUATIONAL QUESTIONS
1. [Question]
2. [Question]
...

## COMPANY & ROLE QUESTIONS
1. [Question]
2. [Question]
..."""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=1200,
                    temperature=Config.TEMPERATURE_FACTUAL
                )
            )
            
            # Parse AI response into structured format
            return self._parse_ai_response(response.text)
        
        except Exception as e:
            print(f"⚠️  AI generation failed: {e}")
            return self._fallback_generate(tech, skills, level)
    
    def _parse_ai_response(self, text: str) -> Dict:
        """Parse AI response into structured format"""
        sections = {
            'technical': [],
            'behavioral': [],
            'situational': [],
            'company': []
        }
        
        current_section = None
        lines = text.split('\n')
        
        for line in lines:
            line_lower = line.lower().strip()
            
            if 'technical' in line_lower and '#' in line:
                current_section = 'technical'
            elif 'behavioral' in line_lower and '#' in line:
                current_section = 'behavioral'
            elif 'situational' in line_lower and '#' in line:
                current_section = 'situational'
            elif ('company' in line_lower or 'role' in line_lower) and '#' in line:
                current_section = 'company'
            elif current_section and line.strip() and (line.strip()[0].isdigit() or line.strip().startswith('-')):
                # Clean up the question
                question = re.sub(r'^\d+[\.\)]\s*', '', line.strip())
                question = re.sub(r'^[-•]\s*', '', question)
                if question:
                    sections[current_section].append(question)
        
        return sections
    
    def _fallback_generate(self, tech: List[str], skills: List[str], level: str) -> Dict:
        """Generate questions without AI"""
        
        tech_str = ', '.join(tech[:3]) if tech else 'your technical stack'
        
        questions = {
            'technical': [
                f"Explain your experience with {tech_str}",
                "Walk me through your problem-solving process for debugging complex issues",
                "Describe a challenging technical project you've worked on",
                f"How would you approach learning {tech[0] if tech else 'a new technology'}?",
                "Explain the difference between {tech[0] if tech else 'OOP'} and {tech[1] if len(tech) > 1 else 'functional programming'}",
                "What's your experience with version control and Git?"
            ],
            'behavioral': [
                "Tell me about a group project where you had to overcome disagreements",
                "Describe a time when you had to learn something new under a tight deadline",
                "Give an example of when you took initiative on a project or team",
                "Tell me about a technical challenge you faced and how you solved it",
                "How do you handle receiving critical feedback on your work?"
            ],
            'situational': [
                "You're working on a feature and discover a major bug in production - what steps do you take?",
                "Your teammate is struggling with their part of the project and it's affecting deadlines - how do you handle it?",
                "You have multiple assignments/projects due at the same time - how do you prioritize?",
                "You disagree with a technical decision made by your team lead - what do you do?"
            ],
            'company': [
                "What interests you about this role and our company?",
                "Where do you see yourself growing in this position?",
                "What unique perspective or skills do you bring to the team?"
            ]
        }
        
        return questions
    
    def _format_guide(self, questions: Dict, tech: List[str], skills: List[str]) -> str:
        """Format the complete interview prep guide"""
        
        guide = f"""
{'='*70}
🎯 INTERVIEW PREPARATION GUIDE
{'='*70}

## 🔧 TECHNICAL QUESTIONS ({len(questions.get('technical', []))})
Focus Areas: {', '.join(tech[:5]) if tech else 'General Programming'}

{self._format_question_list(questions.get('technical', []))}

## 💼 BEHAVIORAL QUESTIONS ({len(questions.get('behavioral', []))})
💡 TIP: Use the STAR Method (Situation, Task, Action, Result)
Focus Areas: {', '.join(skills[:5]) if skills else 'Leadership, Communication, Teamwork'}

{self._format_question_list(questions.get('behavioral', []))}

## 🎭 SITUATIONAL QUESTIONS ({len(questions.get('situational', []))})
💡 TIP: Think through your approach step-by-step

{self._format_question_list(questions.get('situational', []))}

## 🏢 COMPANY & ROLE QUESTIONS ({len(questions.get('company', []))})

{self._format_question_list(questions.get('company', []))}

{'='*70}
📚 PREPARATION TIPS
{'='*70}

✅ BEFORE THE INTERVIEW:
   • Research the company: mission, values, recent news, products
   • Prepare 3-5 strong examples from your projects/coursework/internships
   • Review your resume and be ready to discuss every point
   • Practice coding problems on LeetCode/HackerRank
   • Prepare thoughtful questions to ask the interviewer

✅ DURING THE INTERVIEW:
   • Listen carefully and ask clarifying questions
   • Think out loud when solving technical problems
   • Use specific examples with quantifiable results
   • Be honest about what you don't know
   • Show enthusiasm and curiosity

✅ STAR METHOD FOR BEHAVIORAL QUESTIONS:
   📌 Situation: Set the context (project, team, challenge)
   📌 Task: Explain your responsibility
   📌 Action: Describe specific steps you took
   📌 Result: Share the outcome with metrics

✅ TECHNICAL PROBLEM-SOLVING:
   1. Clarify requirements and constraints
   2. Discuss your approach before coding
   3. Consider edge cases
   4. Write clean, readable code
   5. Test your solution
   6. Discuss time/space complexity

🔥 POWER PHRASES:
   • "In my project on [X], I improved performance by [Y]%"
   • "I collaborated with [N] teammates to deliver [outcome]"
   • "I took the initiative to learn [technology] to solve [problem]"
   • "Through iterative testing, I reduced bugs by [X]%"

{'='*70}
🌟 REMEMBER: Your academic projects, hackathons, and personal projects
   are valuable experience. Present them with confidence!
{'='*70}
"""
        return guide
    
    def _format_question_list(self, questions: List[str]) -> str:
        """Format a list of questions"""
        if not questions:
            return "   (No specific questions generated)\n"
        
        formatted = []
        for i, q in enumerate(questions, 1):
            formatted.append(f"   {i}. {q}")
        
        return '\n'.join(formatted) + '\n'


# Convenience function for quick usage
def quick_interview_prep(job_description: str, resume: str = "", level: str = "entry") -> str:
    """Generate interview questions in one function call"""
    generator = InterviewGenerator()
    return generator.generate(job_description, resume, level)
