// const bcrypt = require("1K.hashes.txt")
const bcrypt = require("bcryptjs")
const fsPromises = require("fs/promises")
var pwds = require(`./mcupws.json`)
var Letter="abcdefghijklmnopqrstuvwxyz".split("")

function check10K(pwd){
    for (i = 0; i < pwds.length; i++){
        if (bcrypt.compareSync(pwds[i], pwd)) return pwds[i]
    }
    
    return false
}

function checkempty(pwd){
    if (bcrypt.compareSync("", pwd)) {
        return ""
    }
    return false;
}

function checkLetter(pwd){
    for (i = 0; i < Letter.length; i++){
        if (bcrypt.compareSync(Letter[i], pwd)) return Letter[i] 
    }
    return false
}

function check2Letter(pwd){
    for (i = 0; i < Letter.length; i++){
        for (j = 0; j < Letter.length; j++){
            if (bcrypt.compareSync(Letter[i]+Letter[j], pwd)) return Letter[i]+Letter[j] 
        }
    }
    return false
}

function check3Letter(pwd){
    for (i = 0; i < Letter.length; i++){
        for (j = 0; j < Letter.length; j++){
            for (k = 0; k < Letter.length; k++){
                if (bcrypt.compareSync(Letter[i]+Letter[j]+Letter[k], pwd)) return Letter[i]+Letter[j]+Letter[k] 
            }
        }
    }
    return false
}

function check4Letter(pwd){
    for (i = 0; i < Letter.length; i++){
        for (j = 0; j < Letter.length; j++){
            for (k = 0; k < Letter.length; k++){
                for (l = 0; l < Letter.length; l++){
                    if (bcrypt.compareSync(Letter[i]+Letter[j]+Letter[k]+Letter[l], pwd)) return Letter[i]+Letter[j]+Letter[k]+Letter[l]
                }
            }
        }
    }
    return false
}

async function init() {
    console.log(1);
    await sleep(1000);
    console.log(2);
  }
  
  function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }

async function crackPwd(){
    crackedPwd =[]
    const text = await fsPromises.readFile('./bank.hashes.txt', 'utf8')
    pwds = text.split("\n")
    let timerID = setTimeout(myFunction, 1000, "Educative");
    for (i = 0; i < pwds.length;i++){
        if ((pwd = checkempty(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        }
        if ((pwd = checkLetter(pwds[i]))) {
                crackedPwd.push(pwd)
                continue
        }
        if ((pwd = check2Letter(pwds[i]))) {
                crackedPwd.push(pwd)
                continue
        }
        if ((pwd = check3Letter(pwds[i]))) {
                crackedPwd.push(pwd)
                continue
        }
        if ((pwd = check4Letter(pwds[i]))) {
                crackedPwd.push(pwd)
                continue
        }
        if ((pwd = check4Letter(pwds[i]))) {
                crackedPwd.push(pwd)
                continue
        }
        if ((pwd = check10K(pwds[i]))) {
                crackedPwd.push(pwd)
                continue
        }
    }
    fs.appendFile("./1K.hashes.cracked.txt", crackedPwd, (error) => {
        if (error) {
            console.log('An error has occurred ', error)
            return
        } else {
            process.exit()
        }
    })
}

crackPwd()

