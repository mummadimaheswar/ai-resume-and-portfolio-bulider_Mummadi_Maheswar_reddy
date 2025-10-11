#!/usr/bin/env python3#!/usr/bin/env python3#!/usr/bin/env python3

"""

AI Resume & Portfolio Builder - Main Application""""""

Complete solution for students to create resumes, cover letters, and portfolios

"""AI Resume & Portfolio Builder - Main ApplicationResume Optimization Tool - Main Application



import osComplete solution for students to create resumes, cover letters, and portfolios"""

import argparse

import sys"""

from pathlib import Path

from datetime import datetimeimport os



from file_processor import FileProcessorimport osimport argparse

from resume_optimizer import ResumeOptimizer

from interview_generator import InterviewGeneratorimport argparsefrom file_processor import FileProcessor

from cover_letter_generator import CoverLetterGenerator

from portfolio_generator import PortfolioGeneratorimport sysfrom resume_optimizer import ResumeOptimizer

from config import Config

from pathlib import Pathfrom interview_generator import InterviewGenerator

# Color codes for terminal output

class Colors:from datetime import datetimefrom config import Config

    HEADER = '\033[95m'

    BLUE = '\033[94m'

    GREEN = '\033[92m'

    YELLOW = '\033[93m'from file_processor import FileProcessordef main():

    RED = '\033[91m'

    END = '\033[0m'from resume_optimizer import ResumeOptimizer    parser = argparse.ArgumentParser(description='Resume Optimization Tool')

    BOLD = '\033[1m'

from interview_generator import InterviewGenerator    parser.add_argument('--jd', required=True, help='Job Description file path')

def print_header():

    """Print application header"""from cover_letter_generator import CoverLetterGenerator    parser.add_argument('--resume', required=True, help='Resume file path')

    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")

    print(f"  {Config.APP_NAME} v{Config.APP_VERSION}")from portfolio_generator import PortfolioGenerator    parser.add_argument('--format', default='txt', choices=['pdf', 'txt', 'doc', 'docx'], help='Output format')

    print(f"  Empowering Students to Showcase Their Potential")

    print(f"{'='*70}{Colors.END}\n")from config import Config    



def print_success(message):    args = parser.parse_args()

    """Print success message"""

    print(f"{Colors.GREEN}✅ {message}{Colors.END}")# Color codes for terminal output    



def print_error(message):class Colors:    # Initialize components

    """Print error message"""

    print(f"{Colors.RED}❌ {message}{Colors.END}")    HEADER = '\033[95m'    file_processor = FileProcessor()



def print_info(message):    BLUE = '\033[94m'    optimizer = ResumeOptimizer()

    """Print info message"""

    print(f"{Colors.BLUE}ℹ️  {message}{Colors.END}")    GREEN = '\033[92m'    interview_gen = InterviewGenerator()



def print_warning(message):    YELLOW = '\033[93m'    

    """Print warning message"""

    print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")    RED = '\033[91m'    try:



def setup_output_directory():    END = '\033[0m'        # Process input files

    """Create output directory if it doesn't exist"""

    output_dir = Config.ensure_output_dir()    BOLD = '\033[1m'        print("📄 Reading job description...")

    print_info(f"Output directory: {output_dir}")

    return output_dir        jd_content = file_processor.read_file(args.jd)



