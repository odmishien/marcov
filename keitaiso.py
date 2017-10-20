import sys
import MeCab
import random
import re

f = open("dazai.txt")
data = f.read()
data = re.sub(r'[a-z]+', "", data)
data=re.sub(r'[!-~]', "", data)#半角記号,数字,英字
data=re.sub(r'[︰-＠]', "", data)#全角記号

tagger = MeCab.Tagger("-Owakati")
node = tagger.parse(data)

def create_tw(wordlist):
    markov = {}
    w1 = ""
    w2 = ""
    w3 = ""
    w4 = ""
    w5 = ""
    endword = ["。", "!", "？"]
    for word in wordlist:
        if w1 and w2 and w3 and w4 and w5:
            if(w1, w2, w3, w4, w5) not in markov:
                markov[(w1, w2, w3, w4, w5)] = []
            markov[(w1, w2, w3, w4, w5)].append(word)
        w1, w2, w3, w4, w5 = w2, w3, w4, w5, word
        
    count = 0
    sentence = ""
    w1, w2, w3, w4, w5 = random.choice(list(markov.keys()))

    while count < len(wordlist):
        tmp = random.choice(markov[w1, w2, w3, w4, w5])
        #句読点などの区切りがついたら文章作成を終了
        if tmp in endword:
            break
        sentence += tmp
        w1, w2, w3, w4, w5 = w2, w3, w4, w5, tmp
        count += 1

        if count > 140:
            break
    return sentence

print(create_tw(node))