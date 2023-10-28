import autogen
import openai
import os
from dotenv import load_dotenv
 

# Load the environment variables from dev.env
load_dotenv("dev.env")
##other model is gpt-3.5-turbo-16k-0613
config_list = [
    {
        'model':'gpt-4',
        'api_key': os.getenv("API_KEY")
    }
]

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
   human_input_mode="TERMINATE"
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager,
    message="Find the latest paper about autogen on arxiv and find its potential applications"
)
# task2 = """
# Change the code in the file you just created to instead output numbers 1 to 200
# """

# user_proxy.initiate_chat(
#     assistant,
#     message=task2
# )