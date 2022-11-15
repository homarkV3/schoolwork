// const bcrypt = require("1K.hashes.txt")
const bcrypt = require("bcryptjs")
const fsPromises = require("fs/promises")
var pwds10k = require(`./mcupws.json`)
const fs = require("fs")
var Letter = "abcdefghijklmnopqrstuvwxyz".split("")
const cluster = require('cluster')
const numCPUs = require('os').cpus().length
let arr =[]

var uncracked = []

function check10K(pwd) {
    for (let i = 0; i < pwds10k.length; i++) {
        if (bcrypt.compare(pwds10k[i], pwd)){
            return pwds10k[i]
        }
    }
    return false
}

function checkempty(pwd) {
    if (bcrypt.compareSync("", pwd)) {
        return ""
    }
    return false;
}

function checkLetter(pwd) {
    for (let i = 0; i < Letter.length; i++) {
        if (bcrypt.compareSync(Letter[i], pwd)) {
            return Letter[i]
        }
    }
    return false
}

function check2Letter(pwd){
    for (let i = 0; i < Letter.length; i++){
        for (let j = 0; j < Letter.length; j++){
            if (bcrypt.compareSync(Letter[i]+Letter[j], pwd)) {
                return Letter[i]+Letter[j] 
            }
        }
    }
    return false
}


function check3Letter(pwd) {
    for (let i = 0; i < Letter.length; i++) {
        for (let j = 0; j < Letter.length; j++) {
            for (let k = 0; k < Letter.length; k++) {
                if (bcrypt.compareSync(Letter[i] + Letter[j] + Letter[k], pwd)) {
                    return Letter[i] + Letter[j] + Letter[k]
                }
            }
        }
    }
    return false
}

function check4Letter(pwd) {
    for (let i = 0; i < Letter.length; i++) {
        for (let j = 0; j < Letter.length; j++) {
            for (let k = 0; k < Letter.length; k++) {
                for (let l = 0; l < Letter.length; l++) {
                    if (bcrypt.compareSync(Letter[i] + Letter[j] + Letter[k] + Letter[l], pwd)) {
                        return Letter[i] + Letter[j] + Letter[k] + Letter[l]
                    }
                }
            }
        }
    }
    return false
}

async function store(message) {
    fs.appendFile("./1K.hashes.cracked.txt", message+"\n", (error) => {
        if (error) {
            console.log('An error has occurred ', error)
            return
        }
    })
}

async function crackPwd() {
    setTimeout(function() {
        process.exit(0)}, 
    600000)
    const text = await fsPromises.readFile('./1K.hashes.txt', 'utf8')
    pwds = text.split("\n")
    if (cluster.isMaster) {
        const splitQty = pwds.length / numCPUs;

        for (let i = 0; i < numCPUs; i++) {
            const worker = cluster.fork()
            let msg = {start: Math.floor(i * splitQty), end: Math.floor(i * splitQty + splitQty )}
            worker.send(msg)
            worker.on('message', text => {
                return
            })
        }
    } else { //worker
        process.on('message', ({start, end }) => {
            for (let i = start; i < end; i++) {
                let pwd
                if ((pwd = checkempty(pwds[i]))) {
                    store(pwd)
                    continue
                } else if ((pwd = checkLetter(pwds[i]))) {
                    store(pwd)
                    continue
                } else if ((pwd = check2Letter(pwds[i]))) {
                    store(pwd)
                    continue
                } else if ((pwd = check10K(pwds[i]))) {
                    store(pwd)
                    continue
                }
                uncracked.push(pwds[i])
                continue
            }
            for (let i = 0; i < uncracked.length; i++) {
                if ((pwd = check3Letter(pwds[i]))) {
                    crackedPwd.push(pwd)
                    continue
                } else if ((pwd = check4Letter(pwds[i]))) {
                    crackedPwd.push(pwd)
                    continue
                }
            }
            process.exit()
        })
    }
}

crackPwd()

