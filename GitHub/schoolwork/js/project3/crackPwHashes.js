// const bcrypt = require("1K.hashes.txt")
const bcrypt = require("bcryptjs")
const fsPromises = require("fs/promises")
var pwds10k = require(`./mcupws.json`)
const fs = require("fs")
var letters = "abcdefghijklmnopqrstuvwxyz".split("")
const cluster = require('cluster')
const { Console } = require("console")
const numCPUs = require('os').cpus().length
let arr =[]

var uncracked = []

function check10K(hash) {
    for (let pwd10k of pwds10k) {
        if (bcrypt.compareSync(pwd10k, hash)){
            return pwd10k
        }
    }
    return false
}

function checkempty(hash) {
    if (bcrypt.compareSync("", hash)) {
        return ""
    }
    return false;
}

function checkLetter(hash) {
    for (let letter of letters) {
        if (bcrypt.compareSync(letter, hash)) {
            return letter
        }
    }
    return false
}

function check2Letter(hash){
    for (let letter1 of letters){
        for (let letter2 of letters){
            if (bcrypt.compareSync(letter1+letter2, hash)) {
                return letter1+letter2
            }
        }
    }
    return false
}


function check3Letter(hash) {
    for (let letter1 of letters) {
        for (let letter2 of letters) {
            for (let letter3 of letters) {
                if (bcrypt.compareSync(letter1 + letter2 + letter3, hash)) {
                    return letter1 + letter2 + letter3
                }
            }
        }
    }
    return false
}

function check4Letter(hash) {
    for (let letter1 of letters) {
        for (let letter2 of letters) {
            for (let letter3 of letters) {
                for (let letter4 of letters) {
                    if (bcrypt.compareSync(letter1 + letter2 + letter3 + letter4, hash)) {
                        return letter1 + letter2 + letter3 + letter4
                    }
                }
            }
        }
    }
    return false
}

function store(pwd) {
    fs.appendFileSync("./1K.hashes.cracked.txt", pwd+"\n", (error) => {
        if (error) {
            console.log('An error has occurred ', error)
            return
        }
    })
}

function crackPwd() {
    // setTimeout(function() {
    //     process.exit(0)}, 
    // 600000)
    const text = fs.readFileSync('./1K.hashes (2).txt', 'utf8')
    let hashes = text.split("\r\n")
    if (cluster.isMaster) {
        const splitQty = hashes.length / numCPUs;

        for (let i = 0; i < numCPUs; i++) {
            const worker = cluster.fork()
            let msg = {start: Math.floor(i * splitQty), end: Math.floor(i * splitQty + splitQty )}
            worker.send(msg)
            worker.on('message', () => {
                return
            })
        }
    } else { //worker
        process.on('message', ({start, end }) => {
            for (let i = start; i < end; i++) {
                if ((pwdempty = checkempty(hashes[i]))) {
                    store(pwdempty)
                    continue
                } else if ((pwd1 = checkLetter(hashes[i]))) {
                    store(pwd1)
                    continue
                } else if ((pwd2 = check2Letter(hashes[i]))) {
                    store(pwd2)
                    continue
                } else if ((pwd10k = check10K(hashes[i]))) {
                    store(pwd10k)
                    continue
                }
                uncracked.push(hashes[i])
                continue
            }
            for (let hash of uncracked) {
                if ((pwd3 = check3Letter(hash))) {
                    store(pwd3)
                    continue
                } else if ((pwd4 = check4Letter(hash))) {
                    store(pwd4)
                    continue
                }
            }
            process.exit()
        })
    }
}

crackPwd()

