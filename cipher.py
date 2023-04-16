#Getting the word list, seven letter word and each letter within the ciphertext into arrays
import math
wordList,sevenLetter,possibleKey,commonWords=[],[],[],[]
startingIndex=0
finalanswer=('',startingIndex)
with open('words.txt') as f:
    for line in f:
        wordList.append(line.strip())
with open('most_common.txt') as g:
    for line in g:
        commonWords.append(line.strip())
ciphertext='ntpspxvqzklzxizhycjyutbfxcemjhfvzqvrpvvvrpyvzrb'
cipherList=[]
for letter in ciphertext:
    cipherList.append(ord(letter)-96)
for word in wordList:
    if(len(word)==7):
        sevenLetter.append(word)
  
#print ('Seven letter list', len(sevenLetter))

#loop through each seven letter word and send the ciphertext to decode function and append to the answerList
def main():
    for key in sevenLetter:
        for letter in key:
            possibleKey.append(ord(letter)-96)
        decode(possibleKey,cipherList,key)
        possibleKey.clear() 
    print (finalanswer)

#Subtract each letter within the cipher text with the possible key as num and convert it back to a string
#then pass it to the match function. Append possible answer if returned true
def decode(key,list,actualKey):
    i=0
    newlist,charlist=[],''
    global finalanswer
    for num in list:
        if(i>6):
           i=0
        if(num-key[i]>0):
            newlist.append(num-key[i]) 
        else:
            if(num-key[i]+26==26):
                newlist.append(0)
            else:
                newlist.append(num-key[i]+26)
        i+=1
    for num2 in newlist:
        charlist+=(chr(num2+97))
    index=match(charlist)
    answer=(charlist,index,actualKey)
    if(answer[1]>finalanswer[1]):
        finalanswer=answer
    #if(match(charlist)):
    #    answerList.append(charlist)
#look for plaintext that starts with a word and return true 
def match(ans):
    score=0
    for word in commonWords:
        if(ans.find(word)>=0):
            score+=math.factorial(len(word))
    return score
main()