const fs = require('fs');
const blkfile = require('filesize.js');

const noSort = (a, b) => 0

const compareNumbers = (a, b) => a - b

const compareStrings = (a, b) => a.localeCompare(b)

const compareFileNames = (a, b) => compareStrings(a.name, b.name)

function convertfilesize(bytes,decimalPoint) {
    if(bytes == 0) return '0 Bytes';
    var k = 1000,
        dm = decimalPoint || 2,
        sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
        i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
 }

function compareFileExtensions(a, b) {
    let extA = a.name.includes('.') ? a.name.split('.').pop() : ''
    let extB = b.name.includes('.') ? b.name.split('.').pop() : ''
    return compareStrings(extA, extB)
}
const compareFileSizes = (a, b) => compareNumbers(a.size, b.size)

function usage(){
    const text = fs.readFileSync('help.txt', {encoding: 'utf8'})
    console.log(JSON.stringify(text))
}

var assignedPath = __dirname
var sortOrder = noSort
var metric = false
var thresHoldMin = 0.0
var blocksize = false
let outFileSize 

function parseArgs(args) {
    for (let i=0; i<args.length; i++) {
        switch(args[i]) {
            case '-h':
            case '--help':
                usage()
                process.exit()
            case '-p':
            case '--path':
                assignedPath = args[++i]
                break
            case '-s':
            case '--sort':
                sortType = args[++i]
                if (sortType === 'alpha') {
                    sortOrder = compareFileNames
                }
                else if (sortType === 'exten') {
                    sortOrder = compareFileExtensions
                }
                else if (sortType === 'size') {
                    sortOrder = compareFileSizes
                }
                break
            case '-t':
            case '--threshold':
                thresHoldMin = Number(args[++i])
                break
            case '-m':
            case '--metric':
                metric = true
                break
            case '-b':
            case '--blocksize':
                blocksize = true
                break
            default:
                throw new error("bad flag")

        }
    }
    if (args.length < 0){
        throw new error('no args found');
    }
}

function diskfull(path){
    let dirFiles = fs.readdirSync(path)
    let dirsize = 0
    let files = []
    console.group()
    for (let i = 0; i < dirFiles.length; i++) {
        if (sortOrder == noSort){
            let filestat = fs.statSync(path+"/"+dirFiles[i])
            switch (blocksize) {
                case true:
                    outFileSize = blkfile.default(filestat.size, 2, "si")
                    break
                default:
                    outFileSize = filestat.size
                    break
            }
            switch(filestat.isDirectory()){
                case true:
                    outFileSize = diskfull(path+"/"+dirFiles[i])
                    dirsize += outFileSize
                    print(path, dirFiles[i], outFileSize)
                    break
                default: 
                    print(path, dirFiles[i], outFileSize)
                    dirsize += filestat.size
                    break
            }
        } else {
            let file = new Object()
            let filestat = fs.statSync(path+"/"+dirFiles[i])
            switch (blocksize) {
                case true:
                    let extra = filestat.size%4096
                    outFileSize = filestat.size-extra+4096
                    break
                default:
                    outFileSize = filestat.size
                    break
            }
            switch(filestat.isDirectory()){
                case true:
                    outFileSize = diskfull(path+"/"+dirFiles[i])
                    file.name = path+"/"+dirFiles[i]
                    file.size = outFileSize
                    break
                default: 
                    file.name = path+"/"+dirFiles[i]
                    file.size = outFileSize
                    dirsize += outFileSize
                    break
            }
            files.push(file)
        }
    }
    if (sortOrder == noSort){
        print(path, "", dirsize)
    } else {
        files.sort(sortOrder)
        for (let i = 0; i < files.length; i++) {
            if (outFileSize >= thresHoldMin){
                if (metric){
                    console.log(`${files[i].name} \tsize: ${convertfilesize(files[i].size)}`)
                } else {
                    console.log(`${files[i].name} \tsize: ${files[i].size}`)
                }
            }
        }
    }
    console.groupEnd()
    return dirsize
}

function print(path, dirFiles, outFileSize){
    if (outFileSize >= thresHoldMin){
        if (metric){
            outFileSize = console.log(`${path}/${dirFiles} size: ${convertfilesize(outFileSize)}`)
        } else {
            console.log(`${path}/${dirFiles} size: ${outFileSize}`)
        }
    }
}

function main() {
    const args = process.argv.slice(2)
    parseArgs(args)
    diskfull(assignedPath)
}

main()