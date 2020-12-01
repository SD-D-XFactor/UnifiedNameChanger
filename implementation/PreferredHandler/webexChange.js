//https://rensselaer.webex.com/webappng/sites/rensselaer/dashboard?siteurl=rensselaer
const optionDefinitions = [
    {name: 'uname'},
    {name: 'pword'},
    {name: 'pname', multiple: true}
]
const commandLineArgs = require("command-line-args")
const options = commandLineArgs(optionDefinitions)

uname = options.uname
email = uname + "@rpi.edu"
pword = options.pword
pnameArr = options.pname
firstname = pnameArr[0]
lastname = pnameArr[1]
pname = firstname + " " + lastname

const puppeteer = require('puppeteer');

(async() => {
    // setup browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // navigate to webex
    await page.goto("https://rensselaer.webex.com/")

    // click login button
    await Promise.all([
        page.waitForSelector("#IDToken1"),
        page.click("#guest_signin_split_button-trigger > div > button:nth-child(1)")
    ]);

    // enter email
    await page.type("#IDToken1", email)
    await Promise.all([
        page.waitForSelector("#username"),
        page.click("#IDButton2")
    ]);

    // login
    await page.type("#username", uname)
    await page.type("#password", pword)
    await Promise.all([
        page.waitForSelector("#main_top_menu > div.nav_bar > div.top_nav > div.nav_t"),
        page.click("#homepage > div > div > div > form > button")
    ])

    // nav to profile edit
    await page.goto("https://rensselaer.webex.com/webappng/sites/rensselaer/myprofile/home")

    // open popup
    const popupPromise = new Promise(x => page.once('popup', x));
    await page.click("#viewMyProfile-changeMyProfile-Button");
    const popup = await popupPromise;

    // edit name
    await popup.waitForSelector("body > main > article > section:nth-child(1) > a:nth-child(3)")
    await Promise.all([
        popup.waitForSelector("body > main > article > section > div.row > div:nth-child(2) > input"),
        popup.click("body > main > article > section:nth-child(1) > a:nth-child(3)")
    ])
    await popup.evaluate( (pname) => {document.querySelector("body > main > article > section > div.row > div:nth-child(2) > input").value=pname}, pname)
    await popup.click("body > main > article > section > div.form-actions > button")

    await page.close();
    await browser.close();
})();
