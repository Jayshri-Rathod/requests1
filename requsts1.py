import requests
import json

course_url= requests.get("http://saral.navgurukul.org/api/courses")
Data = course_url.json()
with open("data.json","w") as read_file:
    json.dump(Data,read_file,indent=4)

def my_function():
    serial_number=1
    for index in Data["availableCourses"]:
        print(serial_number,index["name"],index["id"])
        serial_number+=1
my_function()

topic_1=int(input("Enter the topic number:"))
next=input("Enter where you want to go next or previous(n/p):")
if next=="p":
    my_function()
    topic_1=int(input("Enter the topic number:"))
parent_url=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercises")
data=parent_url.json()
with open("parent.json","w") as read_file:
    json.dump(data,read_file,indent=4)
    
def saral_function():
    serial1=1
    serial_2=1
    topic_list=[]
    for index1 in data["data"]:
        if len(index1["childExercises"])==0:
            print("     ",serial1,index1["name"])
            topic_list.append(index1["name"])
            print("        ",serial_2,index1["slug"])
            serial1+=1
        else:
            serial_no2=1
            print("   ",serial1,index1["name"])
            topic_list.append(index1["name"])
            for questions in index1["childExercises"]:
                print("         ",serial_no2,questions["name"])
                serial_no2+=1
            serial1+=1
saral_function()

next=input("Enter where you want to go next or previous(n/p):")
if next=="p":
    my_function()
    topic_1=int(input("Enter the topic number:"))
    parent_url=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercises")
    data=parent_url.json()
    with open("parent.json","w") as read_file:
        json.dump(data,read_file,indent=4)
        saral_function()

question_list=[]
slug_list=[]
slug=int(input("Enter the parent number:"))
for index1 in data["data"][slug-1]["childExercises"]:
    s=1
    for index1 in data["data"][slug-1]["childExercises"]:
        print("           ",s,index1["name"])
        question_list.append(index1["name"])
        s+=1
    que=int(input("Enter question number:"))
    url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-1]["slug"]))
    DATA=url3.json()
    with open("question.json","w") as re_file:
        json.dump(DATA,re_file,indent=4)
        print(DATA["content"])
        break
else:
    s_no=1
    print("         ",s_no,".",data["data"][slug-1]["slug"])
    slug_list.append(data["data"][slug-1]["slug"])
    que=int(input("Enter question number:"))
    slug_url=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["slug"]))
    data1=slug_url.json()
    with open("questions.json","w") as read_file:
        json.dump(data1,read_file,indent=4)
        print(data1["content"])
    for index2 in range(len(slug_list)):
        privous=input("Enter where you want to go next or previous:(n/p)")
        if privous=="n":
            print("Next page.")
            break
        if privous=="p":
            print("No more questions.")
            break
for i in range(len(question_list)):
    p_n = input("p/n")
    if p_n == "n":
        url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que]["slug"]))
        DATA=url3.json()
        with open("question.json","w") as read_file:
            json.dump(DATA,read_file,indent=4)
            print(DATA["content"])
            que=que+1
            if que==len(question_list):
                print("no more question")
                break
    elif p_n=="p":
        url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-2]["slug"]))
        DATA=url3.json()
        with open("question.json","w") as read_file:
            json.dump(DATA,read_file,indent=4)
            print(DATA["content"])
            que=que+1
            break
        