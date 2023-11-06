#IMPORTANT - change file path on lines 32, 52, and 84 to the file path of the .txt file you wish to use for your passwords

def ceasercipherencrypter(message):
    encryptedPass = ''
    for item in message:
        for ch in item:
            if 'A' <= ch <= 'Z':
                encryption = chr(((ord(ch) - ord('A') + 5) % 26) + ord('A'))
                encryptedPass += encryption

            elif 'a' <= ch <= 'z':
                encryption = chr(((ord(ch) - ord('a') + 5) % 26) + ord('a'))
                encryptedPass += encryption
    return encryptedPass
def ceasercipherdecrypter(message):
    decryptedPass = ''
    for item in message:
        for ch in item:
            if 'A' <= ch <= 'Z':
                decryption = chr(((ord(ch) - ord('A') - 5) % 26) + ord('A'))
                decryptedPass += decryption

            elif 'a' <= ch <= 'z':
                decryption = chr(((ord(ch) - ord('a') - 5) % 26) + ord('a'))
                decryptedPass += decryption
    return decryptedPass

while True:
    passViewer = {

    }
    with open(r"C:\Users\jeezu\OneDrive\Desktop\\passManager2.txt", 'r') as passManager:
        lines = passManager.readlines()
        for line in lines:
            lineSplit = line.split(":")
            fixedLineSplit = lineSplit[1].split("\n")
            if len(fixedLineSplit) > 1:
                fixedLineSplit.remove(fixedLineSplit[1])

            else:
                pass
            passViewer[lineSplit[0]] = fixedLineSplit
    for key in passViewer:
        value = passViewer.get(key)
        decryptedPass = ceasercipherdecrypter(value)
        passViewer[key] = decryptedPass

    choice1 = input('REMOVE/ADD/VIEW Passwords?:')
    if choice1 == 'REMOVE' or choice1 == 'remove':
        choice2 = input("ALL/SPECIFIC:")
        if choice2 == 'ALL' or choice2 == 'all':
            with open(r"C:\Users\jeezu\OneDrive\Desktop\\passManager2.txt", 'w') as passManager:
                pass
            print("All passwords removed. Thank you for using Bio's PassManager! :3")
            passViewer = {}
        if choice2 =='SPECIFIC' or choice2 =='specific':
            choice3 = input("What site would you like to remove?:")
            passwords = passViewer.copy()
            for key in passwords:
                if choice3 == key:
                    choice4 = input('Removing ' + key + ' profile. Is that okay? (Y/N):')
                    if choice4 == 'Y' or choice4 == "y":
                        del passViewer[key]

    elif choice1 == 'ADD' or choice1 == 'add':
        def add():
            site = input("WEBSITE:")
            passW = input("PASSWORD:")
            if site not in passViewer:
                passViewer[site] = [passW]
            else:
                print("Sorry, this website is already registered. Please try another.")
                add()
        add()
    #allows you to view all passwords. decrypted
    elif choice1 == 'VIEW' or choice1 == 'view':
        authorization = input('Please enter authorization code to view passwords: ')
        if authorization == 'nogreaterlovehathmanthenthisthentolaydownhislifeforhisfriends':
            for i in passViewer:
                value = passViewer.get(i)
                print(i + ": " + value)

    #adding all new changes, and encrypts all passwords so if the .txt file is opened enemy will get nonsense
    with open(r"C:\Users\jeezu\OneDrive\Desktop\\passManager2.txt", 'w') as passManager:
        for key in passViewer:
            value = passViewer.get(key)
            encryptedPass = ceasercipherencrypter(value)
            newPass = (key + ":" + encryptedPass + '\n')
            passManager.write(newPass)

    #decides if you want to continue managing your passwords or not
    choice0 = input("Close PassManager? (Y/N): ")
    if choice0 == 'Y' or choice0 == 'y':
        break