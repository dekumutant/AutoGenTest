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
            "gpt-3.5-turbo-16k",
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
termination_notice = (
    '\n\nDo not show appreciation in your responses, say only what is necessary. '
    'if "Thank you" or "You\'re welcome" are said in the conversation, then say TERMINATE '
    'to indicate the conversation is finished and this is your last message.'
)
prompt = """
Generate code that prints numbers 1 to 100
"""
task = prompt + termination_notice
user_proxy.initiate_chat(
    assistant,
    message=task
)