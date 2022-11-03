var puppeteer = require("puppeteer")
const fs = require('fs');

(async () => {
    const total_page = 100
    passArr = []
    for (var i = 1; i <= total_page; i++) {
        var url = `https://www.passwordrandom.com/most-popular-passwords/page/${i}`
        const browser = await puppeteer.launch()
        try {
            const page = await browser.newPage()
            await page.goto(url)
            console.log(url)
            const rawData = await page.evaluate(() => {
                let data = []
                let table = document.getElementById('cntContent_lstMain')
                for (var i = 1; i < table.rows.length; i++) {
                    let objCells = table.rows.item(i).cells
                    data.push(objCells.item(1).innerHTML.toLowerCase())
                }
                return data.filter(password => /^[A-Za-z0-9]+$/.test(password))
            })
            passArr = [...passArr, ...rawData]
            console.log(rawData)
        } catch (error) {
            console.log('error', error)
        }
    }
    fs.appendFile("./mcupws.json", JSON.stringify(passArr, null, 3), (error) => {
        if (error) {
            console.log('An error has occurred ', error)
            return
        }
        console.log('Data written successfully to disk')
    })
    return
})()