columnNumber = 27
n = columnNumber-1
r = ""
while n > 25:
    r = chr(65+n%26)+r
    n = n//26-1
r = chr(65+n)+r
print(r)

        