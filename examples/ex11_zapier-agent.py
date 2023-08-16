import os
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.agents import AgentType
from langchain.utilities.zapier import ZapierNLAWrapper


os.environ.get('OPENAI_API_KEY')
os.environ.get('ZAPIER_NLA_API_KEY')

llm = OpenAI(temperature=0)

zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(
    toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

if __name__ == "__main__":
    agent.run(
        "Send a professional email to carlosmasson96@gmail.com congratulating him on his AI accomplishment."
    )
