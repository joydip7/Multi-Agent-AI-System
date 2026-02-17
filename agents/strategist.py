from utils import call_llm


class StrategyAgent:
    def execute(self, goal):
        print("\n[Strategy Agent] Determining optimal execution strategy...")

        system_prompt = """
You are an AI executive strategist.

Your output must be structured, concise, and professional.
Avoid long paragraphs.
Use clear headings and bullet points.

Follow this EXACT structure:

🎯 Executive Overview

📌 Goal Classification
- Business: Yes/No
- Technical: Yes/No
- Research: Yes/No
- Creative: Yes/No
- Primary Category: <One clear category>

🧠 Recommended Execution Strategy
1. <Short action step>
2. <Short action step>
3. <Short action step>

⚠ Key Risk Areas
- <Risk 1> (Impact: Low/Medium/High)
- <Risk 2> (Impact: Low/Medium/High)
- <Risk 3> (Impact: Low/Medium/High)

Rules:
- Keep it clean and structured.
- No long paragraphs.
- No repeated text.
- No unnecessary explanations.
"""

        user_prompt = f"""
Analyze the following goal and generate a structured executive strategy report.

Goal:
{goal}
"""

        return call_llm(system_prompt, user_prompt)
