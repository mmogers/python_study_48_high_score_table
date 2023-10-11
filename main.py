print("\U0001F4AF \033[1;32mHIGH SCORE TABLE\033[0m \U0001F4AF")

def myInputPrint(text):  #prints input text with green clolor 
  result = input(f"{text} \033[32m")
  print("\033[0m", end="")
  return result
  
while True:
  initials = myInputPrint("\nInput your initials > ")
  score = int(myInputPrint("Input your score > "))

  f = open("high.score" , "a+")
  f.write(f"{initials} {score}\n")
  print("\nADDED\n")
  again = myInputPrint("Add another? y/n? ").strip().lower()
  if again == "y":
    continue
  else:
    f.close()
    break
  
