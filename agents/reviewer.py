from utils import call_llm

class ReviewerAgent:
    def execute(self, report):
        print("\n[Reviewer Agent] Evaluating and refining output...")

        system_prompt = """
        You are a critical evaluator in an advanced AI system.

        Your job:
        - Evaluate quality
        - Identify weaknesses
        - Improve clarity and professionalism
        """

        user_prompt = f"""
        Step 1: Score the report out of 10.
        Step 2: Identify weaknesses.
        Step 3: Provide an improved final version.

        Report:
        {report}
        """

        return call_llm(system_prompt, user_prompt)
