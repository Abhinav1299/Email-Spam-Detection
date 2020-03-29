# import cv2
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
    #     print(email)
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


# feature vectorization and dataset

def dataset(dic):
    direc="email/"

    files=os.listdir(direc)
    emails=[direc + email for email in files]
    label=[]
    data_set=[]
    count=len(emails)
    for email in emails:
        words=[]
        data=[]
        try:
            f=open(email)
            b=f.read()
            words+=(b.split(" "))
            # print(words)

            for key in dic:
                data.append(words.count(key[0]))
            data_set.append(data)
            if ("ham" in email):
                label.append(0)
            if("spam" in email):
                label.append(1)
            print(count)
            count-=1
        except Exception as e:
            pass
    pi_out=open("X.pickle","wb")
    pickle.dump(data_set,pi_out)
    pi_out.close()
    pi_out=open("y.pickle","wb")
    pickle.dump(label,pi_out)
    pi_out.close()
    return data_set,label

        
# k,j = (dataset(dict_create()))
# print(len(k),len(j))

pi_in=open("X.pickle","rb")
feature=pickle.load(pi_in)
pi_in=open("y.pickle","rb")
label=pickle.load(pi_in)

x_train,x_test,y_train,y_test=tts(feature,label,test_size=0.2)

clf=MultinomialNB()
clf.fit(x_train,y_train)

pred=clf.predict(x_test)
print(pred)

print(accuracy_score(pred,y_test))
