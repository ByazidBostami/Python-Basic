prompt="\nTell me something, i will repeat back to you "
prompt+="\nEnter 'quit' to end the program "
message=''
while message!='quit':
    message=input(prompt)
    if message!="quit":
        print(message)