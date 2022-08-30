const fs = require('fs');

const text = fs.writeFileSync('help.text', {encoding: 'utf8'})
console.log(JSON.stringify(text))
