To allow docket to work on windows.
Download docker
R=In admin powershell run wsl --update
wsl -l -v
https://www.youtube.com/watch?v=JRluDLoiHXM&t=309s explains

https://microsoft.github.io/autogen/docs/FAQ/


For GPT-3.5 use below so it doesnt get stuck in a loop
prompt = "Some user query"

termination_notice = (
    '\n\nDo not show appreciation in your responses, say only what is necessary. '
    'if "Thank you" or "You\'re welcome" are said in the conversation, then say TERMINATE '
    'to indicate the conversation is finished and this is your last message.'
)

prompt += termination_notice