def optimize_resume(args):def print_header():        

    """Handle resume optimization"""

    print_header()    """Print application header"""        print("📄 Reading resume...")

    print(f"{Colors.BOLD}📄 RESUME OPTIMIZATION MODE{Colors.END}\n")

        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")        resume_content = file_processor.read_file(args.resume)

    try:

        # Initialize components    print(f"  {Config.APP_NAME} v{Config.APP_VERSION}")        

        file_processor = FileProcessor()

        optimizer = ResumeOptimizer()    print(f"  Empowering Students to Showcase Their Potential")        # Optimize resume

        

        # Read input files    print(f"{'='*70}{Colors.END}\n")        print("🔧 Optimizing resume...")

        print("📖 Reading job description...")

        jd_content = file_processor.read_file(args.jd)        optimized_resume = optimizer.optimize(resume_content, jd_content)

        

        print("📖 Reading resume...")def print_success(message):        

        resume_content = file_processor.read_file(args.resume)

            """Print success message"""        # Generate interview questions

        # Optional student info

        student_info = {}    print(f"{Colors.GREEN}✅ {message}{Colors.END}")        print("❓ Generating interview questions...")

        if hasattr(args, 'gpa') and args.gpa:

            student_info['gpa'] = float(args.gpa)        interview_questions = interview_gen.generate(jd_content, resume_content)

        if hasattr(args, 'coursework') and args.coursework:

            student_info['coursework'] = args.courseworkdef print_error(message):        

        

        # Optimize resume    """Print error message"""        # Save outputs

        print("\n🔧 Optimizing resume for target role...")

        optimized_resume = optimizer.optimize(resume_content, jd_content, student_info)    print(f"{Colors.RED}❌ {message}{Colors.END}")        resume_filename = f"Optimized_Resume.{args.format}"

        

        # Save output        questions_filename = f"Interview_Questions.{args.format}"

        output_dir = setup_output_directory()

        output_file = output_dir / f"Optimized_Resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"def print_info(message):        

        file_processor.write_file(str(output_file), optimized_resume, args.format)

            """Print info message"""        file_processor.write_file(resume_filename, optimized_resume, args.format)

        print_success(f"Resume optimized: {output_file}")

            print(f"{Colors.BLUE}ℹ️  {message}{Colors.END}")        file_processor.write_file(questions_filename, interview_questions, args.format)

        # Optionally generate interview questions

        if hasattr(args, 'interview') and args.interview:        

            print("\n❓ Generating interview questions...")

            interview_gen = InterviewGenerator()def print_warning(message):        print(f"✅ Generated: {resume_filename}")

            questions = interview_gen.generate(jd_content, resume_content, args.level)

                """Print warning message"""        print(f"✅ Generated: {questions_filename}")

            questions_file = output_dir / f"Interview_Prep_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"

            file_processor.write_file(str(questions_file), questions, args.format)    print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")        

            print_success(f"Interview prep guide created: {questions_file}")

            except Exception as e:

    except FileNotFoundError as e:

        print_error(f"File not found: {e}")def setup_output_directory():        print(f"❌ Error: {e}")

        sys.exit(1)

    except Exception as e:    """Create output directory if it doesn't exist"""

        print_error(f"Error: {e}")

        if Config.DEBUG_MODE:    output_dir = Config.ensure_output_dir()if __name__ == "__main__":

            raise

        sys.exit(1)    print_info(f"Output directory: {output_dir}")    main()

    return output_dir

