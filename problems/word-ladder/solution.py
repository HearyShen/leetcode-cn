import argparse
import time
from typing import List
from collections import defaultdict

parser = argparse.ArgumentParser(__name__)
parser.add_argument("-p", "--print-freq", default=1000)
args = parser.parse_args()

class Solution:
    def __init__(self):
        self.abs2words = defaultdict(set)   # {key: wordAbstractForm, value: words}
        self.reachedWords = set()          # reached words shouldn't be searched again

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if len(endWord) != len(beginWord) or not (endWord in words):
            return 0

        # build absword-to-nextwords dict
        self.buildAbsDict(words)

        bfsCount = 0
        bfsQueue = []
        bfsQueue.append([beginWord, 1])
        self.reachedWords.add(beginWord)
        while len(bfsQueue) > 0:
            curWord = bfsQueue[0][0]
            curLen = bfsQueue[0][1]
            if bfsCount % args.print_freq == 0:
                print(f"BFS count: {bfsCount}, Now: {curWord} {curLen}.")
            if curWord == endWord:
                print(f"BFS search count: {bfsCount}.")
                return curLen

            nextStepWords = self.findNextWords(curWord) - self.reachedWords
            for nextWord in nextStepWords:
                bfsQueue.append([nextWord, curLen+1])

            self.reachedWords = self.reachedWords.union(nextStepWords)

            # basic BFS operations
            bfsQueue.remove(bfsQueue[0])
            bfsCount += 1
        return 0

    def buildAbsDict(self, words: set):
        """Build absword-to-words dict"""
        for word in words:
            for i in range(len(word)):
                absWord = word[:i] + '*' + word[i+1:]
                self.abs2words[absWord].add(word)

    def findNextWords(self, beginWord: str) -> set:
        """Returns the words valid for next step."""
        absWords = [beginWord[:i]+'*'+beginWord[i+1:] for i in range(len(beginWord))]

        nextWords = set()
        for absWord in absWords:
            nextWords = nextWords.union(self.abs2words[absWord])
        return nextWords


if __name__ == "__main__":
    # normal testcase
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    # # large wordList testcase
    # beginWord = "cet"
    # endWord = "ism"
    # wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]

    tic = time.time()
    ret = Solution().ladderLength(beginWord, endWord, wordList)
    toc = time.time()
    
    print(f"Found: {ret} in {toc-tic:.3f}s.")