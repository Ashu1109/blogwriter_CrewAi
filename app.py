from crewai import Agent, Task, Process, Crew, LLM
from crewai_tools import SerperDevTool, WebsiteSearchTool, YoutubeVideoSearchTool, YoutubeChannelSearchTool
from dotenv import load_dotenv
import os
load_dotenv()



# Initialize SerperDevTool with verified API key
search = SerperDevTool()

 #LLM Object from crewai package
llm=LLM( 
    model="groq/llama-3.1-8b-instant",
    temperature=0.7
    )
agent1 = Agent(
     role="Senior Blog Writer",
     goal="Write a blog for according to the client's requirements. ",
     backstory="I have been writing blogs for the past 5 years and have written over 1000 blogs.",
     verbose=True,
     allow_delegation=True,
     tools=[search],
     llm=llm #<<<<<<< add model to agent to ensure it uses it
 )
manager = Agent(
        role="Manager",
        goal="Manage the team and ensure the blog is written according to the client's requirements.",
        backstory="I have been managing teams for the past 10 years and have managed over 100 projects.",
        verbose=True,
        allow_delegation=True,
        llm=llm #<<<<<<< add model to agent to ensure it uses it
)
task1 = Task(
    description="Write a blog on the benefits of AI in the healthcare industry. The blog should be 2000 words long and should be written according to the client's requirements.",
    expected_output="A 2000-word blog on the benefits of AI in the healthcare industry.",
    agent=agent1,
    manager=manager,
)
crew = Crew(
     agents=[agent1],
     model="ollama/llama3.2:3b", #<<<<< add model to crew to ensure it uses it
     tasks= [task1],
     manager_agent=manager,
     cache=True,
     verbose=True,
     process=Process.hierarchical,
     planning=True, # I see better results with this
     planning_llm=llm
 )

crew.kickoff()


