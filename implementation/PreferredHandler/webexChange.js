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
    await page.goto("https://rensselaer.webex.com/").catch(() => {
        page.close();
        browser.close();
        console.log("Connection error!")
        process.exit(-1);
    });

    // click login button
    await Promise.all([
        page.waitForSelector("#IDToken1"),
        page.click("#guest_signin_split_button-trigger > div > button:nth-child(1)")
    ]).catch(error => {
        page.close();
        browser.close();
        console.log("Failed to click login button!")
        process.exit(-1);
    });

    // enter email
    await page.type("#IDToken1", email).catch(error => {
        page.close();
        browser.close();
        console.log("Failed to type email!")
        process.exit(-1);
    });
    await Promise.all([
        page.waitForSelector("#username"),
        page.click("#IDButton2")
    ]).catch(error => {
        page.close();
        browser.close();
        console.log("Incorrect email!")
        process.exit(-1);
    });

    // login
    await page.type("#username", uname).catch(error => {
        page.close();
        browser.close();
        console.log("Failed to type username!")
        process.exit(-1);
    });
    await page.type("#password", pword).catch(error => {
        page.close();
        browser.close();
        console.log("Failed to type password!")
        process.exit(-1);
    });
    await Promise.all([
        page.waitForSelector("#main_top_menu > div.nav_bar > div.top_nav > div.nav_t"),
        page.click("#homepage > div > div > div > form > button")
    ]).catch(error => {
        page.close();
        browser.close();
        console.log("Incorrect Username or Password!")
        process.exit(-1);
    });

    // nav to profile edit
    await page.goto("https://rensselaer.webex.com/webappng/sites/rensselaer/myprofile/home").catch(error => {
        page.close();
        browser.close();
        console.log("Failed to access namechange page!")
        process.exit(-1);
    });

    // open popup
    const popupPromise = new Promise(x => page.once('popup', x));
    await page.click("#viewMyProfile-changeMyProfile-Button").catch(error => {
        page.close();
        browser.close();
        console.log("Failed to open popup!")
        process.exit(-1);
    });
    const popup = await popupPromise;

    // edit name
    await popup.waitForSelector("body > main > article > section:nth-child(1) > a:nth-child(3)").catch(error => {
        page.close();
        browser.close();
        console.log("Failed to access namechange page!")
        process.exit(-1);
    });
    await Promise.all([
        popup.waitForSelector("body > main > article > section > div.row > div:nth-child(2) > input"),
        popup.click("body > main > article > section:nth-child(1) > a:nth-child(3)")
    ]).catch(error => {
        page.close();
        browser.close();
        console.log("Failed to access namechange page!")
        process.exit(-1);
    });
    await popup.evaluate( (pname) => {document.querySelector("body > main > article > section > div.row > div:nth-child(2) > input").value=pname}, pname).catch(error => {
        page.close();
        browser.close();
        console.log("Failed to submit namechange!")
        process.exit(-1);
    });
    await popup.click("body > main > article > section > div.form-actions > button").catch(error => {
        page.close();
        browser.close();
        console.log("Failed to submit namechange!")
        process.exit(-1);
    });

    await page.close();
    await browser.close();
})();
