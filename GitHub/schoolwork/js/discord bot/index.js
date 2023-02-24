const { Client, Events, GatewayIntentBits} = require('discord.js');
const { token } = require('./config.json');
const { LoremIpsum } = require('lorem-ipsum')
const puppeteer = require("puppeteer")
const client = new Client({ 
    intents: [
        GatewayIntentBits.Guilds, 
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.GuildVoiceStates, 
        GatewayIntentBits.MessageContent
    ] });
const fs = require('fs')
const nodemailer = require('nodemailer')
const open =  require('open')
const { DisTube } = require('distube');

client.distube = new DisTube(client, {
    leaveOnStop: false,
    emitNewSongOnly: true,
    emitAddSongWhenCreatingQueue: false,
    emitAddListWhenCreatingQueue: false,
})

var help = fs.readFileSync("./help.txt", 'utf8');
// When the client is ready, run this code (only once)
// We use 'c' for the event parameter to keep it separate from the already defined 'client'
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});

client.on('messageCreate', async message => {
	if (message.author.bot) return
    if (!message.content.startsWith('!')) return
    input = message.content.split(" ")

    switch (input[0]) {
        case(`!hello`):
            if (input.length > 1) return message.reply("please read the help and follow as this does not take any other argument")
            console.log("world")
            message.reply("world")
            break
        case(`!help`):
            if (input.length > 1) return message.reply("please read the help and follow as this does not take any other argument")
            console.log(help)
            message.reply(help)
            break
        case(`!lorem`):
            if (input.length > 2) return message.reply("please read the help and follow as this does not take more then 1 argument")
            const lorem = new LoremIpsum()
            console.log(input)
            if (input.length == 1) {
                console.log(lorem.generateWords(10))
                message.reply(lorem.generateWords(10))
            } else {
                console.log(lorem.generateWords(Number(input[1])))
                message.reply(lorem.generateWords(Number(input[1])))
            }
            break
        case(`!virus`):
            if (input.length > 1) return message.reply("please read the help and follow as this does not take any other argument")
            getCovid()
            break
        case(`!dadjoke`):
            if (input.length > 1) return message.reply("please read the help and follow as this does not take any other argument")
            joke("./dadjoke.txt", 100)
            break
        case(`!chuck`):
            if (input.length > 1) return message.reply("please read the help and follow as this does not take any other argument")
            joke("./chuck.txt", 101)
            break
        case(`!die`):
            if (input.length > 1) return message.reply("please read the help and follow as this does not take any other argument")
            process.exit(0)
        case(`!email`):
            if (input.length > 4) return message.reply("please read the help and follow as this does not take more then 3 argument")
            sendemail(input[1], input[2], input[3])
            break
        case(`!spotify`):
            if (input.length > 2) return message.reply("please read the help and follow as this does not take more then 1 argument")
            message.reply("opening spotify on web")
            open(`https://open.spotify.com/search/${input[1]}`);
            break
        case(`!play`):
            const channel = message.member.voice.channel
            if(!channel) return message.channel.send('please join a channel for this to work')
            console.log(client.distube.voices.get(message.guild))
            await message.reply("**Searching and attempting...**")
            await message.reply("Searching done :ok_hand: ")
            await client.distube.play(channel, input.join(' '),{
                textChannel: message.channel,
                member: message.member,
            })
            break
        default:
            message.reply(`Unknown command ${message.content}. If you type it again, I'll kill you. Type !help to see safer options.`)
            break
        }

        function joke(file, amount){
            var joke = fs.readFileSync(file, 'utf8');
            jokes = joke.split("\n")
            console.log(`${jokes[getRandomInt(amount)]}`)
            message.reply(`${jokes[getRandomInt(amount)]}`)
        }

        function getRandomInt(max) {
            return Math.floor(Math.random() * max);
        }

        function sendemail(to, subj, content) {
            var transporter = nodemailer.createTransport({
                service: 'gmail',
                auth: {
                  user: `homaxx98@gmail.com`,
                  pass: `gxjdsqgdrmmlqzux`
                }
              })
              var mailOptions = {
                from: `homaxx98@gmail.com`,
                to: `${to}`,
                subject: `${subj}`,
                text: `${content}`
              }
              
              transporter.sendMail(mailOptions, function(error, info){
                if (error) {
                  message.reply(`${error}`)
                  console.log(error)
                } else {
                  message.reply('Email sent: ' + info.response)
                  console.log('Email sent: ' + info.response)
                }
              })
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
                    message.reply(`current covid cases in utah county: ${text}`)
                } catch (error) {
                    console.log('error', error)
                }
                return
            })()
        }
});
// Log in to Discord with your client's token
client.login(token);
