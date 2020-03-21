'''

Here is a question from the "Cracking The Coding Interview" book with a twist.

Implement a method to perform basic string compression using the counts of repeated characters. (p. 73 5th edition)

The twist: the string can also contain digits. Think of encoding and decode protocol. How the compression can be reversed properly?

For example, ab2ccccd -> ab24cd

'''


def compress_str(txt):

    def cmprs(ch, fin_txt, cnt):
        if cnt > 1:
            fin_txt += str(cnt)
        if ch.isdigit():
            fin_txt += '_'
        fin_txt += ch
        cnt = 1
        return fin_txt, cnt


    ind = 0
    fin_txt = ''
    while ind < len(txt):
        if ind ==0:
            prev = txt[ind]
            cnt = 1
        elif txt[ind] == prev:
            cnt+=1
        else:
            fin_txt, cnt = cmprs(prev, fin_txt, cnt)
            prev = txt[ind]
        ind+=1

    fin_txt, cnt = cmprs(prev, fin_txt, cnt)

    return fin_txt


print(compress_str('sdsdsfff3kk'))

