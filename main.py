from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent
from memory import Memory
from agents.strategist import StrategyAgent



class MultiAgentSystem:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()
        self.memory = Memory()
        self.strategist = StrategyAgent()


    def run(self, goal):
        print("\n[System] Starting multi-agent collaboration...\n")

        # Step 0: Strategy Analysis
        strategy = self.strategist.execute(goal)
        self.memory.add("Strategy Analysis:\n" + strategy)

        # Step 1: Planning
        tasks = self.planner.execute(goal)
        self.memory.add("Planning Stage:\n" + "\n".join(tasks))

        # Step 2: Research
        results = []
        for task in tasks:
            result = self.researcher.execute(goal,task)
            results.append(result)

        self.memory.add("Research Stage:\n" + "\n\n".join(results))

        # Step 3: Writing
        draft_report = self.writer.execute(results)
        self.memory.add("Draft Report:\n" + draft_report)

        # Step 4: Review & Improve
        final_output = self.reviewer.execute(draft_report)

        print("\n[System Memory Log]")
        print(self.memory.get_context())


        print("\n[System] Multi-Agent Execution Completed Successfully.\n")

        return final_output


if __name__ == "__main__":
    print("=== Autonomous Multi-Agent Task Collaboration System ===")
    goal = input("\nEnter your complex goal: ")

    system = MultiAgentSystem()
    output = system.run(goal)

    print("\n===== FINAL REFINED OUTPUT =====\n")
    print(output)
