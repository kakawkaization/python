def countLines(name):
    f = open(name)
    print(len(f.readlines()))
    f.seek(0, 0)
 
def countChars(name):
    f = open(name)
    print(len(f.read()))
    f.seek(0)

def test(name):
   countLines(name)
   countChars(name)

if __name__ == '__main__':
    test(name)
