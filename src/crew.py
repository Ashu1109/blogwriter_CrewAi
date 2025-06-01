from crewai import Agent, Task, Process, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class BlogWriterCrew:
    def __init__(self):
        self.search = SerperDevTool()
        self.setup_agents()
        self.setup_tasks()
        self.setup_crew()
        
    def setup_agents(self):
        self.agent1 = Agent(
            role="Senior Blog Writer",
            goal="Write a blog according to the client's requirements.",
            backstory="I have been writing blogs for the past 5 years and have written over 1000 blogs.",
            verbose=True,
            allow_delegation=True,
            tools=[self.search],
        )
        
        self.manager = Agent(
            role="Manager",
            goal="Manage the team and ensure the blog is written according to the client's requirements.",
            backstory="I have been managing teams for the past 10 years and have managed over 100 projects.",
            verbose=True,
            allow_delegation=True,
        )
    
    def setup_tasks(self):
        self.task1 = Task(
            description="Write a blog on the benefits of AI in the Generative AI industry(RAG, LLM,N8N,AI Agents, AI Chatbot, AI Image Generator, AI Video Generator, AI Audio Generator, AI Music Generator, AI Art Generator, etc). The blog should be 2000 words long and should be written according to the client's requirements.",
            expected_output="A 2000-word blog on the benefits of AI in the Generative AI industry.",
            agent=self.agent1,
            manager=self.manager,
        )
    
    def setup_crew(self):
        self.crew = Crew(
            agents=[self.agent1],
            tasks=[self.task1],
            manager_agent=self.manager,
            cache=True,
            verbose=True,
            process=Process.hierarchical,
            planning=True,
        )
    
    def run(self):
        return self.crew.kickoff()

# Simple function to create and run the crew
def create_blog():
    blog_writer = BlogWriterCrew()
    return blog_writer.run()

if __name__ == "__main__":
    create_blog()
