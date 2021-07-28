import sys
import urllib.request

if __name__ == "__main__":
    # get the server address
    addr = sys.argv[1]
    # get the project name
    prjName = sys.argv[2]

    url = "http://" +addr + ":8080?projectName=" + prjName
    print(url)
    # query the server
    contents = urllib.request.urlopen(url)
    print(contents.getcode())
    
    if(contents.getcode() != 200):
        print("error while creating project")
    else:
        print("project created succesfully")
