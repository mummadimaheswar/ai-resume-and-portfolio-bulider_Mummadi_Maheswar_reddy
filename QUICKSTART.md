# 🚀 Quick Start Guide - AI Resume & Portfolio Builder

## Get Started in 5 Minutes!

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up API Key
1. Get free API key: https://makersuite.google.com/app/apikey
2. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
3. Edit `.env` and add your API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### Step 3: Launch the App
```bash
streamlit run app.py
```

### Step 4: Upload & Generate!
1. Go to http://localhost:8501
2. Choose your tool (Resume, Cover Letter, Interview Prep)
3. Upload your files
4. Fill in the form
5. Click Generate!
6. Download your professional documents

## 🎯 Tips for Best Results

### Resume Optimization
- ✅ Use clear, well-formatted resume
- ✅ Include complete job description
- ✅ Add your GPA if >= 3.0
- ✅ List relevant coursework

### Cover Letter
- ✅ Research the company first
- ✅ Mention specific projects
- ✅ Be authentic and enthusiastic
- ✅ Proofread before submitting

### Interview Prep
- ✅ Practice answers out loud
- ✅ Use STAR method for behavioral questions
- ✅ Prepare 3-5 strong examples
- ✅ Research company thoroughly

## 🆘 Need Help?

### Common Issues

**"GEMINI_API_KEY not found"**
- Solution: Create `.env` file with your API key

**"Module not found: streamlit"**
- Solution: Run `pip install streamlit`

**"Port 8501 already in use"**
- Solution: Close other Streamlit apps or use a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```

### Still Need Help?
- 📖 Read the full README.md
- 🐛 Check GitHub Issues
- 💬 Ask in Discussions

## 📱 Want the CLI Instead?

### Optimize Resume
```bash
python main.py optimize-resume --jd job.txt --resume resume.pdf --interview
```

### Generate Cover Letter
```bash
python main.py cover-letter --jd job.txt --name "Your Name" --company "Company" --position "Position"
```

### Interview Questions
```bash
python main.py interview --jd job.txt --level entry
```

---

**Happy Job Hunting! 🎉**
