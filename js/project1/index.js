// import chalk from 'chalk'
// import fs from 'fs'
// import filesize from 'filesize'
// import fsPromises from 'fs/promises'
// import glob from 'glob'
//v2

// utility base comparators
const fs = require("fs")
const filesize = require("filesize")
const fsPromises = require("fs/promises")
const glob = require("glob")
const chalk = require("chalk")

const noSort = (a, b) => 0
const compareNumbers = (a, b) => a - b
const compareStrings = (a, b) => a.localecompare(b)

const compareFileNames = (a, b) => compareStrings(a.name, b.name)
const compareFileSizes = (a, b) => -compareNumbers(a.size, b.size)
function compareFileExtensions(a, b) {
  let extA = a.name.includes('.') ? a.name.split('.').pop() : ''
  let extB = b.name.includes('.') ? b.name.split('.').pop() : ''
  return compareStrings(extA, extB)
}

let blockSize = false
let threshold = 0
let metric = false
let path = '.'
let sortOrder = noSort
let lang = "en"
let loc = "US"
let configFile = "config.json"
let filter = ""
const defConfigs = {"blockSize": "false", 
                    "threshold": 0,
                    "metric": false,
                    "path": '.',
                    "sortOrder": "noSort",
                    "lang": "en",
                    "loc": "US",
                    "configFile": "config.json",
                    "filter": ""}

let errMessages = {}

async function usage() {
  const text = await fsPromises.readFile(`help.${lang}-${loc}.txt`, 'utf8')
  console.log(chalk.yellow(text))
  process.exit()
}

async function setconfig() {
  const fileConfigs = await fsPromises.readFile(configFile, 'utf8')
  for(var fileConfig in fileConfigs){
    if (defConfigs[fileConfig]) {}
  } 
}

async function setLang(){
  const args = process.argv.slice(2)
  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '-lang':
      case '--language':
        lang = args[++i]
        break
      case '-loc':
      case '--locale':
        loc = args[++i]
        break          
    }
  }
  errMessageFile = `messages.${lang}-${loc}.json`
  errMessages = await fsPromises.readFile(errMessageFile, 'utf8')
}

function setFlags() {
  const args = process.argv.slice(2)
  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '-c':
      case '--config':
        configFile = args[++i]
        break
      case '-f':
      case '--filter':
        filter = args[++i]
        break     
      case '-h':
      case '--help':
        usage()
        break
      case '-t':
      case '--threshold':
        threshold = Number(args[++i]) * 1_000_000_000
        break
      case '-p':
      case '--path':
        path = args[++i]
        break
      case '-m':
      case '--metric':
        metric = true
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
      default: console.log(chalk.red(errMessages[flagErr]))
    }
  }
}

async function readTree(dirPath) {
  dirPath += '/'
  const dir = {
    name: dirPath,
    size: 0,
    children: []
  }
  const names = await fsPromises.readdir(dirPath)
  for (let name of names) {
    const childName = `${dirPath}${name}`
    const stats = fs.statSync(childName)
    if (stats.isFile()) {
      const file = {
        name: childName,
        size: blockSize ? getBlockSize(stats.size) : stats.size
      }
      dir.size += file.size
      dir.children.push(file)
    }
    else if (stats.isDirectory()) {
      const subDir = await readTree(childName)
      dir.size += subDir.size
      dir.children.push(subDir)
    }
  }
  dir.children.sort(sortOrder)
  return dir
}

function displayTree(dirEntry) {
  if (dirEntry.size < threshold) return

  if (metric) {
    console.log(chalk.magenta(dirEntry.name), chalk.gray(filesize(dirEntry.size)))
  }
  else console.log(chalk.magenta(dirEntry.name), chalk.gray(dirEntry.size.toLocaleString('en-US'), `bytes`))

  if (!dirEntry.children) return
  console.group()
  for (let child of dirEntry.children) {
    displayTree(child)
  }
  console.groupEnd()
}

async function main() {
  await setLang()
  await setconfig()
  setFlags()
  let tree = await readTree(path)
  displayTree(tree)
}
main()