def generate_cover_letter(args):

    """Handle cover letter generation"""def optimize_resume(args):

    print_header()    """Handle resume optimization"""

    print(f"{Colors.BOLD}✉️  COVER LETTER GENERATION MODE{Colors.END}\n")    print_header()

        print(f"{Colors.BOLD}📄 RESUME OPTIMIZATION MODE{Colors.END}\n")

    try:    

        file_processor = FileProcessor()    try:

        generator = CoverLetterGenerator()        # Initialize components

                file_processor = FileProcessor()

        # Read inputs        optimizer = ResumeOptimizer()

        print("📖 Reading job description...")        

        jd_content = file_processor.read_file(args.jd)        # Read input files

                print("📖 Reading job description...")

        resume_content = ""        jd_content = file_processor.read_file(args.jd)

        if hasattr(args, 'resume') and args.resume:        

            print("📖 Reading resume...")        print("📖 Reading resume...")

            resume_content = file_processor.read_file(args.resume)        resume_content = file_processor.read_file(args.resume)

                

        # Student info        # Optional student info

        student_info = {        student_info = {}

            'name': args.name or 'Your Name',        if hasattr(args, 'gpa') and args.gpa:

            'company': args.company or 'Company Name',            student_info['gpa'] = float(args.gpa)

            'position': args.position or 'Position',        if hasattr(args, 'coursework') and args.coursework:

            'email': getattr(args, 'email', 'your.email@example.com'),            student_info['coursework'] = args.coursework

            'phone': getattr(args, 'phone', '(XXX) XXX-XXXX'),        

            'linkedin': getattr(args, 'linkedin', '')        # Optimize resume

        }        print("\n🔧 Optimizing resume for target role...")

                optimized_resume = optimizer.optimize(resume_content, jd_content, student_info)

        # Generate cover letter        

        print("\n✍️  Generating cover letter...")        # Save output

        cover_letter = generator.generate(jd_content, resume_content, student_info)        output_dir = setup_output_directory()

                output_file = output_dir / f"Optimized_Resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"

        # Save output        file_processor.write_file(str(output_file), optimized_resume, args.format)

        output_dir = setup_output_directory()        

        output_file = output_dir / f"Cover_Letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"        print_success(f"Resume optimized: {output_file}")

        file_processor.write_file(str(output_file), cover_letter, args.format)        

                # Optionally generate interview questions

        print_success(f"Cover letter created: {output_file}")        if hasattr(args, 'interview') and args.interview:

                    print("\n❓ Generating interview questions...")

    except Exception as e:            interview_gen = InterviewGenerator()

        print_error(f"Error: {e}")            questions = interview_gen.generate(jd_content, resume_content, args.level)

        if Config.DEBUG_MODE:            

            raise            questions_file = output_dir / f"Interview_Prep_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"

        sys.exit(1)            file_processor.write_file(str(questions_file), questions, args.format)

            print_success(f"Interview prep guide created: {questions_file}")

