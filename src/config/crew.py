"""Configuration for the CrewAI components."""

from crewai import Agent, Task, Process, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_search_tool():
    """Get the SerperDev search tool instance."""
    return SerperDevTool()

def create_blog_writer_agent(search_tool):
    """Create the blog writer agent."""
    return Agent(
        role="Senior Blog Writer",
        goal="Write a blog according to the client's requirements.",
        backstory="I have been writing blogs for the past 5 years and have written over 1000 blogs.",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool],
    )

def create_manager_agent():
    """Create the manager agent."""
    return Agent(
        role="Manager",
        goal="Manage the team and ensure the blog is written according to the client's requirements.",
        backstory="I have been managing teams for the past 10 years and have managed over 100 projects.",
        verbose=True,
        allow_delegation=True,
    )

def create_blog_task(agent, manager, topic="Generative AI industry", word_count=2000):
    """Create a blog writing task."""
    return Task(
        description=f"Write a blog on the benefits of AI in the {topic}. The blog should be {word_count} words long and should be written according to the client's requirements.",
        expected_output=f"A {word_count}-word blog on the benefits of AI in the {topic}.",
        agent=agent,
        manager=manager,
    )

def setup_crew(agents, tasks, manager):
    """Create and configure the CrewAI crew."""
    return Crew(
        agents=agents,
        tasks=tasks,
        manager_agent=manager,
        cache=True,
        verbose=True,
        process=Process.hierarchical,
        planning=True,
    )
