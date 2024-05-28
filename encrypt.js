const { JSDOM } = require('jsdom');
const { readFileSync } = require('fs');
const { Script } = require('vm');

class HSW_Sandbox {
    constructor(hsw = 'archive/de80b1b/custom_hsw.js') {
        this.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36";
        this.custom_hsw = readFileSync(hsw, 'utf-8');
        this.vm = this.loadJsdom();
        this.run_hsw(this.custom_hsw);
    }

    loadJsdom() {
        const dom = new JSDOM('<title>hsw</title>', {
            runScripts: 'dangerously',
            pretendToBeVisual: true,
            url: 'https://discord.com/',
            referrer: 'https://discord.com/register',
            storageQuota: 10000000
        });

        return dom.getInternalVMContext();
    }

    run_hsw(scriptContent) {
        const script = new Script(scriptContent);
        script.runInContext(this.vm);
    }

    encrypt(data) {
        const script = new Script(`encrypt('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiIxMWV0QytPYTNhVWdHd2M3TFF1Tms2aUgvWmQvMm1LeUFFdllZRDBKOGdUcE4yK2xEcXBNZmxuVFpnY2NBQUlaUW9GeVRpb3E3WmNyTkthc2xHOVhkKzFLK3FXVUp2eFFqUmVLeXhWSkZsd1NVOGJTSll0VkN2WnZaTlRmbURhbGliY2MzNUpIbEl0bE92d1ZZVkJTRzU4MFZrMG9CT254cHV3MFdGbWJtejRjam9IVlF0S05BZGpCOW9ieUFob1R6elE1enpDSmhnc042SWE5MDVobDZXWlN3WHRwSzFlOEVmd2ZzUnNpcXBIeEJQQ2MwOVo2Q2hBN1lOU1FoVFdlIiwibCI6Imh0dHBzOi8vbmV3YXNzZXRzLmhjYXB0Y2hhLmNvbS9jL2Y5MjJhNDEiLCJpIjoic2hhMjU2LVF0bWtBUnJEYXVTRDZPUExTN0t6Z3B1V3Z6WnJ2QndPS3JRTlRYM3Jra0E9IiwiZSI6MTcxNTYxNjY4MiwibiI6ImhzdyIsImMiOjEwMDB9.kO00qLSV_ogCVPzD5JnorvbSLyjU7gBHdtXhKgFdBuQ', '${data}')`);
        return script.runInContext(this.vm);
    }
}


async function encrypt(data) {
    const hsw = new HSW_Sandbox();
    const encrypted = hsw.encrypt(data);
    const hswstr = await encrypted;
    console.log(hswstr);
}

encrypt();
