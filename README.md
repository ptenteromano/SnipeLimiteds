## A script to get UGC items for free quickly

Features
- Get free limiteds
- Searches 24/7 to see if it's for sale
- Easy to use
- Lightweight
- Retries purchase when it fails
- Integrated Anti-Crash
- Speed in milliseconds

## Installation

### Step 1
**Download the script**

Go to https://github.com/ptenteromano/SnipeLimiteds
Click on "Code" > "Download ZIP" or go to the latest Release.

This will download the script as a .zip file, extract all the files in the folder of your choice.
Make sure you know where the folder is!

<hr>

### Step 2
**Access your Roblox Account**

We will put your Roblox cookie in the `cookies.txt` file (this file is in the `data/` folder), it should be the only thing in this file.

This is to be able to log in to your account to make purchases.

Install the Cookie-Editor extension for your browser:

For [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)

For [Edge](https://microsoftedge.microsoft.com/addons/detail/cookieeditor/neaplmfkghagebokkhpjpoebhdledlfi)

Then open a tab in Roblox and click on the extension, then click on the `.ROBLOSECURITY` tab and copy **everything** that is inside the Value box. Now open `data/cookies.txt` and paste it there.

This is the `.ROBLOSECURITY`, don't share it with anyone!!

<hr>

### Step 3
**Run the Bot**

Install Python3, you should be able to run python from the command line.
Your best bet is to google this and find the correct steps for your operating system.

After installing, open `PowerShell` for Windows (or `Terminal` if on a Mac).
Move to the directory where the repository is using the `cd` command.

For example, if the "SnipeLimiteds" folder is in your Downloads, you would type: `cd Downloads/SnipeLimiteds-Main`
Then run `python main.py`, it will install the libraries for you.
When that's done, you need to run it again in the same way: `python main.py`.

**Note**: You may have to run with `python3` or `python.exe` instead of just `python`

<hr>

### Optional
**Add specific limiteds**

You can optionally add in limiteds ID that are currently, or will be going on sale soon. In the `limiteds.txt` file, add the IDs separated by commas, like this: `12345,67890,82141`

This is optional, the bot should be able to search for currently on-sale limiteds. If no limiteds on sale, it will continue to search.
