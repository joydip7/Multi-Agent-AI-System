from utils import call_llm

class PlannerAgent:
    def execute(self, goal):
        print("\n[Planner Agent] Strategically decomposing goal...")

        system_prompt = """
        You are a senior strategic project architect.

        Your job is to:
        - Analyze complex goals
        - Break them into logically ordered, actionable subtasks
        - Ensure realism and feasibility
        - Avoid vague tasks

        Always think step-by-step before producing final output.
        """

        user_prompt = f"""
        Break the following goal into 5 clear, practical subtasks.

        Format:
        1. Subtask
        2. Subtask
        3. Subtask
        4. Subtask
        5. Subtask

        Goal:
        {goal}
        """

        response = call_llm(system_prompt, user_prompt)

        tasks = [
            line.split(".", 1)[-1].strip()
            for line in response.split("\n")
            if line.strip() and line[0].isdigit()
        ]

        return tasks
