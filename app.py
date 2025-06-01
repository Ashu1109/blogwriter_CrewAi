from crewai import Agent, Task, Process, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

search = SerperDevTool()

agent1 = Agent(
    role="Senior Blog Writer",
    goal="Write a blog for according to the client's requirements. ",
    backstory="I have been writing blogs for the past 5 years and have written over 1000 blogs.",
    verbose=True,
    allow_delegation=True,
    tools=[search],
)
manager = Agent(
    role="Manager",
    goal="Manage the team and ensure the blog is written according to the client's requirements.",
    backstory="I have been managing teams for the past 10 years and have managed over 100 projects.",
    verbose=True,
    allow_delegation=True,
)
task1 = Task(
    description="Write a blog on the benefits of AI in the Generative AI industry(RAG, LLM,N8N,AI Agents, AI Chatbot, AI Image Generator, AI Video Generator, AI Audio Generator, AI Music Generator, AI Art Generator, etc). The blog should be 2000 words long and should be written according to the client's requirements.",
    expected_output="A 2000-word blog on the benefits of AI in the Generative AI industry.",
    agent=agent1,
    manager=manager,
)
crew = Crew(
    agents=[agent1],
    tasks=[task1],
    manager_agent=manager,
    cache=True,
    verbose=True,
    process=Process.hierarchical,
    planning=True,
)

crew.kickoff()
