import sys
import urllib.request
import urllib.error
import pickle
import json
from prettytable import PrettyTable
import prettytable


# later the command the user was trying to use will be passed as an argument
def print_help():
    print("help! (todo: change)")

if __name__ == "__main__":
    try:
        with open("data/servers", "rb") as f:
            server_dict = pickle.load(f)
    except:
        server_dict = dict()
    # check that at least 1 argument is passed otherwise print the help message
    if len(sys.argv) < 2:
        print_help()
        exit()
    # if asked to add a server to later use a logical name to reference it
    if sys.argv[1] == "add-server":
        try:
            server_name = sys.argv[2]
            server_addr = sys.argv[3]
            # add to the dictionary read from the file using pickle
            server_dict[server_name] = server_addr
        except:
            print_help()
    if sys.argv[1] == "list-servers":
        try:
            print("registered servers:")
            p = PrettyTable(["name", "address"])
            for k in server_dict:
                p.add_row([k, server_dict[k]])
            print(p)
        except:
            print_help()
    if sys.argv[1] == "create":
        addr = ""
        prjName = ""
        # if asked to create a project
        # get the server address
        if sys.argv[2] == "-r":
            # user registered server name (server name shall be passed as third argument)
            addr = server_dict[sys.argv[3]]  
            # get the project name
            prjName = sys.argv[4]
        else:
            addr = sys.argv[2]
            prjName = sys.argv[3]

        url = "http://" +addr + ":8080?projectName=" + prjName
        # query the server
        try:
            contents = urllib.request.urlopen(url)
        
            if(contents.getcode() != 200):
                print("error while creating project")
            else:
                print("project created succesfully, following are the project information:")
                info = json.loads(contents.read().decode("utf-8"))
                p = PrettyTable(["name", "value"])
                for k in info:
                    p.add_row([k, info[k]])
                print(p)
        except urllib.error.HTTPError as e:
            print(f"error while requesting project creation: {e.getcode()}")
    with open("data/servers", "wb") as f:
        pickle.dump(server_dict, f)
    
