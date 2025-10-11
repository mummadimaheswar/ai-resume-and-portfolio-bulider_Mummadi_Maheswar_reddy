"""
Configuration file for AI Resume & Portfolio Builder
Production-ready configuration with validation and fallbacks
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

class Config:
    """Central configuration for the application"""
    
    # ==================== API SETTINGS ====================
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
    
    # ==================== FILE PROCESSING ====================
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    SUPPORTED_FORMATS = ['pdf', 'txt', 'doc', 'docx']
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'outputs')
    
    # ==================== RESUME OPTIMIZATION ====================
    KEYWORD_DENSITY_TARGET = 0.02  # 2% keyword density
    MAX_BULLET_POINTS = 6
    MIN_BULLET_POINTS = 3
    
    # ==================== GENERATION SETTINGS ====================
    # Interview Questions
    TECHNICAL_QUESTIONS = 6
    BEHAVIORAL_QUESTIONS = 5
    SITUATIONAL_QUESTIONS = 4
    
    # Temperature settings for AI generation
    TEMPERATURE_CREATIVE = 0.8  # For cover letters and portfolios
    TEMPERATURE_FACTUAL = 0.7   # For resumes and questions
    
    # ==================== STUDENT-FOCUSED FEATURES ====================
    HIGHLIGHT_PROJECTS = True
    HIGHLIGHT_SKILLS = True
    INCLUDE_GPA = True  # Show GPA if above 3.0
    INCLUDE_COURSEWORK = True
    
    # ==================== APPLICATION SETTINGS ====================
    APP_NAME = "AI Resume & Portfolio Builder"
    APP_VERSION = "1.0.0"
    DEBUG_MODE = os.getenv('DEBUG', 'False').lower() == 'true'
    
    @classmethod
    def validate(cls) -> bool:
        """Validate critical configuration"""
        if not cls.GEMINI_API_KEY:
            print("⚠️  Warning: GEMINI_API_KEY not set. AI features will be limited.")
            return False
        return True
    
    @classmethod
    def ensure_output_dir(cls) -> Path:
        """Ensure output directory exists"""
        output_path = Path(cls.OUTPUT_DIR)
        output_path.mkdir(parents=True, exist_ok=True)
        return output_path
    
    @classmethod
    def get_info(cls) -> dict:
        """Get configuration information"""
        return {
            "app_name": cls.APP_NAME,
            "version": cls.APP_VERSION,
            "api_configured": bool(cls.GEMINI_API_KEY),
            "model": cls.GEMINI_MODEL,
            "output_dir": cls.OUTPUT_DIR,
            "debug_mode": cls.DEBUG_MODE
        }
