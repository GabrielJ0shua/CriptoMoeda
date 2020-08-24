import hashlib
import time
import binascii

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

class Blockchain:
    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)
        self.DIFFICULTY_ADJUSTMENT = 10
        self.BLOCK_INTERVAL = 120

    def getLatestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    def generationNextBlock(self, data):
        previousBlock = self.getLatestBlock()
        nextIndex = previousBlock.index + 1
        nextTimestamp = int(round(time.time() * 1000))
        nextPreviousHash = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTimestamp, data, calculateHash(nextIndex, nextPreviousHash, nextTimestamp, data))

        if validatingBlock(newBlock) == True:
            self.__chain.append(newBlock)

    def validatingBlock(self, newBlock):
        previousBlock = self.getLatestBlock()
        if previousBlock.index +1 != newBlock.index:
            return False
        elif previousBlock.index +1 != newBlock.previousHash:
            return False
        return True

    def hasMatchesDifficulty(self, hash, difficulty):
        hashBinary = binascii.unhexlify(hash)
        requiredPrefix = '0'*int(difficulty)
        return hashBinary.startswith(requiredPrefix)

    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = self.calculateHash(index, previousHash, timestamp, data, difficulty)
            if self.hasMatchesDifficulty(hash, difficulty):
                block = Block(index, previousHash, timestamp, data, difficulty, nonce)
                return block
            nonce = nonce + 1

    def getdifficulty(self):
        latestBlock = self.getLatestBlock()
        if latestBlock.index % self.DIFFICULTY_ADJUSTMENT == 0 and latestBlock.index != 0:
            return self.getAdjustedDifficulty()
        else:
            return latestBlock.difficulty
    
    def getAdjustedDifficulty(self):
        prevAjustmentBlock = self.blockchain(len(self.blockchain) - self.DIFFICULTY_ADJUSTMENT)
        timeExpected = self.BLOCK_INTERVAL * self.DIFFICULTY_ADJUSTMENT
        timeTaken = latestBlock.timestamp - prevAjustmentBlock.timestamp
        if timeTaken < timeExpected * 2:
            return prevAdjustmenteBlock.difficulty + 1
        elif timeTaken > timeExpected * 2:
            return prevAjustmentBlock.difficulty -1
        else: 
            return prevAjustmentBlock.difficulty

def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).encode('utf-8').hexdigest()

ts = int(round(time.time() * 1000))
genesisBlock = Block(0, "", ts, "Genesis block", calculateHash(0, "", ts, "Genesis block"))