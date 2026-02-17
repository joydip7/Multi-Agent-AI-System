from utils import call_llm

class ResearchAgent:
    def execute(self, goal, task):
        print(f"\n[Research Agent] Deep analysis for: {task}")

        system_prompt = """
        You are a domain expert analyst.

        Provide:
        - Structured analysis
        - Practical implementation insights
        - Real-world considerations
        - Risks and mitigation strategies

        Be specific. Avoid generic advice.
        """

        user_prompt = f"""
        Overall Goal:
        {goal}

        Current Task:
        {task}

        Provide output in this format:

        1. Objective
        2. Key Actions
        3. Tools/Resources Required
        4. Risks
        5. Expected Outcome
        """

        return call_llm(system_prompt, user_prompt)
