# 🎨 System Architecture - AI Resume & Portfolio Builder

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   AI RESUME & PORTFOLIO BUILDER                          │
│                         System Architecture                              │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                           USER INTERFACES                                │
├─────────────────────────────┬───────────────────────────────────────────┤
│    WEB INTERFACE (app.py)   │    CLI INTERFACE (main.py)               │
│                             │                                           │
│  • Streamlit-based GUI      │  • Command-line arguments                │
│  • Drag-and-drop uploads    │  • Subcommands                           │
│  • Real-time previews       │  • Colored output                        │
│  • One-click downloads      │  • Batch processing                      │
│  • Mobile-responsive        │  • Scriptable                            │
└─────────────────────────────┴───────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          CORE APPLICATION LAYER                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────┐  ┌────────────────────┐  ┌──────────────────┐ │
│  │  Resume Optimizer  │  │  Cover Letter Gen  │  │  Interview Gen   │ │
│  │                    │  │                    │  │                  │ │
│  │  • AI tailoring    │  │  • Personalized    │  │  • Technical Q's │ │
│  │  • ATS optimization│  │  • Company research│  │  • Behavioral Q's│ │
│  │  • Keyword match   │  │  • STAR examples   │  │  • Situational   │ │
│  │  • Student focus   │  │  • Multiple formats│  │  • Prep tips     │ │
│  └────────────────────┘  └────────────────────┘  └──────────────────┘ │
│                                                                          │
│  ┌────────────────────┐  ┌────────────────────┐  ┌──────────────────┐ │
│  │  Portfolio Gen     │  │  File Processor    │  │  Configuration   │ │
│  │                    │  │                    │  │                  │ │
│  │  • Project display │  │  • PDF reading     │  │  • API keys      │ │
│  │  • Skills org      │  │  • DOCX support    │  │  • Settings      │ │
│  │  • Markdown output │  │  • TXT handling    │  │  • Validation    │ │
│  │  • GitHub ready    │  │  • Format convert  │  │  • Defaults      │ │
│  └────────────────────┘  └────────────────────┘  └──────────────────┘ │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          AI & EXTERNAL SERVICES                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              Google Gemini AI (gemini-1.5-flash)                │   │
│  │                                                                  │   │
│  │  • Resume optimization prompts                                  │   │
│  │  • Cover letter generation                                      │   │
│  │  • Interview question creation                                  │   │
│  │  • Portfolio content generation                                 │   │
│  │  • Keyword extraction from job descriptions                     │   │
│  │                                                                  │   │
│  │  Fallback: Template-based generation (no API required)          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                            DATA FLOW                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  INPUT                  PROCESSING               OUTPUT                 │
│  ─────                  ──────────               ──────                 │
│                                                                          │
│  📄 Job Description  →  🤖 AI Analysis       →  📄 Optimized Resume     │
│  📄 Resume          →  🔍 Keyword Extract   →  ✉️  Cover Letter        │
│  👤 User Info       →  ✍️  Content Gen      →  ❓ Interview Questions  │
│  🎯 Projects        →  🎨 Formatting        →  🎨 Portfolio Content    │
│                                                                          │
│  All processing in-memory • No data storage • Auto cleanup              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                        DEPLOYMENT ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐               │
│  │  Streamlit   │   │   Heroku     │   │   Railway    │               │
│  │    Cloud     │   │              │   │              │               │
│  │   (Free)     │   │  (Freemium)  │   │  (Freemium)  │               │
│  └──────────────┘   └──────────────┘   └──────────────┘               │
│                                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐               │
│  │    Render    │   │    Local     │   │  University  │               │
│  │              │   │    Server    │   │    Server    │               │
│  │  (Freemium)  │   │  (On-prem)   │   │  (On-prem)   │               │
│  └──────────────┘   └──────────────┘   └──────────────┘               │
│                                                                          │
│  All platforms support: Python 3.8+, pip, environment variables         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                          SECURITY ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  🔐 API Key Management                                                  │
│     └─→ Environment variables (.env file)                               │
│     └─→ Never committed to git (.gitignore)                             │
│     └─→ Platform secrets on cloud deployment                            │
│                                                                          │
│  🛡️  Data Privacy                                                       │
│     └─→ No database or persistent storage                               │
│     └─→ In-memory processing only                                       │
│     └─→ Temporary files auto-deleted                                    │
│     └─→ No user tracking or logging                                     │
│                                                                          │
│  ✅ Input Validation                                                    │
│     └─→ File type checking                                              │
│     └─→ File size limits (10MB)                                         │
│     └─→ Sanitized inputs                                                │
│     └─→ Error handling and graceful failures                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                           FILE STRUCTURE TREE                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  muti/                                                                   │
│  ├── 🌐 app.py                    # Streamlit web interface            │
│  ├── ⚡ main.py                   # CLI entry point                     │
│  ├── ⚙️  config.py                 # Configuration                      │
│  │                                                                       │
│  ├── 📄 resume_optimizer.py       # Resume AI engine                   │
│  ├── ✉️  cover_letter_generator.py # Cover letter AI                   │
│  ├── ❓ interview_generator.py     # Interview questions AI            │
│  ├── 🎨 portfolio_generator.py     # Portfolio AI                      │
│  ├── 📁 file_processor.py          # File I/O utilities                │
│  │                                                                       │
│  ├── 📦 requirements.txt           # Dependencies                       │
│  ├── 🔐 .env.example               # Environment template              │
│  ├── 🚫 .gitignore                 # Git ignore rules                  │
│  │                                                                       │
│  ├── 📖 README.md                  # Main documentation                │
│  ├── 🚀 QUICKSTART.md              # 5-min setup guide                 │
│  ├── 🌐 DEPLOYMENT.md              # Deploy instructions               │
│  ├── 📋 CHANGELOG.md               # Version history                   │
│  ├── 🎯 PROJECT_SUMMARY.md         # Project overview                  │
│  │                                                                       │
│  ├── 📂 examples/                  # Sample files                       │
│  │   ├── sample_job_description.txt                                    │
│  │   └── sample_resume.txt                                             │
│  │                                                                       │
│  └── 📂 outputs/                   # Generated documents (auto-created)│
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                         TECHNOLOGY STACK                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Core:        Python 3.8+                                               │
│  AI/ML:       Google Gemini 1.5 (gemini-1.5-flash)                     │
│  Web:         Streamlit 1.39.0                                          │
│  Docs:        python-docx 1.1.2, PyPDF2 3.0.1                          │
│  Config:      python-dotenv 1.0.1                                       │
│                                                                          │
│  All open-source, well-maintained, MIT licensed                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                        FEATURE COMPLETION STATUS                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Resume Optimizer            100% Complete                           │
│  ✅ Cover Letter Generator      100% Complete                           │
│  ✅ Interview Prep Generator    100% Complete                           │
│  ✅ Portfolio Generator          100% Complete                           │
│  ✅ Web Interface (Streamlit)   100% Complete                           │
│  ✅ CLI Interface                100% Complete                           │
│  ✅ File Processing (PDF/DOCX)  100% Complete                           │
│  ✅ Configuration System         100% Complete                           │
│  ✅ Error Handling               100% Complete                           │
│  ✅ Documentation                100% Complete                           │
│  ✅ Example Files                100% Complete                           │
│  ✅ Deployment Ready             100% Complete                           │
│                                                                          │
│  🎉 PROJECT STATUS: PRODUCTION READY! 🎉                                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                            QUICK START                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. pip install -r requirements.txt                                     │
│  2. Copy .env.example to .env                                           │
│  3. Add your GEMINI_API_KEY to .env                                     │
│  4. streamlit run app.py                                                │
│  5. Open http://localhost:8501                                          │
│  6. Start creating professional documents! 🚀                           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

```

---

**Legend:**
- 📄 Document/File
- 🤖 AI Processing
- 🔍 Analysis
- ✍️  Generation
- 🎨 Formatting
- 🔐 Security
- ⚙️  Configuration
- 📦 Package/Module
- 🌐 Web Interface
- ⚡ CLI Interface
- ✅ Complete
- 📖 Documentation

---

**Built with ❤️ for students worldwide**

*Architecture designed for: Scalability • Maintainability • Simplicity*
