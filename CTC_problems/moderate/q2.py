# Find the word count givven repetitive queries

def word_count(doc):
    cnt = dict()
    for i in doc.split():
        if i in cnt:
            cnt[i] +=1
        else:
            cnt[i] = 1

    return cnt



doc= 'I am the the person'
cnt = word_count(doc)

print(cnt['the'])