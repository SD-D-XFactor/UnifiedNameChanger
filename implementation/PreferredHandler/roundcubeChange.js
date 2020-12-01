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
    await page.goto("https://webmail.rpi.edu/roundcube/")

    // login
    await page.type("#rcmloginuser", uname);
    await page.type("#rcmloginpwd", pword);
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#login-form > div.box-inner > form > p > input"),
    ]); // if timeout then return "incorrect login info"

    await page.goto("https://webmail.rpi.edu/roundcube/?_task=settings&_action=identities")

    // nav to first Identity
    await page.click("#identities-table > tbody > tr:first-child > td:first-child");
    await page.waitForFunction('document.querySelector("#identities-table > tbody > tr:first-child").classList.value == "selected focused"');
    await page.waitForSelector('iframe[id="preferences-frame"]');

    // type name
    const elementHandle = await page.$('iframe[id="preferences-frame"]')
    const frame = await elementHandle.contentFrame();

    await frame.evaluate((pname) => {
        document.querySelector('#preferences-details > form > fieldset:nth-child(6) > table > tbody > tr:nth-child(1) > td:nth-child(2) > input').value = pname;
        document.querySelector("body > div.footerleft.formbuttons > input").click();
    }, pname);

    // submit name
    await page.close();
    await browser.close();
})();
