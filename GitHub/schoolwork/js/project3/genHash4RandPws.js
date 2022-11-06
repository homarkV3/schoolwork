const bcrypt = require("bcryptjs")
var pwds = require(`./mcupws.json`)
const fs = require('fs')

function rndPwd(passwords){
    const random = Math.floor(Math.random() * passwords.length);
    return passwords[random]
}

function rndLetter(){
    Letter="abcdefghijklmnopqrstuvwxyz"
    return rndPwd(Letter.split(""))
}
function kPwds(){
    kpwds = []
    for (var index = 0; index < 700; index++) {
        var pwd = rndPwd(pwds)
        kpwds.push(pwd[1])
    }
    for (var index = 0; index < 200; index++) {
        pwd = ""
        kpwds.push(pwd)
    }
    for (var index = 0; index < 40; index++) {
        pwd = rndLetter()
        kpwds.push(pwd)
    }
    for (var index = 0; index < 30; index++) {
        pwd = rndLetter()+rndLetter()
        kpwds.push(pwd)
    }
    for (var index = 0; index < 20; index++) {
        pwd = rndLetter()+rndLetter()+rndLetter()
        kpwds.push(pwd)
    }
    for (var index = 0; index < 10; index++) {
        pwd = rndLetter()+rndLetter()+rndLetter()+rndLetter()
        kpwds.push(pwd)
    }
    return kpwds
}
async function rnd1kecrypt(){
    hashes =[]
    pwds1k=kPwds()
    for (i=0; i<pwds1k.length; i++){
        var hash = bcrypt.hashSync(pwds1k[i], 8)
        await fs.appendFile("./1K.hashes.txt", hash+"\n", (error) => {
            if (error) {
                console.log('An error has occurred ', error)
                return
        }})
    }
}

rnd1kecrypt()

// function remove(arr, value) { 
//     return arr.filter(function(ele){ 
//         return ele != value; 
//     });
// }