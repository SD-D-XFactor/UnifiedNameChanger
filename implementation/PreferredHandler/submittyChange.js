const optionDefinitions = [
    {name: 'uname'},
    {name: 'pword'},
    {name: 'pname', multiple: true}
]
const commandLineArgs = require("command-line-args")
const options = commandLineArgs(optionDefinitions)

uname = options.uname
pword = options.pword
pnameArr = options.pname
firstname = pnameArr[0]
lastname = pnameArr[1]

const puppeteer = require('puppeteer');

(async() => {
    // setup browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // navigate to submitty
    await page.goto("https://submitty.cs.rpi.edu/home").catch(() => {
        page.close();
        browser.close();
        console.log("Connection error!")
        process.exit(-1);
    });

    // login
    await page.type("#login > label:nth-child(1) > input[type=text]", uname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to type username!")
        process.exit(-1);
    });
    await page.type("#login > label:nth-child(2) > input[type=password]", pword).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to type password")
        process.exit(-1);
    });
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#login > input"),
    ]).catch(error => {
        page.close();
        browser.close();
        console.log("Incorrect Username or Password!")
        process.exit(-1);
    });

    // nav to my profile
    await page.goto("https://submitty.cs.rpi.edu/user_profile").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to go to user profile page!")
        process.exit(-1);
    });

    // open 
    await page.click("#basic_info > span:nth-child(2) > a").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to open name change page!")
        process.exit(-1);
    });

    // type name
    await page.evaluate( () => document.getElementById("user-firstname-change").value = firstname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to change first name!")
        process.exit(-1);
    });
    await page.evaluate( () => document.getElementById("user-lastname-change").value = lastname).catch(() => {
        page.close();
        browser.close();
        console.log("Failed to change last name!")
        process.exit(-1);
    });

    // submit name
    await page.click("#edit-username-form > form > div > div > div.form-body > div.form-buttons > div > input").catch(() => {
        page.close();
        browser.close();
        console.log("Failed to submit name!")
        process.exit(-1);
    });

    await page.close();
    await browser.close();
})();
