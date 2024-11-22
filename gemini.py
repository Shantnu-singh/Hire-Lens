import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

ats_check_promt = """"
Analyze the provided job description and the resume image, converting the resume image into text first. Compare the extracted resume details against the key skills, qualifications, experience, and requirements mentioned in the job description. Based on this analysis, calculate an ATS (Applicant Tracking System) score from 0 to 100, where 100 represents a perfect match and 0 represents no match.

For each section (Skills, Experience, Education, Keywords, Job-specific requirements), provide a detailed breakdown of the score. Include reasons why points were awarded or deducted in each category. Indicate areas where the resume aligns well with the job description and where it falls short, and suggest specific improvements that could raise the score.

Use the following guidelines for scoring:

Skills Match (30 percent of the score): Evaluate how well the skills mentioned in the resume align with those in the job description.
Experience Match (30 percent of the score): Assess the relevance of the candidate's experience based on years, job titles, and responsibilities.
Education Match (15 percent of the score): Check if the educational qualifications align with the job’s requirements.
Keyword Usage (15 percentof the score): Measure the presence of specific keywords from the job description in the resume.
Job-specific Requirements (10 percent of the score): Determine how well the resume addresses unique requirements or preferences mentioned in the job description.
At the end, provide a summary that includes:

The final ATS score.
A breakdown of the score for each category.
Justifications for the scoring.
Suggestions for improvement if the match is below 70. """

resume_to_personality = """Analyze the provided resume to infer the candidate's personality traits. Consider all factors presented in the resume, including work experience, job titles, skills, educational background, accomplishments, responsibilities, achievements, extracurricular activities, and formatting style. Use the following criteria to assess the candidate's personality:

Professionalism: Evaluate the candidate's attention to detail, clarity, and organization in presenting their work history, skills, and achievements. Consider the formatting, language used, and overall layout.

Communication Skills: Assess the clarity, conciseness, and specificity of the descriptions in the resume. Determine if the candidate effectively communicates their responsibilities, accomplishments, and skills.

Work Ethic and Motivation: Analyze the depth of experience, the progression in roles, and any evidence of going above and beyond in previous positions. Consider any volunteer work, side projects, or certifications that indicate a passion for learning and professional growth.

Leadership and Teamwork: Look for evidence of leadership roles, team projects, or collaborative accomplishments. Assess how the candidate describes their involvement and contributions to teams or organizations.

Problem-Solving and Initiative: Identify examples of problem-solving, critical thinking, or initiatives taken by the candidate in past roles. Look for examples of improvements, optimizations, or innovative solutions they have been involved in.

Adaptability and Flexibility: Check for diverse experiences, skills, or transitions between industries or roles. Consider any upskilling, learning of new tools, or shifts in responsibilities that demonstrate adaptability.

Attention to Detail: Evaluate the resume for any errors or inconsistencies. Consider how the candidate describes their work, focusing on whether they provide specific metrics, results, or detailed examples.

Creativity and Innovation: Look for any indicators of creative thinking, such as unique accomplishments, out-of-the-box projects, or unusual skills that highlight innovation.

Based on these criteria, provide a summary of the candidate's inferred personality traits, strengths, and areas of potential growth. Use specific examples from the resume to support your conclusions and make sure to provide a balanced assessment.

End with a summary that includes:

A list of identified personality traits.
Strengths demonstrated by the candidate.
Areas for development or potential gaps.
How well the candidate’s personality might fit into different types of work environments or roles.
"""
missing_keyword_prompt = """
Analyze the provided job description and compare it with the resume. Identify all the keywords and key phrases mentioned in the job description that are missing in the resume. Provide only a list of these missing keywords and key phrases, without any additional information or explanation."""

def parse_resume(desc , resume , prompt):
    responce = model.generate_content([desc , resume[0] , prompt])
    return responce.text
    


