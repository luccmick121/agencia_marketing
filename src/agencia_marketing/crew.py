from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from agencia_marketing.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Carrega a API key do arquivo .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Cria uma instância do modelo Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5,
    google_api_key=GOOGLE_API_KEY
)

@CrewBase
class AgenciaMarketingCrew():
	"""AgenciaMarketing crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def pesquisador(self) -> Agent:
		@agent
	    return Agent(
			config=self.agents_config['pesquisador'],          
			llm=llm,
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	def estrategista(self) -> Agent:
		@agent
		return Agent(
			config=self.agents_config['estrategista'],
			verbose=True,
			llm=llm
		)

	def copywriter(self) -> Agent:
		@agent
		return Agent(
			config=self.agents_config['copywriter'],
			verbose=True,
			llm=llm
		)

	def gestor(self) -> Agent:
		@agent
		return Agent(
			config=self.agents_config['gestor'],
			verbose=True,
			llm=llm
		)

	def pesquisador_task(self) -> Task:
		@task
		return Task(
			config=self.tasks_config['pesquisador_task'],
			agent=self.pesquisador()
			
		)

	def estrategista_task(self) -> Task:
		@task
	    return Task(
			config=self.tasks_config['estrategista_task'],
			agent=self.estrategista(),
			output_file='trabalho.md'
			
		)

	def copywriter_task(self) -> Task:
		@task
		return Task(
			config=self.tasks_config['copywriter_task'],
			agent=self.copywriter()
			

		)

	def gestor_task(self) -> Task:
		@task
		return Task(
			config=self.tasks_config['gestor_task'],
			agent=self.gestor()
		
		)

	def crew(self) -> Crew:
		#"""Creates the AgenciaMarketing crew"""#
	    @crew
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)