@echo off
REM Quick Demo - Automatic Career Package Generator
REM Uses example files from the repository

echo.
echo ====================================================================
echo   AI CAREER BUILDER - AUTOMATIC DEMO
echo   Generating complete career package with example files...
echo ====================================================================
echo.

REM Check if files exist
if not exist "resume.txt" (
    echo ERROR: resume.txt not found!
    pause
    exit /b 1
)

if not exist "jd.txt" (
    echo ERROR: jd.txt not found!
    pause
    exit /b 1
)

REM Run the smart builder with example files
echo Using files:
echo   Resume: resume.txt
echo   Job Description: jd.txt
echo.
echo Starting generation in 3 seconds...
timeout /t 3 /nobreak > nul

REM Create input file for automated responses
(
    echo resume.txt
    echo jd.txt
    echo John Doe
    echo johndoe@email.com
    echo +1-555-0123
    echo https://linkedin.com/in/johndoe
    echo 3.7
    echo Data Structures, Algorithms, Machine Learning
) > temp_input.txt

REM Run with automated input
python smart_career_builder.py < temp_input.txt

REM Cleanup
del temp_input.txt

echo.
echo ====================================================================
echo   Check the 'outputs' folder for your generated documents!
echo ====================================================================
echo.
pause
