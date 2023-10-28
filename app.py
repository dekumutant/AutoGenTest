import autogen
import openai
import os
from dotenv import load_dotenv
 

# Load the environment variables from dev.env
load_dotenv("dev.env")
##other model is gpt-3.5-turbo-16k-0613
config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": {
            "gpt-4",
            "gpt4",
            "gpt-4-32k",
            "gpt-4-32k-0314",
            "gpt-4-32k-v0314",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-0301",
            "chatgpt-35-turbo-0301",
            "gpt-35-turbo-v0301",
            "gpt",
        }
    }
)

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
Generate code that prints numbers 1 to 100
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)