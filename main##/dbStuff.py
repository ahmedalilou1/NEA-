import sqlite3
import traceback

class Database:
    def __init__(self, dbName):
        self.dbName = dbName
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()

        #create tables
        self.c.execute("CREATE TABLE IF NOT EXISTS words(wordId integer PRIMARY KEY, word text, meaning text, phonetics text)")
        self.c.execute("CREATE TABLE IF NOT EXISTS players(playerId integer PRIMARY KEY, username text UNIQUE, name text)")
        self.c.execute("CREATE TABLE IF NOT EXISTS scores(scoresId integer PRIMARY KEY, playerId integer, score integer)")
        self.c.execute("CREATE TABLE IF NOT EXISTS playerWords(playerWordsId integer PRIMARY KEY, playerId integer, wordId integer, correct boolean)")

        self.conn.commit()

    def listAllTables(self):
        print("Words")
        self.c.execute("SELECT * FROM words")
        data = self.c.fetchall()    
        for item in data:
            print(item)

        print("scores")
        self.c.execute("SELECT * FROM scores")
        data = self.c.fetchall()    
        for item in data:
            print(item)

        print("players")
        self.c.execute("SELECT * FROM players")
        data = self.c.fetchall()    
        for item in data:
            print(item)

        print("PlayerWords")
        self.c.execute("SELECT * FROM playerWords")
        data = self.c.fetchall()    
        for item in data:
            print(item)

    def close(self):
        self.conn.close()

    def execute(self, sql, params=None):
        try:
            if params:
                self.c.execute(sql, params)
            else:
                self.c.execute(sql)
            self.conn.commit()
        except:
            print(traceback.format_exc())

    def addPatientToDB(self, word, meaning, phonetics):
        #add patient to database
        self.c.execute("INSERT INTO words (word, meaning, phonetics) VALUES (?, ?, ?)", (word, meaning, phonetics))

    def getWordsFromDB(self, wordList, debug=False):
        self.c.execute("SELECT * FROM words")
        data = self.c.fetchall()    
        for item in data:
            wordId = item[0]
            word = item[1]
            meaning = item[2]
            phonetic = item[3]
            wordList.addWord(word, meaning, phonetic, wordId)
        return wordList

    def getWordsAndScoresFromDB(self):
        words = []
        self.c.execute("SELECT * FROM words LEFT JOIN playerWords ON words.wordId = playerWords.wordId")
        data = self.c.fetchall()    
        for item in data:
            newWord = []
            newWord.append(item[0])
            newWord.append(item[1])
            newWord.append(item[2]) 
            newWord.append(item[3]) 
            newWord.append(item[4]) 
            newWord.append(item[5])  
            newWord.append(item[6]) 
            newWord.append(item[7]) 
            words.append(newWord)
        return words

    def addPlayerToDB(self, username, password, name):
        try:
            self.execute("INSERT INTO players (username, password, name) VALUES (?, ?, ?)", (username, password, name))
            return True
        except:
            return False

    def addClientToDB(self, username, password, name):
        try:
            self.execute("INSERT INTO players (username, password, name) VALUES (?, ?, ?)", (username, password, name))
            return True
        except:
            return False

    def showCurrentUsernames(self):
        self.execute("SELECT username, name, score, password FROM players LEFT JOIN scores ON players.playerId = scores.playerId ORDER BY score DESC")
        print("Current usernames (plus highest score):")
        data = self.c.fetchall()
        for item in data:
            print(item[0], " (score: " + str(item[2]) + ")" + item[3])
        print("---------------")

    def markWordAsGuessed(self, playerId, wordId):
        self.execute("INSERT INTO playerWords (playerId, wordId, correct) VALUES (?, ?, ?) ",  (playerId, wordId, True))

    def deleteClient(self, username):
        try:
            self.execute("DELETE FROM players WHERE username = ?", (username,))
            return True
        except:
            return False
        print("Client deleted")

    def markWordAsUnguessed(self, playerId, wordId):
        self.execute("INSERT INTO playerWords (playerId, wordId, correct) VALUES (?, ?, ?) ",  (playerId, wordId, False))

    def getAllClients(self):
        try:
            self.c.execute("SELECT playerId, username, name FROM players")
            return self.c.fetchall()
        except:
            print("Error fetching clients")
            return []

    def addClient(self, username, name):
        try:
            self.execute("INSERT INTO players (username, name) VALUES (?, ?)", 
                        (username, name))
            return True
        except:
            return False

    def displayClients(self):
        clients = self.getAllClients()
        if not clients:
            print("\nNo clients found.")
            return
        
        print("\nCurrent Clients:")
        print("-" * 35)
        print(f"{'ID':<5} {'Username':<15} {'Name':<20}")
        print("-" * 35)
        for client in clients:
            print(f"{client[0]:<5} {client[1]:<15} {client[2]:<20}")
        print("-" * 35)