def generate_interview_questions(args):        

    """Handle interview question generation"""    except FileNotFoundError as e:

    print_header()        print_error(f"File not found: {e}")

    print(f"{Colors.BOLD}❓ INTERVIEW PREP MODE{Colors.END}\n")        sys.exit(1)

        except Exception as e:

    try:        print_error(f"Error: {e}")

        file_processor = FileProcessor()        if Config.DEBUG_MODE:

        generator = InterviewGenerator()            raise

                sys.exit(1)

        # Read job description

        print("📖 Reading job description...")def generate_cover_letter(args):

        jd_content = file_processor.read_file(args.jd)    """Handle cover letter generation"""

            print_header()

        resume_content = ""    print(f"{Colors.BOLD}✉️  COVER LETTER GENERATION MODE{Colors.END}\n")

        if hasattr(args, 'resume') and args.resume:    

            print("📖 Reading resume...")    try:

            resume_content = file_processor.read_file(args.resume)        file_processor = FileProcessor()

                generator = CoverLetterGenerator()

        # Generate questions        

        print("\n❓ Generating interview questions...")        # Read inputs

        questions = generator.generate(jd_content, resume_content, args.level)        print("📖 Reading job description...")

                jd_content = file_processor.read_file(args.jd)

        # Save output        

        output_dir = setup_output_directory()        resume_content = ""

        output_file = output_dir / f"Interview_Prep_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"        if hasattr(args, 'resume') and args.resume:

        file_processor.write_file(str(output_file), questions, args.format)            print("📖 Reading resume...")

                    resume_content = file_processor.read_file(args.resume)

        print_success(f"Interview prep guide created: {output_file}")        

                # Student info

    except Exception as e:        student_info = {

        print_error(f"Error: {e}")            'name': args.name or 'Your Name',

        if Config.DEBUG_MODE:            'company': args.company or 'Company Name',

            raise            'position': args.position or 'Position',

        sys.exit(1)            'email': getattr(args, 'email', 'your.email@example.com'),

            'phone': getattr(args, 'phone', '(XXX) XXX-XXXX'),

def main():            'linkedin': getattr(args, 'linkedin', '')

    """Main application entry point"""        }

    parser = argparse.ArgumentParser(        

        description='AI Resume & Portfolio Builder - Empower Your Job Search',        # Generate cover letter

        formatter_class=argparse.RawDescriptionHelpFormatter,        print("\n✍️  Generating cover letter...")

        epilog="""        cover_letter = generator.generate(jd_content, resume_content, student_info)

Examples:        

  # Optimize resume for a job        # Save output

  python main.py optimize-resume --jd job.txt --resume my_resume.pdf --interview        output_dir = setup_output_directory()

        output_file = output_dir / f"Cover_Letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"

  # Generate cover letter        file_processor.write_file(str(output_file), cover_letter, args.format)

  python main.py cover-letter --jd job.txt --name "John Doe" --company "Tech Corp" --position "Developer"        

        print_success(f"Cover letter created: {output_file}")

  # Generate interview questions        

  python main.py interview --jd job.txt --level entry    except Exception as e:

        print_error(f"Error: {e}")

  # Launch web interface        if Config.DEBUG_MODE:

  python main.py web            raise

        """        sys.exit(1)

    )

    def generate_interview_questions(args):

    # Create subparsers for different modes    """Handle interview question generation"""

    subparsers = parser.add_subparsers(dest='mode', help='Operation mode')    print_header()

        print(f"{Colors.BOLD}❓ INTERVIEW PREP MODE{Colors.END}\n")

    # Resume optimization mode    

    resume_parser = subparsers.add_parser('optimize-resume', help='Optimize resume for a job')    try:

    resume_parser.add_argument('--jd', required=True, help='Job description file path')        file_processor = FileProcessor()

    resume_parser.add_argument('--resume', required=True, help='Resume file path')        generator = InterviewGenerator()

    resume_parser.add_argument('--format', default='txt', choices=['txt', 'docx'],         

                               help='Output format (default: txt)')        # Read job description

    resume_parser.add_argument('--interview', action='store_true',         print("📖 Reading job description...")

                               help='Also generate interview questions')        jd_content = file_processor.read_file(args.jd)

    resume_parser.add_argument('--level', default='entry', choices=['entry', 'mid', 'senior'],        

                               help='Job level for interview questions (default: entry)')        resume_content = ""

    resume_parser.add_argument('--gpa', help='Your GPA (optional, shown if >= 3.0)')        if hasattr(args, 'resume') and args.resume:

    resume_parser.add_argument('--coursework', help='Relevant coursework (optional)')            print("📖 Reading resume...")

                resume_content = file_processor.read_file(args.resume)

    # Cover letter mode        

    cover_parser = subparsers.add_parser('cover-letter', help='Generate cover letter')        # Generate questions

    cover_parser.add_argument('--jd', required=True, help='Job description file path')        print("\n❓ Generating interview questions...")

    cover_parser.add_argument('--resume', help='Resume file path (optional but recommended)')        questions = generator.generate(jd_content, resume_content, args.level)

    cover_parser.add_argument('--name', required=True, help='Your name')        

    cover_parser.add_argument('--company', required=True, help='Company name')        # Save output

    cover_parser.add_argument('--position', required=True, help='Position title')        output_dir = setup_output_directory()

    cover_parser.add_argument('--email', help='Your email')        output_file = output_dir / f"Interview_Prep_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"

    cover_parser.add_argument('--phone', help='Your phone')        file_processor.write_file(str(output_file), questions, args.format)

    cover_parser.add_argument('--linkedin', help='Your LinkedIn URL')        

    cover_parser.add_argument('--format', default='txt', choices=['txt', 'docx'],         print_success(f"Interview prep guide created: {output_file}")

                               help='Output format (default: txt)')        

        except Exception as e:

    # Interview prep mode        print_error(f"Error: {e}")

    interview_parser = subparsers.add_parser('interview', help='Generate interview questions')        if Config.DEBUG_MODE:

    interview_parser.add_argument('--jd', required=True, help='Job description file path')            raise

    interview_parser.add_argument('--resume', help='Resume file path (optional)')        sys.exit(1)

    interview_parser.add_argument('--level', default='entry', choices=['entry', 'mid', 'senior'],

                                   help='Job level (default: entry)')def main():

    interview_parser.add_argument('--format', default='txt', choices=['txt', 'docx'],     """Main application entry point"""

                                   help='Output format (default: txt)')    parser = argparse.ArgumentParser(

            description='AI Resume & Portfolio Builder - Empower Your Job Search',

    # Web interface mode        formatter_class=argparse.RawDescriptionHelpFormatter,

    web_parser = subparsers.add_parser('web', help='Launch web interface')        epilog="""

    Examples:

    args = parser.parse_args()  # Optimize resume for a job

      python main.py optimize-resume --jd job.txt --resume my_resume.pdf --interview

    # Validate configuration

    Config.validate()  # Generate cover letter

      python main.py cover-letter --jd job.txt --name "John Doe" --company "Tech Corp" --position "Developer"

    # Route to appropriate function

    if args.mode == 'optimize-resume':  # Generate interview questions

        optimize_resume(args)  python main.py interview --jd job.txt --level entry

    elif args.mode == 'cover-letter':

        generate_cover_letter(args)  # Launch web interface

    elif args.mode == 'interview':  python main.py web

        generate_interview_questions(args)        """

    elif args.mode == 'web':    )

        print_info("Launching web interface...")    

        try:    # Create subparsers for different modes

            import subprocess    subparsers = parser.add_subparsers(dest='mode', help='Operation mode')

            subprocess.run(['streamlit', 'run', 'app.py'])    

        except Exception as e:    # Resume optimization mode

            print_error(f"Could not launch web interface: {e}")    resume_parser = subparsers.add_parser('optimize-resume', help='Optimize resume for a job')

            print_info("Try running: streamlit run app.py")    resume_parser.add_argument('--jd', required=True, help='Job description file path')

    else:    resume_parser.add_argument('--resume', required=True, help='Resume file path')

        parser.print_help()    resume_parser.add_argument('--format', default='txt', choices=['txt', 'docx'], 

                               help='Output format (default: txt)')

