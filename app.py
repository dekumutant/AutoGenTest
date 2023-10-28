import autogen
import openai
import os
from dotenv import load_dotenv
 

# Load the environment variables from dev.env
load_dotenv("dev.env")

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

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

##to use docker code_execution_config={"work_dir": "web", "use_docker": "python:3"},
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("terminate"),
    code_execution_config={"work_dir": "web", "use_docker": "python:3"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Generate code that draws a picture of hatsune miku
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)
# task2 = """
# Change the code in the file you just created to instead output numbers 1 to 200
# """

# user_proxy.initiate_chat(
#     assistant,
#     message=task2
# )