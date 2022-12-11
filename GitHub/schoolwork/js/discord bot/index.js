const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('./config.json');
const { LoremIpsum } = require('lorem-ipsum')
const puppeteer = require("puppeteer")
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });
const fs = require('fs')

var help = fs.readFileSync("./help.txt", 'utf8');
// When the client is ready, run this code (only once)
// We use 'c' for the event parameter to keep it separate from the already defined 'client'
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});

client.on('messageCreate', async Message => {
	if (Message.author.bot) return
    if (!Message.content.startsWith('!')) return
    input = Message.content.split(" ")
    switch (input[0]) {
        case(`!hello`):
            console.log("world")
            Message.reply("world")
            break
        case(`!help`):
            console.log(help)
            Message.reply(help)
            break
        case(`!lorem`):
            const lorem = new LoremIpsum()
            console.log(input)
            if (input.length == 1) {
                console.log(lorem.generateWords(10))
                Message.reply(lorem.generateWords(10))
            } else {
                console.log(lorem.generateWords(Number(input[1])))
                Message.reply(lorem.generateWords(Number(input[1])))
            }
            break
        case(`!virus`):
            await Message.reply(lorem.generateWords('```diff\n- YOU KILLED ME!\1- I\'LL SEE YOU IN HELL.```'))
            currCases = getCovid()
            break
        case(`!dadjoke`):
        
            break
        case(`!chuck`):
            break
        case(`!die`):
            process.exit(0)
        case(`!text`):
            break
        case(`!email`):
            break
        case(`!music`):
            break
        case(`!weather`):
            break
        default:
            Message.reply(`Unknown command ${msg.content}. If you type it again, I'll kill you. Type !help to see safer options.`)
            break
        }

        function getCovid() {
            (async () => {
                var url = `https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0jcky&gl=US&ceid=US%3Aen`
                const browser = await puppeteer.launch()
                try {
                    const page = await browser.newPage()
                    await page.goto(url)
                    console.log(url)
                    const rawData = await page.$("strong")
                    const text = await (await rawData.getProperty('textContent')).jsonValue()
                    console.log(`current covid cases in utah county: ${text}`)
                    Message.reply(`current covid cases in utah county: ${text}`)
                } catch (error) {
                    console.log('error', error)
                }
                return
            })()
        }
});

// Log in to Discord with your client's token
client.login(token);
