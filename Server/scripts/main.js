var http = require('http');
const url = require('url');
const fs = require('fs');
const path = require("path");
const { exec } = require('child_process');

var server = http.createServer(function(req, res) {
        res.end("");    
    const queryObject = url.parse(req.url,true).query;
    if(queryObject["projectName"] != null){
        let prg = queryObject["projectName"];
        // creo il progetto
        console.log(prg)
        // se non esiste la cartella creo la cartella con nome del progetto
        if(!fs.existsSync(".." + path.sep + "projects"  +path.sep + prg + ".git")){
            fs.mkdirSync(".." + path.sep + "projects"  +path.sep + prg + ".git");
            // dentro questa cartella creo il progetto git con init bare
            try {
                process.chdir(".." + path.sep + "projects"  +path.sep + prg + ".git");
                exec("git init --bare");
                res.writeHead(200)
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
});
server.listen(8080);