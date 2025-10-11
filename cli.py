#!/usr/bin/env python3
"""
AI Resume & Portfolio Builder - CLI Tool
Simple command-line interface for resume optimization
"""

import sys
from pathlib import Path
from datetime import datetime

# Import components
from file_processor import FileProcessor
from resume_optimizer import ResumeOptimizer
from interview_generator import InterviewGenerator
from cover_letter_generator import CoverLetterGenerator
from config import Config

def print_header():
    """Print application header"""
    print("\n" + "="*70)
    print(f"  {Config.APP_NAME} v{Config.APP_VERSION}")
    print("  Command Line Interface")
    print("="*70 + "\n")

def optimize_resume_cli():
    """Interactive resume optimization"""
    print_header()
    print("📄 RESUME OPTIMIZER\n")
    
    # Get inputs
    jd_file = input("Job description file path: ").strip()
    resume_file = input("Your resume file path: ").strip()
    
    # Optional inputs
    gpa = input("Your GPA (optional, press Enter to skip): ").strip()
    coursework = input("Relevant coursework (optional, press Enter to skip): ").strip()
    generate_interview = input("Generate interview questions? (y/n): ").strip().lower() == 'y'
    
    try:
        # Initialize
        file_processor = FileProcessor()
        optimizer = ResumeOptimizer()
        
        # Read files
        print("\n📖 Reading files...")
        jd_content = file_processor.read_file(jd_file)
        resume_content = file_processor.read_file(resume_file)
        
        # Prepare student info
        student_info = {}
        if gpa and float(gpa) >= 3.0:
            student_info['gpa'] = float(gpa)
        if coursework:
            student_info['coursework'] = coursework
        
        # Optimize
        print("🔧 Optimizing resume...")
        optimized_resume = optimizer.optimize(resume_content, jd_content, student_info)
        
        # Save
        output_dir = Config.ensure_output_dir()
        output_file = output_dir / f"Optimized_Resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        file_processor.write_file(str(output_file), optimized_resume, 'txt')
        
        print(f"✅ Resume optimized and saved to: {output_file}\n")
        
        # Preview
        print("=" * 70)
        print("PREVIEW (first 500 characters):")
        print("=" * 70)
        print(optimized_resume[:500] + "...")
        print("=" * 70 + "\n")
        
        # Interview questions
        if generate_interview:
            print("❓ Generating interview questions...")
            interview_gen = InterviewGenerator()
            questions = interview_gen.generate(jd_content, resume_content, 'entry')
            
            questions_file = output_dir / f"Interview_Prep_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            file_processor.write_file(str(questions_file), questions, 'txt')
            print(f"✅ Interview prep saved to: {questions_file}\n")
        
        print("🎉 Done! Your files are ready in the 'outputs' folder.\n")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Please check your file paths and try again.\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def generate_cover_letter_cli():
    """Interactive cover letter generation"""
    print_header()
    print("✉️  COVER LETTER GENERATOR\n")
    
    # Get inputs
    jd_file = input("Job description file path: ").strip()
    resume_file = input("Your resume file path (optional, press Enter to skip): ").strip()
    
    print("\nYour Information:")
    name = input("Your full name: ").strip()
    company = input("Company name: ").strip()
    position = input("Position title: ").strip()
    email = input("Your email: ").strip()
    phone = input("Your phone (optional): ").strip()
    linkedin = input("LinkedIn URL (optional): ").strip()
    
    try:
        # Initialize
        file_processor = FileProcessor()
        generator = CoverLetterGenerator()
        
        # Read files
        print("\n📖 Reading job description...")
        jd_content = file_processor.read_file(jd_file)
        
        resume_content = ""
        if resume_file:
            print("📖 Reading resume...")
            resume_content = file_processor.read_file(resume_file)
        
        # Student info
        student_info = {
            'name': name,
            'company': company,
            'position': position,
            'email': email,
            'phone': phone,
            'linkedin': linkedin
        }
        
        # Generate
        print("✍️  Generating cover letter...")
        cover_letter = generator.generate(jd_content, resume_content, student_info)
        
        # Save
        output_dir = Config.ensure_output_dir()
        output_file = output_dir / f"Cover_Letter_{company}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        file_processor.write_file(str(output_file), cover_letter, 'txt')
        
        print(f"✅ Cover letter saved to: {output_file}\n")
        
        # Preview
        print("=" * 70)
        print("PREVIEW:")
        print("=" * 70)
        print(cover_letter[:600] + "...")
        print("=" * 70 + "\n")
        
        print("🎉 Done! Your cover letter is ready.\n")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Please check your file paths and try again.\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def generate_interview_questions_cli():
    """Interactive interview questions generation"""
    print_header()
    print("❓ INTERVIEW PREP GENERATOR\n")
    
    # Get inputs
    jd_file = input("Job description file path: ").strip()
    resume_file = input("Your resume file path (optional, press Enter to skip): ").strip()
    
    print("\nJob Level:")
    print("1. Entry level")
    print("2. Mid level")
    print("3. Senior level")
    level_choice = input("Select level (1-3): ").strip()
    
    level_map = {'1': 'entry', '2': 'mid', '3': 'senior'}
    level = level_map.get(level_choice, 'entry')
    
    try:
        # Initialize
        file_processor = FileProcessor()
        generator = InterviewGenerator()
        
        # Read files
        print("\n📖 Reading job description...")
        jd_content = file_processor.read_file(jd_file)
        
        resume_content = ""
        if resume_file:
            print("📖 Reading resume...")
            resume_content = file_processor.read_file(resume_file)
        
        # Generate
        print(f"❓ Generating {level} level interview questions...")
        questions = generator.generate(jd_content, resume_content, level)
        
        # Save
        output_dir = Config.ensure_output_dir()
        output_file = output_dir / f"Interview_Prep_{level}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        file_processor.write_file(str(output_file), questions, 'txt')
        
        print(f"✅ Interview prep saved to: {output_file}\n")
        
        # Preview
        print("=" * 70)
        print("PREVIEW (first 800 characters):")
        print("=" * 70)
        print(questions[:800] + "...")
        print("=" * 70 + "\n")
        
        print("🎉 Done! Your interview prep guide is ready.\n")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Please check your file paths and try again.\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def show_menu():
    """Show main menu"""
    print_header()
    
    # Check API status
    if Config.GEMINI_API_KEY:
        print("✅ AI Features: ENABLED")
    else:
        print("⚠️  AI Features: LIMITED (No API key configured)")
    
    print("\nSelect an option:")
    print("1. 📄 Optimize Resume")
    print("2. ✉️  Generate Cover Letter")
    print("3. ❓ Generate Interview Questions")
    print("4. 🚀 Launch Web Interface")
    print("5. ❌ Exit")
    print()

def main():
    """Main CLI entry point"""
    
    # Validate config
    Config.validate()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            optimize_resume_cli()
        elif choice == '2':
            generate_cover_letter_cli()
        elif choice == '3':
            generate_interview_questions_cli()
        elif choice == '4':
            print("\n🚀 Launching web interface...")
            print("Opening Streamlit app. Press Ctrl+C to stop.\n")
            import subprocess
            try:
                subprocess.run(['streamlit', 'run', 'app.py'])
            except KeyboardInterrupt:
                print("\n\nStopped web interface.\n")
            except Exception as e:
                print(f"❌ Could not launch: {e}")
                print("Try running: streamlit run app.py\n")
        elif choice == '5':
            print("\n👋 Thank you for using AI Resume & Portfolio Builder!")
            print("Good luck with your job search! 🎉\n")
            break
        else:
            print("\n❌ Invalid choice. Please select 1-5.\n")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)
