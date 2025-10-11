#!/usr/bin/env python3
"""
Smart Career Builder - All-in-One AI Career Package Generator
Automatically generates: Resume + Cover Letter + Interview Prep + Portfolio
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

from file_processor import FileProcessor
from resume_optimizer import ResumeOptimizer
from interview_generator import InterviewGenerator
from cover_letter_generator import CoverLetterGenerator
from portfolio_generator import PortfolioGenerator
from config import Config


class SmartCareerBuilder:
    """Intelligent career package builder that generates everything automatically"""
    
    def __init__(self):
        self.file_processor = FileProcessor()
        self.resume_optimizer = ResumeOptimizer()
        self.interview_generator = InterviewGenerator()
        self.cover_letter_generator = CoverLetterGenerator()
        self.portfolio_generator = PortfolioGenerator()
        
    def generate_complete_package(
        self,
        resume_path: str,
        jd_path: str,
        student_info: Optional[Dict] = None
    ) -> Dict[str, str]:
        """
        Generate complete career package with all documents
        
        Args:
            resume_path: Path to resume file
            jd_path: Path to job description file
            student_info: Optional student information (name, email, GPA, etc.)
            
        Returns:
            Dictionary with paths to all generated files
        """
        print("\n" + "="*80)
        print("  🚀 SMART CAREER BUILDER - AI Career Package Generator")
        print("  Generating: Resume + Cover Letter + Interview Prep + Portfolio")
        print("="*80 + "\n")
        
        # Validate config
        Config.validate()
        
        # Read input files
        print("📖 Step 1/5: Reading your files...")
        try:
            resume_content = self.file_processor.read_file(resume_path)
            jd_content = self.file_processor.read_file(jd_path)
            print("   ✅ Files loaded successfully\n")
        except Exception as e:
            print(f"   ❌ Error reading files: {e}")
            return {}
        
        # Prepare student info with defaults
        if not student_info:
            student_info = {}
        
        # Auto-extract student name from resume if not provided
        if 'name' not in student_info or not student_info['name']:
            student_info['name'] = self._extract_name_from_resume(resume_content)
        
        # Auto-extract company and position from job description
        company, position = self._extract_job_info(jd_content)
        student_info['company'] = company
        student_info['position'] = position
        
        # Determine job level from JD
        job_level = self._determine_job_level(jd_content)
        
        print(f"🎯 Detected Job: {position} at {company} ({job_level} level)")
        print(f"👤 Applicant: {student_info.get('name', 'Candidate')}\n")
        
        # Create output directory
        output_dir = Config.ensure_output_dir()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Generate all documents
        results = {}
        
        # 1. Optimized Resume
        print("📄 Step 2/5: Optimizing your resume with AI...")
        try:
            optimized_resume = self.resume_optimizer.optimize(
                resume_content, jd_content, student_info
            )
            resume_file = output_dir / f"Resume_Optimized_{timestamp}.txt"
            self.file_processor.write_file(str(resume_file), optimized_resume, 'txt')
            results['resume'] = str(resume_file)
            print(f"   ✅ Resume optimized: {resume_file.name}\n")
        except Exception as e:
            print(f"   ⚠️  Resume optimization failed: {e}\n")
            results['resume'] = None
        
        # 2. Cover Letter
        print("✉️  Step 3/5: Writing personalized cover letter...")
        try:
            cover_letter = self.cover_letter_generator.generate(
                jd_content, resume_content, student_info
            )
            cover_file = output_dir / f"CoverLetter_{company}_{timestamp}.txt"
            self.file_processor.write_file(str(cover_file), cover_letter, 'txt')
            results['cover_letter'] = str(cover_file)
            print(f"   ✅ Cover letter created: {cover_file.name}\n")
        except Exception as e:
            print(f"   ⚠️  Cover letter generation failed: {e}\n")
            results['cover_letter'] = None
        
        # 3. Interview Questions
        print("❓ Step 4/5: Preparing interview questions and answers...")
        try:
            interview_prep = self.interview_generator.generate(
                jd_content, resume_content, job_level
            )
            interview_file = output_dir / f"InterviewPrep_{job_level}_{timestamp}.txt"
            self.file_processor.write_file(str(interview_file), interview_prep, 'txt')
            results['interview'] = str(interview_file)
            print(f"   ✅ Interview prep ready: {interview_file.name}\n")
        except Exception as e:
            print(f"   ⚠️  Interview prep generation failed: {e}\n")
            results['interview'] = None
        
        # 4. Portfolio Content
        print("🎨 Step 5/5: Creating portfolio content...")
        try:
            portfolio = self.portfolio_generator.generate(resume_content, student_info)
            portfolio_file = output_dir / f"Portfolio_{timestamp}.md"
            self.file_processor.write_file(str(portfolio_file), portfolio, 'md')
            results['portfolio'] = str(portfolio_file)
            print(f"   ✅ Portfolio generated: {portfolio_file.name}\n")
        except Exception as e:
            print(f"   ⚠️  Portfolio generation failed: {e}\n")
            results['portfolio'] = None
        
        # Generate summary document
        print("📋 Creating package summary...")
        summary = self._create_summary(results, student_info, company, position)
        summary_file = output_dir / f"PACKAGE_SUMMARY_{timestamp}.txt"
        self.file_processor.write_file(str(summary_file), summary, 'txt')
        results['summary'] = str(summary_file)
        
        # Print results
        self._print_results(results, summary_file)
        
        return results
    
    def _extract_name_from_resume(self, resume_content: str) -> str:
        """Try to extract name from resume (first line usually)"""
        lines = resume_content.strip().split('\n')
        for line in lines[:5]:  # Check first 5 lines
            line = line.strip()
            if line and len(line.split()) <= 4 and len(line) < 50:
                # Likely a name if it's short and has 1-4 words
                return line
        return "Candidate"
    
    def _extract_job_info(self, jd_content: str) -> tuple:
        """Extract company and position from job description"""
        lines = jd_content.strip().split('\n')
        
        company = "Target Company"
        position = "Target Position"
        
        # Common patterns
        for line in lines[:20]:  # Check first 20 lines
            line = line.strip()
            lower = line.lower()
            
            if 'company:' in lower or 'organization:' in lower:
                company = line.split(':', 1)[1].strip()
            elif 'position:' in lower or 'role:' in lower or 'title:' in lower:
                position = line.split(':', 1)[1].strip()
            elif 'job title:' in lower:
                position = line.split(':', 1)[1].strip()
        
        return company, position
    
    def _determine_job_level(self, jd_content: str) -> str:
        """Determine job level from job description"""
        lower_jd = jd_content.lower()
        
        senior_keywords = ['senior', 'lead', 'principal', 'staff', 'architect', 
                          '5+ years', '7+ years', '10+ years', 'expert']
        mid_keywords = ['mid-level', 'intermediate', '3+ years', '3-5 years', 
                       'experienced']
        entry_keywords = ['entry', 'junior', 'associate', 'graduate', 'intern',
                         '0-2 years', 'recent graduate', 'new grad']
        
        # Count matches
        senior_count = sum(1 for kw in senior_keywords if kw in lower_jd)
        mid_count = sum(1 for kw in mid_keywords if kw in lower_jd)
        entry_count = sum(1 for kw in entry_keywords if kw in lower_jd)
        
        if senior_count >= 2:
            return 'senior'
        elif mid_count >= 2:
            return 'mid'
        elif entry_count >= 1:
            return 'entry'
        else:
            return 'entry'  # Default to entry level
    
    def _create_summary(
        self, 
        results: Dict[str, str],
        student_info: Dict,
        company: str,
        position: str
    ) -> str:
        """Create a summary document"""
        summary = f"""
{'='*80}
  AI CAREER PACKAGE - GENERATION SUMMARY
  Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
{'='*80}

