from tkinter import *
import numpy
import random
import sys

def main():
    dna = e1.get() #DNAs  
    s = e2.get() #Sequence number 
    s = int(s)    
    a = e3.get() #Sequence length
    a = int(a)    
    m = 0 #Number of trials
        
    while True:
        m += 1 #Increase number of trial
        l_m = numpy.random.randint(4, 6, 1) #Generates number between 4-6. It will used creating a projection.
        l = l_m[0]
        d_m = numpy.random.randint(0, 2, 1) #Generates number between 0-2. It will used creating a projection
        d = d_m[0]
        motif_matrix = numpy.zeros((4, l-d), dtype=int) #The bucket created with matrix. l-d means that motif length(l) - tolerance(d)
        k = define_projection(l, d) #Creating projection with this function.
        for i in range(0, len(dna), a):     
            starting_point = numpy.random.randint(i, i+a-l+1 , 1) #Generates random starting point.
            applicant = search_motif(dna, starting_point, k) #Generates applicant motif
            motif_matrix = edit_motifMatrix(applicant, motif_matrix, l, d) #Edits bucket matrix by applicant motifs
        best_motif = control_matrix(motif_matrix, applicant, l, d, s) #Checks matrix for is projection best or not. 
        isBest = control_motif(best_motif, s) #If best prints valuables else tries one more time.
        if isBest == True:
            print('Motif Founded!')
            result_motif = create_best_motif(dna, starting_point, l)
            print("Position at: ", starting_point, " and motif is :", result_motif)
            myText.set(result_motif)
            myText1.set(starting_point)
            return
        else:
            #reseting bucket matrix
            motif_matrix = numpy.zeros((4, l-d), dtype=int)

def define_projection(pieces, tolerance): 
    #Generating a random projection.
    projection = random.sample(range(pieces), pieces - tolerance)
    projection.sort()
    return projection

def search_motif(dna, starting_point, k):
    #Generates applicant motif by starting point and projection.
    applicant_motif = []
    for i in range(len(k)):
        d = starting_point[0]
        d += k[i]
        applicant_motif.append(dna[d])
    return applicant_motif

def edit_motifMatrix(applicant, matrix, l, k):
    #Edits Bucket Motif
    for i in range(0, l-k, 1):
        if(applicant[i] == 'A' or applicant[i] == 'a'):
            matrix[0][i] += 1
        elif(applicant[i] == 'T' or applicant[i] == 't'):
            matrix[1][i] += 1
        elif(applicant[i] == 'G' or applicant[i] == 't'):
            matrix[2][i] += 1
        else:
            matrix[3][i] += 1
    return matrix

def control_matrix(matrix, applicant_motif, l, k, s):
    #Checks Bucket Motif for the motif
    best_motif = [0] * len(applicant_motif)
    for i in range(0, len(applicant_motif), 1):
        for j in range(0, 4, 1):
            if matrix[j][i] >= s:
                best_motif[i] = matrix[j][i]
    return best_motif

def control_motif(motif, s):
    #Checks motif for the best motif
    for i in range(0, len(motif)):
        if motif[i] >= s:
            continue
        else:
            return False
    return True   

def create_best_motif(dna, starting_point, l):
    #Generates best motif's starting position and how is placed.
    c_v = starting_point[0]
    g_motif = ['A'] * l
    for i in range(l):
        g_motif[i] = dna[c_v + i]
    return g_motif

#GUI Codes
master = Tk()
myText=StringVar();
myText1=StringVar();
Label(master, text="DNA").grid(row=0, sticky=W)
Label(master, text="Sequence Number").grid(row=1, sticky=W)
Label(master, text="Squence Length").grid(row=2, sticky=W)
Label(master, text="Motif: ").grid(row=3, sticky=W)
Label(master, text="Motif's index").grid(row=4, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
result1=Label(master, text="", textvariable=myText1).grid(row=4,column=1, sticky=W)
e1 = Entry(master)
e1.grid(row=0, column=1)
e2 = Entry(master)
e2.grid(row=1, column=1)
e3 = Entry(master)
e3.grid(row=2, column=1)
b = Button(master, text="Calculate", command=main)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
mainloop()
#GUI Codes End
    