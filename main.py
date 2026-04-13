# main.py

from dotenv import load_dotenv
load_dotenv() # <-- THIS MUST BE THE FIRST THING THAT RUNS

# Now all other imports will work
from crew import legal_assistant_crew

def run(user_input: str):
    result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

    print("-"*50)
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    user_input = (
        "A man broke into my house at night while my family was sleeping. "
        "He stole jewelry and cash from our bedroom. When I confronted him, "
        "he threatened me with a knife and ran away. We reported it to the police, "
        "but I'm not sure which legal charges should be filed under IPC."
    )

    run(user_input)



#just extra info
# main.py
#
# from dotenv import load_dotenv
# load_dotenv() # First line
# import os # Import os here
#
# # ---- ADD THESE TWO LINES FOR DEBUGGING ----
# print(f"My Google API Key is: {os.getenv('GOOGLE_API_KEY')}")
# print(f"My Tavily API Key is: {os.getenv('TAVILY_API_KEY')}")
# # -------------------------------------------
#
# from crew import legal_assistant_crew # Keep this after
#
# def run(user_input: str):
#     result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})
#
#     print("-"*50)
#     print(result)
#     print("-" * 50)
#
# if __name__ == "__main__":
#     user_input = (
#         "A man broke into my house at night while my family was sleeping. "
#         "He stole jewelry and cash from our bedroom. When I confronted him, "
#         "he threatened me with a knife and ran away. We reported it to the police, "
#         "but I'm not sure which legal charges should be filed under IPC."
#     )
#
#     run(user_input)