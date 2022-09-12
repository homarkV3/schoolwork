// spike for parsing command line params

const fs = require('fs')

function readTree(path) { // path is always a directory
    console.log(path + '/')

    const dirEntries = fs.readdirSync(path)
    console.group()
    for (let dirEntry of dirEntries) { // works for one level down from the current directory
        console.log(dirEntry.name, dirEntry.isFile(), dirEntry.isDirectory()) // spike to see if isFile() and isDirectory() work
        // use fs.statSync(path) to get the size for files
        // a dir size is the sum of all the children sizes
        // TODO make this work for a whole subtree
    }
    console.groupEnd()
    // return
}

function displayTree(tree) {
    console.log('printTree() not implemented')
}

const noSort = (a, b) => 0

const compareNumbers = (a, b) => a - b

const compareStrings = (a, b) => a.localeCompare(b)

const compareFileNames = (a, b) => compareStrings(a.name, b.name)

function compareFileExtensions(a, b) {
    let extA = a.name.includes('.') ? a.name.split('.').pop() : ''
    let extB = b.name.includes('.') ? b.name.split('.').pop() : ''
    return compareStrings(extA, extB)
}

const compareFileSizes = (a, b) => compareNumbers(a.size, b.size)

let sortOrder = noSort
let threshold = 0

function usage() {
    //print the help doc
    console.log('usage')
}

function parseArgs(args) {
    for (let i=0; i<args.length; i++) {
        switch(args[i]) {
            case '-h':
            case '--help':
                usage()
                process.exit()
            case '-t':
            case '--threshold':
                threshold = Number(args[++i])
                break
            case '-s':
            case '--sort':
                let sortType = args[++i]
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
            default: console.log('bad input')
        }
    }
}
  
function compareFileExtensions(a, b) {
    let extA = a.name.includes('.') ? a.name.split('.').pop() : ''
    let extB = b.name.includes('.') ? b.name.split('.').pop() : ''
    return compareStrings(extA, extB)
}

// console.log(files.sort(compareFileExtensions))
console.log(nums.sort(compareFileNames))
console.log(strs.sort(compareFileSizes))
  
  //'baz.txt'
    // console.log(extA) //, extA[extA.length-1]) //[ 'bar', 'exe' ]
    // let extB = b.name.slice(b.name.indexOf('.')+1)
    // console.log('b', extB)
  
    // extA = a.name.substr(a.name.lastIndexOf('.')+1)
    // console.log('substr', extA)
    
    //compare those strings

// function main() {
//     const args = process.argv.slice(2)
//     parseArgs(args)
//     console.log(threshold, typeof(threshold))
// }

function main() {
    setFlags()
    let tree = readTree('.')
    displayTree(tree)
}

main()