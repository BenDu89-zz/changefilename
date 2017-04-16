import os

def renamefile(liste):
    # Step 1: get all the files into a list
    liste = os.listdir(liste)
    os.chdir("/Users/benjamindunisch/Downloads/prank/") #change dir
    #Step 2: rename
    for i in liste:
        os.rename(i, i.translate(None,"0123456789"))
    return liste
print renamefile("/Users/benjamindunisch/Downloads/prank/")
