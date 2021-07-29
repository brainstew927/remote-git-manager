import sys
import urllib.request
import urllib.error
import json

if __name__ == "__main__":
    # get the server address
    addr = sys.argv[1]
    # get the project name
    prjName = sys.argv[2]

    url = "http://" +addr + ":8080?projectName=" + prjName
    # print(url)
    # query the server
    try:
        contents = urllib.request.urlopen(url)
    
        if(contents.getcode() != 200):
            print("error while creating project")
        else:
            print("project created succesfully, following are the project information:")
            info = json.loads(contents.read().decode("utf-8"))
            for k in info:
                print(f"\t{k}:\t{info[k]}")
            
    except urllib.error.HTTPError as e:
        print(f"error while requesting project creation: {e.getcode()}")
    
    