if __name__ == "__main__":    resume_parser.add_argument('--interview', action='store_true', 

    main()                               help='Also generate interview questions')

    resume_parser.add_argument('--level', default='entry', choices=['entry', 'mid', 'senior'],
                               help='Job level for interview questions (default: entry)')
    resume_parser.add_argument('--gpa', help='Your GPA (optional, shown if >= 3.0)')
    resume_parser.add_argument('--coursework', help='Relevant coursework (optional)')
    
    # Cover letter mode
    cover_parser = subparsers.add_parser('cover-letter', help='Generate cover letter')
    cover_parser.add_argument('--jd', required=True, help='Job description file path')
    cover_parser.add_argument('--resume', help='Resume file path (optional but recommended)')
    cover_parser.add_argument('--name', required=True, help='Your name')
    cover_parser.add_argument('--company', required=True, help='Company name')
    cover_parser.add_argument('--position', required=True, help='Position title')
    cover_parser.add_argument('--email', help='Your email')
    cover_parser.add_argument('--phone', help='Your phone')
    cover_parser.add_argument('--linkedin', help='Your LinkedIn URL')
    cover_parser.add_argument('--format', default='txt', choices=['txt', 'docx'], 
                               help='Output format (default: txt)')
    
    # Interview prep mode
    interview_parser = subparsers.add_parser('interview', help='Generate interview questions')
    interview_parser.add_argument('--jd', required=True, help='Job description file path')
    interview_parser.add_argument('--resume', help='Resume file path (optional)')
    interview_parser.add_argument('--level', default='entry', choices=['entry', 'mid', 'senior'],
                                   help='Job level (default: entry)')
    interview_parser.add_argument('--format', default='txt', choices=['txt', 'docx'], 
                                   help='Output format (default: txt)')
    
    # Web interface mode
    web_parser = subparsers.add_parser('web', help='Launch web interface')
    
    args = parser.parse_args()
    
    # Validate configuration
    Config.validate()
    
    # Route to appropriate function
    if args.mode == 'optimize-resume':
        optimize_resume(args)
    elif args.mode == 'cover-letter':
        generate_cover_letter(args)
    elif args.mode == 'interview':
        generate_interview_questions(args)
    elif args.mode == 'web':
        print_info("Launching web interface...")
        try:
            import app
            app.main()
        except ImportError:
            print_error("Web interface not available. Install Streamlit: pip install streamlit")
            print_info("Or run: streamlit run app.py")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
