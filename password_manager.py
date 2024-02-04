from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)'''
    
def load_key():
    file=open("key.key",'rb')
    key=file.read()
    file.close()
    return key


key=load_key()
fer=Fernet(key)


def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("User ACC:",user,", Password:",fer.decrypt(passw.encode()).decode())
# the rstrip() will do not return the new line that we added in the add mode , strips it off to yhe output.
 # the split("|") do split based on the given parameter into list of elements.           
def add():
    name=input("Enter Account name: ")
    pwd=input('Enter password: ')

    with open('passwords.txt','a') as f:
        f.write(name + '|'+ fer.encrypt(pwd.encode()).decode() + "\n")

#encode()-converts string to bytes
#decode()-converts bytes to string

# 'w' - if passwords.txt already exists it clears the file and write to it
# 'a' - it will append the content to existing file,if file mentioned not present it creates a new one and append to it.
# 'r' - it just reads the content of the file mentioned
# the line with open() will defaultly closes the file itself.
    


while True:
    mode=input("would you like to add a new password or view existing ones(view,add) or q to quit?  ").lower()
    if mode=="q":
        break
    elif mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
        continue