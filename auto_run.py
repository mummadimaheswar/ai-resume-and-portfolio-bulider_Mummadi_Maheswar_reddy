#!/usr/bin/env python3
"""
Auto Career Builder - Zero-Click Career Package Generator
Just run it - no questions asked!
"""

import sys
from pathlib import Path
from smart_career_builder import SmartCareerBuilder
from config import Config


def main():
    """Automatic execution - uses default files"""
    
    print("\n" + "⚡ " * 25)
    print("  AUTO CAREER BUILDER - Zero-Click Mode")
    print("  Automatically generating your complete career package...")
    print("⚡ " * 25 + "\n")
    
    # Default files - try multiple locations
    possible_resumes = ["resume.txt", "examples/sample_resume.txt"]
    possible_jds = ["jd.txt", "examples/sample_job_description.txt"]
    
    resume_file = None
    for rf in possible_resumes:
        if Path(rf).exists():
            resume_file = rf
            break
    
    jd_file = None
    for jf in possible_jds:
        if Path(jf).exists():
            jd_file = jf
            break
    
    # Check if files exist
    if not resume_file:
        print(f"❌ Error: No resume file found!")
        print("   Please create resume.txt or use examples/sample_resume.txt\n")
        sys.exit(1)
    
    if not jd_file:
        print(f"❌ Error: No job description file found!")
        print("   Please create jd.txt or use examples/sample_job_description.txt\n")
        sys.exit(1)
    
    print(f"✅ Found: {resume_file}")
    print(f"✅ Found: {jd_file}\n")
    
    # Default student info (will auto-extract from files)
    student_info = {
        'email': 'your.email@example.com',
        'phone': '+1-555-0100',
        'linkedin': 'https://linkedin.com/in/yourprofile'
    }
    
    print("🚀 Generating complete career package...\n")
    
    try:
        builder = SmartCareerBuilder()
        results = builder.generate_complete_package(
            resume_file,
            jd_file,
            student_info
        )
        
        if results:
            print("\n✅ DONE! Check the 'outputs' folder for all your documents.\n")
        else:
            print("\n⚠️  Generation completed with some errors. Check output above.\n")
    
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled by user.\n")
        sys.exit(0)
