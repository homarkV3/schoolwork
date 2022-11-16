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
    for (let i = 0; i < 700; i++) {
        pwd = rndPwd(pwds)
        kpwds.push(pwd)
    }
    for (let i = 0; i < 200; i++) {
        pwd = ""
        kpwds.push(pwd)
    }
    for (let i = 0; i < 40; i++) {
        pwd = rndLetter()
        kpwds.push(pwd)
    }
    for (let i = 0; i < 30; i++) {
        pwd = rndLetter()+rndLetter()
        kpwds.push(pwd)
    }
    for (let i = 0; i < 20; i++) {
        pwd = rndLetter()+rndLetter()+rndLetter()
        kpwds.push(pwd)
    }
    for (let i = 0; i < 10; i++) {
        pwd = rndLetter()+rndLetter()+rndLetter()+rndLetter()
        kpwds.push(pwd)
    }
    return kpwds
}
async function rnd1kecrypt(){
    hashes =[]
    pwds1k=kPwds()
    for (let i=0; i<pwds1k.length; i++){
        var hash = bcrypt.hashSync(pwds1k[i], 4)
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