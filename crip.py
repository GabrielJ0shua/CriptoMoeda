import hashlib
import time

class Block:
    def __init__(self, index, previosHash, timestamp, data, hash):
        self.index = index
        self.previosHash = previosHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)

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
        elif previousBlock.index +1 != newBlock.previosHash:
            return False
        return True

def calculateHash(index, previosHash, timestamp, data):
    return hashlib.sha256(str(index) + previosHash + str(timestamp) + data).hexdigest()

ts = int(round(time.time() * 1000))
genesisBlock = Block(0, "", ts, "Genesis block", calculateHash(0, "", ts, "Genesis block"))