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
    console.log("browser")

    // navigate to submitty
    await page.goto("https://submitty.cs.rpi.edu/home")
    console.log("submitty")

    // login
    await page.type("#login > label:nth-child(1) > input[type=text]", uname);
    await page.type("#login > label:nth-child(2) > input[type=password]", pword);
    await Promise.all([
        page.waitForNavigation({waitUntil: 'load'}),
        page.click("#login > input"),
    ]); // if timeout then return "incorrect login info"
    console.log("login")

    // nav to my profile
    await page.goto("https://submitty.cs.rpi.edu/user_profile")
    console.log("profile")

    // open 
    await page.click("#basic_info > span:nth-child(2) > a")
    console.log("form")

    // type name
    await page.evaluate( () => document.getElementById("user-firstname-change").value = "")
    await page.type("#user-firstname-change", firstname);
    await page.evaluate( () => document.getElementById("user-lastname-change").value = "")
    await page.type("#user-lastname-change", lastname);
    console.log("filled")

    // submit name
    await page.click("#edit-username-form > form > div > div > div.form-body > div.form-buttons > div > input")
    console.log("submitted")

    await page.close();
    await browser.close();
})();
