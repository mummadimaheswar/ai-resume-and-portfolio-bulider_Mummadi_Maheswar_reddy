# 🚀 Auto Career Builder - Quick Start

## ONE-COMMAND CAREER PACKAGE GENERATOR

This tool **automatically generates** everything you need for a job application:
- ✅ **Optimized Resume** (ATS-friendly, keyword-matched)
- ✅ **Personalized Cover Letter** (company-specific)
- ✅ **Interview Prep Guide** (questions + STAR answers)
- ✅ **Portfolio Content** (GitHub-ready markdown)

---

## 🎯 How to Use (3 Simple Steps)

### Step 1: Add Your Files
Put these files in the project folder:
- `resume.txt` - Your current resume
- `jd.txt` - The job description you're applying to

*(Or use the example files in the `examples/` folder for testing)*

### Step 2: Run the Generator
Open terminal and run:
```bash
python auto_run.py
```

### Step 3: Get Your Documents
All documents are generated in the `outputs/` folder automatically!

---

## 📂 What You Get

After running, you'll find in `outputs/`:

1. **Resume_Optimized_XXXXXX.txt**
   - Tailored to the job description
   - Keywords optimized for ATS systems
   - Student-friendly formatting

2. **CoverLetter_Company_XXXXXX.txt**
   - Personalized for the company
   - Highlights your best fit
   - Professional tone

3. **InterviewPrep_level_XXXXXX.txt**
   - Common interview questions
   - STAR method sample answers
   - Company-specific prep tips

4. **Portfolio_XXXXXX.md**
   - GitHub README ready
   - Project highlights
   - Skills showcase

5. **PACKAGE_SUMMARY_XXXXXX.txt**
   - Overview of all generated files
   - Next steps checklist

---

## 🔧 Configuration (Optional)

### For AI-Powered Generation
Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

Without an API key, the tool uses **smart templates** (still very good!).

### Add Your Info
Edit these in `auto_run.py`:
```python
student_info = {
    'email': 'your.email@example.com',
    'phone': '+1-555-0100',
    'linkedin': 'https://linkedin.com/in/yourprofile'
}
```

---

## 💡 Tips

1. **Resume File**: Use plain text format (.txt) for best results
2. **Job Description**: Copy-paste the entire job posting into jd.txt
3. **Review & Customize**: Generated content is 90% ready - add personal touches!
4. **Multiple Applications**: Run it once per job - files are timestamped

---

## ⚡ Advanced: Web Interface

Want a visual interface instead?
```bash
streamlit run app.py
```

Then open: http://localhost:8501

---

## 🆘 Troubleshooting

**Problem**: "File not found"
- **Solution**: Make sure `resume.txt` and `jd.txt` exist in the project folder

**Problem**: "AI not available"
- **Solution**: This is OK! Templates still work. Add API key for full AI power.

**Problem**: "PDF support disabled"
- **Solution**: Run `pip install PyPDF2` (optional - only for PDF resumes)

---

## 📞 Need Help?

Check the `SUCCESS.md` file for detailed information or run:
```bash
python smart_career_builder.py
```
for the interactive version (asks questions).

---

## 🎉 That's It!

Just one command: `python auto_run.py`

**Good luck with your job search!** 🚀
