const optionDefinitions = [
    {name: 'uname'},
    {name: 'pword'},
    {name: 'pname'}
]
const commandLineArgs = require("command-line-args")
const options = commandLineArgs(optionDefinitions)

uname = options.uname
pword = options.pword
pname = options.pname

const puppeteer = require('puppeteer');

(async() => {
    // setup browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // navigate to apex
    await page.goto("https://apex.cct.rpi.edu/apex/f?p=128")

    // login
    await page.type("#username", uname);
    await page.type("#password", pword);
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("input.btn-submit"),
    ]); // if timeout then return "incorrect login info"


    // nav to Personal
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#uHeader > nav > ul > li:nth-child(6) > a"),
    ]);

    // type name
    await page.evaluate( () => document.getElementById("P8_PREF_FIRST_NAME").value = "")
    await page.type("#P8_PREF_FIRST_NAME", pname);

    // submit name
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#B17981913808549937"),
    ]);

    await page.close();
    await browser.close();
})();
