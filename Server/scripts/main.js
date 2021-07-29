var http = require('http');
const url = require('url');
const fs = require('fs');
const path = require("path");
const os = require("os");
const ip = require("ip");
const { exec } = require('child_process');

var server = http.createServer(function(req, res) {
    console.log("requested creation of a project");
    let startPath = ".." + path.sep + "projects";
    try{
        console.log("setting current directory inside of projects folder");
        process.chdir(startPath);
    }catch{
        return -1;
    }
    console.log(req.url);
    const queryObject = url.parse(req.url,true).query;
    if(queryObject["projectName"] != null){
        let prg = queryObject["projectName"];
        // creo il progetto
        let _path = prg + ".git";
        console.log("project name: " + prg);
        // se non esiste la cartella creo la cartella con nome del progetto
        if(!fs.existsSync(_path)){
            fs.mkdirSync(_path);
            // dentro questa cartella creo il progetto git con init bare
            try {
                // creo oggetto json da restituire per verifiche
                let verOb = new Object();
                process.chdir(_path);
                exec("git init --bare");
                res.writeHead(200);
                verOb["projectName"] = prg;
                verOb["path"] = process.cwd(); // + path.sep + _path;
                
                let userInfo = os.userInfo();
                
                verOb["git_repo"] = 
                    userInfo.username + "@" + // utente
                    String(ip.address(null, "ipv4")) +// host (indirizzo)
                    ":" +
                    verOb["path"];// path
                
                console.log(verOb["path"]);
                res.write(JSON.stringify(verOb));
                process.chdir("..");
              }
              catch (err) {
                console.log('chdir: ' + err);
                res.writeHead(500);
            }   
        }else{
            // se esiste da come risposta un errore
            res.writeHead(500);
        }
    }else{
        res.writeHead(500);
    }
    res.end("");
});
server.listen(8080);