APPLICATION DETAILS
-------------------
Applicant: {student_info.get('name', 'Candidate')}
Position:  {position}
Company:   {company}

{'='*80}
GENERATED DOCUMENTS
{'='*80}

"""
        
        if results.get('resume'):
            summary += f"✅ OPTIMIZED RESUME\n"
            summary += f"   Location: {results['resume']}\n"
            summary += f"   Purpose: ATS-optimized resume tailored to job requirements\n\n"
        
        if results.get('cover_letter'):
            summary += f"✅ PERSONALIZED COVER LETTER\n"
            summary += f"   Location: {results['cover_letter']}\n"
            summary += f"   Purpose: Professional cover letter highlighting fit\n\n"
        
        if results.get('interview'):
            summary += f"✅ INTERVIEW PREPARATION GUIDE\n"
            summary += f"   Location: {results['interview']}\n"
            summary += f"   Purpose: Practice questions with STAR method answers\n\n"
        
        if results.get('portfolio'):
            summary += f"✅ PORTFOLIO CONTENT\n"
            summary += f"   Location: {results['portfolio']}\n"
            summary += f"   Purpose: GitHub/website ready portfolio markdown\n\n"
        
        summary += f"\n{'='*80}\n"
        summary += "NEXT STEPS\n"
        summary += "{'='*80}\n\n"
        summary += "1. Review your optimized resume and make any personal adjustments\n"
        summary += "2. Customize the cover letter with specific company research\n"
        summary += "3. Practice interview questions using the STAR method\n"
        summary += "4. Add portfolio content to your GitHub README.md\n"
        summary += "5. Save documents as PDF/DOCX for final submission\n\n"
        
        summary += "🎉 Good luck with your application!\n"
        summary += f"\nAll files are in: outputs/\n"
        
        return summary
    
    def _print_results(self, results: Dict[str, str], summary_file: Path):
        """Print beautiful results summary"""
        print("\n" + "="*80)
        print("  🎉 SUCCESS! YOUR CAREER PACKAGE IS READY")
        print("="*80 + "\n")
        
        print("📦 Generated Documents:\n")
        
        if results.get('resume'):
            print(f"   📄 Resume:         {Path(results['resume']).name}")
        if results.get('cover_letter'):
            print(f"   ✉️  Cover Letter:   {Path(results['cover_letter']).name}")
        if results.get('interview'):
            print(f"   ❓ Interview Prep: {Path(results['interview']).name}")
        if results.get('portfolio'):
            print(f"   🎨 Portfolio:      {Path(results['portfolio']).name}")
        
        print(f"\n   📋 Summary:        {summary_file.name}")
        
        print(f"\n📁 Location: {Config.ensure_output_dir()}\n")
        
        print("="*80)
        print("  ✨ TIP: Review and customize documents before submitting")
        print("="*80 + "\n")


def main():
    """Main entry point - simple and automatic"""
    
    print("\n" + "🤖 " * 20)
    print(f"  {Config.APP_NAME}")
    print(f"  Version {Config.APP_VERSION} - Smart Mode")
    print("🤖 " * 20 + "\n")
    
    # Get inputs
    print("Let's build your complete career package!\n")
    
    resume_path = input("📄 Enter your resume file path: ").strip()
    if not resume_path:
        print("❌ Resume file is required!")
        return
    
    jd_path = input("📋 Enter job description file path: ").strip()
    if not jd_path:
        print("❌ Job description file is required!")
        return
    
    # Optional student info
    print("\n🎓 Student Information (optional - press Enter to skip):")
    name = input("   Your name: ").strip()
    email = input("   Your email: ").strip()
    phone = input("   Your phone: ").strip()
    linkedin = input("   LinkedIn URL: ").strip()
    gpa = input("   GPA (if 3.0+): ").strip()
    coursework = input("   Key coursework: ").strip()
    
    student_info = {}
    if name:
        student_info['name'] = name
    if email:
        student_info['email'] = email
    if phone:
        student_info['phone'] = phone
    if linkedin:
        student_info['linkedin'] = linkedin
    if gpa:
        try:
            gpa_float = float(gpa)
            if gpa_float >= 3.0:
                student_info['gpa'] = gpa_float
        except:
            pass
    if coursework:
        student_info['coursework'] = coursework
    
    # Generate everything
    print("\n🚀 Starting AI generation...\n")
    
    try:
        builder = SmartCareerBuilder()
        results = builder.generate_complete_package(
            resume_path,
            jd_path,
            student_info
        )
        
        if results:
            print("✅ All documents generated successfully!")
        else:
            print("⚠️  Some documents could not be generated. Check errors above.")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Generation cancelled by user.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check your input files and try again.\n")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)
