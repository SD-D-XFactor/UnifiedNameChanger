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
    await page.goto("https://apex.cct.rpi.edu/apex/f?p=128").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to navigate to directory!")
        process.exit(-1);
    });

    // login
    await page.type("#username", uname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to type username!")
        process.exit(-1);
    });
    await page.type("#password", pword).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to type password!")
        process.exit(-1);
    });
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("input.btn-submit"),
    ]).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to click input button")
        process.exit(-1);
    });


    // nav to Personal
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#uHeader > nav > ul > li:nth-child(6) > a"),
    ]).catch(() => {
        page.close();
        browser.close();
        console.log("Incorrect username or password!")
        process.exit(-1);
    });

    // type name
    await page.evaluate( () => document.getElementById("P8_PREF_FIRST_NAME").value = pname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to set preferred name!")
        process.exit(-1);
    });

    // submit name
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#B17981913808549937"),
    ]).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to submit preferred name!")
        process.exit(-1);
    });

    await page.close();
    await browser.close();
})();
