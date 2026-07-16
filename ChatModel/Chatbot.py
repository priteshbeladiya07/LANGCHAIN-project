from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv() 
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
import sys
sys.stdout.reconfigure(encoding='utf-8')

model = ChatMistralAI(model="mistral-small-2506",temperature=1,max_tokens=20)
print("Choose your AI mode")
print("Press 1 for Angry mode")
print("Press 2 for Funny mode")
print("Press 3 for Sad mode")
choice = int(input("Tell Your Choice :-"))

if choice == 1:
  mode = "Angry"
elif choice ==2:
  mode ="Funny"
elif choice==3:
  mode="Sad"

message = [
       SystemMessage(content = f"yoa are ${mode} ai agents and give answer according this behavior")
]
print("--------Welcome dude,type 'exit' for leave application--------")
while True:
  
  prompt = input("you : ")
  message.append(HumanMessage(content=prompt))
  if prompt == "exit":
    break
  result = model.invoke(message)
  message.append(AIMessage(content = result.content))
  print("Bot :",result.content)
  