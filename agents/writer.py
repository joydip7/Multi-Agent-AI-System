from utils import call_llm

class WriterAgent:
    def execute(self, data):
        print("\n[Writer Agent] Creating executive-level draft...")

        combined_data = "\n\n".join(data)

        system_prompt = """
        You are an executive business report specialist.

        Produce:
        - Clear headings
        - Logical structure
        - Professional tone
        - Concise but detailed explanations
        """

        user_prompt = f"""
        Combine the following structured insights into a
        coherent executive-level report.

        {combined_data}
        """

        return call_llm(system_prompt, user_prompt)
