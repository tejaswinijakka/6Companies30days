class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #sort the word and it would be the key of dic
        #and keep appending the relevant ones
        dic = {}
        for i in words:
            k = sorted(i)
            k = ''.join(k)
            if k in dic:
                dic[k].append(i)
            else:
                dic[k] = []
                dic[k].append(i)
        return dic.values()