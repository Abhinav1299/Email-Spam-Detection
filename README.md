# Introduction
A python script which uses machine learning model to detect whether an email is spam or ham (not spam). The accuracy of this model is about 92%.

# Dataset
Data is obtained from the following link : http://www2.aueb.gr/users/ion/data/enron-spam/


The dataset consists of two directories, spam and ham. For the purpose of simplicity, the files of both the folders are collected in one main folder "email". Since the name of the text files contains the keyword "ham" or "spam" as its substring, it is easy to distinguish the two classes.

The complete dataset can be downloaded from the link and copied in email folder. 

# How it Works
The ***spam.py*** script is run to read each and every email and create a dictionary of top 3000 words. The Dictionary is sorted on the basis of most frequent words. Then corresponding to each email, all the words of the dictionary are counted and *oneHotEncoded* feature matrix is created. Corresponding label vectors are also identified. This data is stored in *pickle* files. Then our model is trained on **Naive Bayes** algorithm and accuracy is calculated.

The ***check.py*** script is designed to provide user to input some random email, and the model after one time training could be able to detect whether the user entered a *spam* email or a *ham* email.
