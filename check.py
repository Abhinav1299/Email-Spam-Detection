import os
from collections import Counter
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

def dict_create():
    direc="email/"

    files=os.listdir(direc)
    emails=[direc + email for email in files]

    words=[]
    count=len(emails)
    for email in emails:
        print(email)
        f=open(email)
        try:
            b=f.read()
            words+=b.split(" ")
            print(count)
            count-=1
        except Exception as e:
            pass

    # deleting non-alphabetic strings
    for i in range(len(words)):
        if(not words[i].isalpha()):
            words[i]=""

    dic=Counter(words)
    del dic[""]
    return dic.most_common(3000)

pi_in=open("X.pickle","rb")
feature=pickle.load(pi_in)
pi_in=open("y.pickle","rb")
label=pickle.load(pi_in)

x_train,x_test,y_train,y_test=tts(feature,label,test_size=0.2)

clf=MultinomialNB()
clf.fit(x_train,y_train)

d=dict_create()

pred=clf.predict(x_test)
print(accuracy_score(pred,y_test))

while True:
    input_features=[]
    s=input("Enter your mail : ")
    if(s=="exit"):
        break
    for key in d:
        input_features.append(s.count(key[0]))

    out=clf.predict([input_features])
    print(out)
    if(out[0]==0):
        print("Not spam email")
    else:
        print("spam email")