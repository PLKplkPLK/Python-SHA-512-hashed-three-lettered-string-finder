import hashlib
import string

hashed_string=input("Insert hash: ")

flag=0
for a in string.ascii_letters:
    for b in string.ascii_letters:
        for c in string.ascii_letters:
            if hashlib.sha512(str(a+b+c).encode("utf-8")).hexdigest()==hashed_string:
                print("Found string:",a+b+c)
                flag=1
                break

if flag==0:
    print("Inserted hash was not created using three lettered string or wasn't hashed using SHA-512 algorithm.")
