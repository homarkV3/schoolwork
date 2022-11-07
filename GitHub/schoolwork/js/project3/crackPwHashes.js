// const bcrypt = require("1K.hashes.txt")
const bcrypt = require("bcryptjs")
const fsPromises = require("fs/promises")
var pwds10k = require(`./mcupws.json`)
const fs = require("fs")
var Letter="abcdefghijklmnopqrstuvwxyz".split("")

var crackedPwd =[]
var uncracked = []

async function check10K(pwd){
    let promises = []
    for (let i = 0; i < pwds10k.length; i++){
        promises.push(bcrypt.compare(pwds10k[i], pwd))
        if (promises.length >= 100||i == pwds10k.length-1){
            let results = await Promise.all(promises)
            if ((results.find((element)=>element))){
                return pwds10k[results.indexOf(true)]
            }
            promises.length = 0
        }
    }
    console.timeEnd("10k")
    return false
}

function checkempty(pwd){
    if (bcrypt.compareSync("", pwd)) {
        return ""
    }
    return false;
}

function checkLetter(pwd){
    for (let i = 0; i < Letter.length; i++){
        if (bcrypt.compareSync(Letter[i], pwd)) return Letter[i]
    }
    return false
}

function check2Letter(pwd){
    for (let i = 0; i < Letter.length; i++){
        for (let j = 0; j < Letter.length; j++){
            if (bcrypt.compare(Letter[i]+Letter[j], pwd)) return Letter[i]+Letter[j] 
        }
    }
    return false
}

function check3Letter(pwd){
    for (let i = 0; i < Letter.length; i++){
        for (let j = 0; j < Letter.length; j++){
            for (let k = 0; k < Letter.length; k++){
                if (bcrypt.compareSync(Letter[i]+Letter[j]+Letter[k], pwd)) return Letter[i]+Letter[j]+Letter[k] 
            }
        }
    }
    return false
}

function check4Letter(pwd){
    for (let i = 0; i < Letter.length; i++){
        for (let j = 0; j < Letter.length; j++){
            for (let k = 0; k < Letter.length; k++){
                for (let l = 0; l < Letter.length; l++){
                    if (bcrypt.compareSync(Letter[i]+Letter[j]+Letter[k]+Letter[l], pwd)) return Letter[i]+Letter[j]+Letter[k]+Letter[l]
                }
            }
        }
    }
    return false
}

async function timer() {
    console.time("")
    await sleep(3600000)
} 

function sleep(ms) {
    return new Promise((store) => {
        setTimeout(store(), ms)
    })
}

async function store(){
    fs.appendFile("./1K.hashes.cracked.txt", crackedPwd.join('\n') , (error) => {
        if (error) {
            console.log('An error has occurred ', error)
            return
        } else {
            process.exit()
        }
    })
}

async function crackPwd(){
    timer()
    const text = await fsPromises.readFile('./1K.hashes.txt', 'utf8')
    pwds = text.split("\n")
    for (let i = 0; i < pwds.length;i++){
        let pwd
        if ((pwd = checkempty(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        } else if ((pwd = checkLetter(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        } else if ((pwd = check2Letter(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        } else if ((pwd = await check10K(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        } else if ((pwd = check3Letter(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        } else if ((pwd = check4Letter(pwds[i]))) {
            crackedPwd.push(pwd)
            continue
        }
    }
    store()
}

crackPwd()

