from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chat_models import ChatOpenAI
import os
from dotenv import  load_dotenv
from marshmallow.fields import Tuple

load_dotenv()
mykey_openai = os.getenv("mykey_openai")
os.environ["TAVILY_API_KEY"] = os.getenv("tavily_apikey")

llm_openai = ChatOpenAI(model="gpt-3.5-turbo", api_key=mykey_openai)

tools = [TavilySearchResults(max_results=1)]
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm_openai, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
result = agent_executor.invoke({"input": "Türkiye bir sonraki yerel seçimleri hangi tarihte gerçekleştirecek? cevabı bulduktan sonra yanıtı türkçe yaz"}, handle_parsing_errors = True)

print("*"*100)
print(f"Sorunuz şuydu: {result["input"]}")
print("*"*100)
print(f"Yanıt şu: {result["output"]}")
