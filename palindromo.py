import time
class StackAutomaton:
    def __init__(self):
        self.__states = []
        self.__stack = ["#"]

    def initializeAutomaton(self):
        stateP = State()
        stateP.initializeState({"name":"p", "followingStates":["p","q"]})
        stateP.transitions.initializeTransition(
            {"inputSymbol":{
                "p":["a","b","a","b","a","b"], # transiciones de P a P
                "q":["c","c","c"]},            # transicinoes de P a Q
            "symbolUnstacks":{
                "p":["#","#","a","a","b","b"],
                "q":["a","b","#"]},
            "stackedSymbol":{
                "p":["#a","#b","aa","ab","ba","bb"],
                "q":["a","b","#"]}
            }
        )
        #---------------
        stateQ = State()
        stateQ.initializeState({"name":"q", "followingStates":["q","r"]})
        stateQ.transitions.initializeTransition(
            {"inputSymbol":{
                "q":["a","b"],
                "r":["lambda"]},
            "symbolUnstacks":{
                "q":["a","b"],
                "r":["#"]},
            "stackedSymbol":{
                "q":["lambda","lambda"],
                "r":["#"]}
            }
        )
        #---------------
        stateR = State()
        stateR.initializeState({"name":"r", "followingStates":"end"})
        stateR.transitions.initializeTransition(
            {"inputSymbol":"",
            "symbolUnstacks":"",
            "stackedSymbol":""
            }
        )
        self.__states = [stateP,stateQ,stateR]
        myWord = PalindromeWord()
        self.validateWord(myWord)
    
    def validateWord(self, word):
        numberIterations = 0
        for wordLetter in word.string:
            stateAutomaton = self.searchStatus(word.state) 
            stackSymbol = self.__stack[len(self.__stack)-1]  #obtenemos la cabeza de la pila
            word.state = self.LetterAndSymbolmatch(wordLetter, stackSymbol, stateAutomaton)
            numberIterations += 1
            if numberIterations == (len(word.string)): #saber si estoy en el ultimo caracter de la palabra
                stackSymbol = self.__stack[len(self.__stack)-1]
                word.state = self.LetterAndSymbolmatch("lambda", stackSymbol, stateAutomaton)
            if word.state == False:
                break
        if word.state == "r":
            print("valid word")
            return True
        else:
            print("invalid word")

    def searchStatus(self,nameState):
        for state in self.__states:
            if nameState == state.name:
                return state

    def LetterAndSymbolmatch(self, letter, symbol, state):
        for nameState in state.followingStates:
            iterator = 0
            for nameLetter in state.transitions.inputSymbol[nameState]:
                if  letter == nameLetter and symbol == state.transitions.symbolUnstacks[nameState][iterator]:
                    self.unstack()
                    self.stack(state.transitions.stackedSymbol[nameState][iterator])
                    return nameState
                iterator += 1  
        return False
    
    def unstack(self):
        self.__stack.pop()

    def stack(self, character):
        if character != "lambda":
            for aCharacter in character:
                self.__stack.append(aCharacter)
            
class State:
    def __init__(self):
        self.name = ""
        self.followingStates = []
        self.transitions = Transition()
    
    def initializeState(self, features):
        self.name = features["name"]
        self.followingStates = features["followingStates"]

class Transition:
    def __init__(self):
        self.inputSymbol = {}
        self.symbolUnstacks = {}
        self.stackedSymbol = {}
    
    def initializeTransition(self, features):
        self.inputSymbol = features["inputSymbol"]
        self.symbolUnstacks = features["symbolUnstacks"]
        self.stackedSymbol = features["stackedSymbol"]

class PalindromeWord:
    def __init__(self):
        self.state = "p"
        self.string = "abacaba"

prueba = StackAutomaton()
prueba.initializeAutomaton()
        
