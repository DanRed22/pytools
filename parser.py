import csv

class Data:
    def __init__(self, question, a1, s1, a2, s2, a3, s3, a4, s4, a5, s5, a6, s6, a7, s7):
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        self.s7 = s7
    
    def __str__(self):
        return f'"{self.question}":[["{self.a1}","{self.s1}"],["{self.a2}","{self.s2}"],["{self.a3}","{self.s3}"],["{self.a4}","{self.s4}"],["{self.a5}","{self.s5}"],["{self.a6}","{self.s6}"],["{self.a7}","{self.s7}"]],'

data_list = []

# Specify the encoding as 'ISO-8859-1' (latin1)
with open('data.csv', 'r', encoding='ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)

    for row in csvreader:
        question, a1, s1, a2, s2, a3, s3, a4, s4, a5, s5, a6, s6, a7, s7 = row
        data = Data(question, a1, s1, a2, s2, a3, s3, a4, s4, a5, s5, a6, s6, a7, s7)
        data_list.append(str(data)+"\n")

with open('output.txt', 'w', encoding='utf-8') as textfile:
    textfile.writelines(data_list)
