const optionDefinitions = [
    {name: 'uname'},
    {name: 'pword'},
    {name: 'pname', multiple: true}
];
const commandLineArgs = require("command-line-args");
const options = commandLineArgs(optionDefinitions);

uname = options.uname;
pword = options.pword;
pname_arr = options.pname;
firstname = pname_arr[0];
lastname = pname_arr[1];
pname = firstname + " " + lastname;

const puppeteer = require('puppeteer');

(async() => {
    // setup browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // navigate to roundcube
    await page.goto("https://webmail.rpi.edu/roundcube/").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to visit roundcube!")
        process.exit(-1);
    });

    // login
    await page.type("#rcmloginuser", uname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to type username!")
        process.exit(-1);
    });
    await page.type("#rcmloginpwd", pword).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to type password!")
        process.exit(-1);
    });
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#login-form > div.box-inner > form > p > input"),
    ]).catch(() => {
        page.close();
        browser.close();
        console.log("Incorrect username or password!")
        process.exit(-1);
    });

    await page.goto("https://webmail.rpi.edu/roundcube/?_task=settings&_action=identities").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to go to identity seciton of settings!")
        process.exit(-1);
    });

    // nav to first Identity
    await page.click("#identities-table > tbody > tr:first-child > td:first-child").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to click first identity!")
        process.exit(-1);
    });
    await page.waitForFunction('document.querySelector("#identities-table > tbody > tr:first-child").classList.value == "selected focused"').catch(() => {
        page.close();
        browser.close();
        console.log("Failed to select first entity!")
        process.exit(-1);
    });
    await page.waitForSelector('iframe[id="preferences-frame"]').catch(() => {
        page.close();
        browser.close();
        console.log("iframe failed to appear!")
        process.exit(-1);
    });

    // type name
    const elementHandle = await page.$('iframe[id="preferences-frame"]')
    const frame = await elementHandle.contentFrame();

    await frame.evaluate((pname) => {
        document.querySelector('#preferences-details > form > fieldset:nth-child(6) > table > tbody > tr:nth-child(1) > td:nth-child(2) > input').value = pname;
        document.querySelector("body > div.footerleft.formbuttons > input").click();
    }, pname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to input preferred name in iframe!")
        process.exit(-1);
    });

    // submit name
    await page.close();
    await browser.close();
})();
