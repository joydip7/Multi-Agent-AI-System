from utils import call_llm

class StrategyAgent:
    def execute(self, goal):
        print("\n[Strategy Agent] Determining optimal execution strategy...")

        system_prompt = """
        You are an AI meta-strategist.

        Your job is to analyze a goal and decide:
        - Is it business-related?
        - Is it technical?
        - Is it research-based?
        - Is it creative?

        Then recommend an execution strategy.
        """

        user_prompt = f"""
        Analyze this goal and determine:
        1. Goal Category
        2. Recommended Execution Approach
        3. Key Risk Areas

        Goal:
        {goal}
        """

        return call_llm(system_prompt, user_prompt)
