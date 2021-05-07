import zipfile
import sys

wordlist = "english.txt"
zip_file = "test_zip.zip"

zip_file = zipfile.ZipFile(zip_file)

with open(wordlist, "rb") as wordlist:
    for line in wordlist.readlines():
        try:
            zip_file.extractall(pwd=line.strip())
        except:
            continue        
        else:  
            print("The password is: ",line.decode().strip())
            sys.exit()
print("The password is not on this wordlist.")