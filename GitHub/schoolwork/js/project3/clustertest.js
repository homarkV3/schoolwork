const cluster = require('cluster')
const numCPUs = require('os').cpus().length
let arr =[]

async function trial1() {
    if (cluster.isMaster) {
        const [, , qty] = process.argv.map(Number)
        const splitQty = qty / numCPUs;

        for (let i = 0; i < numCPUs; i++) {
            const worker = cluster.fork()
            let msg = { id: i, start: i * splitQty, end: i * splitQty + splitQty }
            worker.send(msg)
            worker.on('message', text => {
                arr.push(text)
            })
        }
    } else { //worker
        process.on('message', ({ id, start, end }) => {
            process.send(`Worker ${id} all done with my ${end - start + 1} things`)
            process.exit()
        })
    }
}
trial1()