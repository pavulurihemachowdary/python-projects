with open("story.txt","r") as f:
    story=f.read()
#enumerate() in python gives us access to have both index and character once at a time

words=set()
start_of_word=-1
target_start="<"
target_end=">"


for i,char in enumerate(story):
    if char==target_start:
        start_of_word=i
    if char==target_end and start_of_word!=-1:
        words.add(story[start_of_word:i+1])
        start_of_word=-1
answers={}
for i in words:
    ans=input("enter a word for "+i+": ")
    answers[i]=ans

for i in words:
    story=story.replace(i,answers[i])

print(story)
