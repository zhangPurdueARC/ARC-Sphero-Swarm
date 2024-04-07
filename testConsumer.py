import time

if __name__ == "__main__":
    fileNum = 0
    while True:
        fileName = "algorithm/hello"+str(fileNum)+".txt"
        try:
            file = open(fileName, "r")
            commands = file.read()
            print(commands)
            file.close()
            fileNum += 1
        except FileNotFoundError:
            print("Looking for: " + fileName)
        time.sleep(1)