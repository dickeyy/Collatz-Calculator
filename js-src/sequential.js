var fs = require('fs');
var data = fs.readFileSync('../src/lastSuccessful.json');
var obj = JSON.parse(data);
var oNum = BigInt(obj.number)
var num = BigInt(oNum)
var startNum = 0

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function main() {
    let startTime = Date.now()

    var calcRateThresh = 1000000

    sleep(0).then(() => {
        while (true) {

            if (startNum == BigInt(calcRateThresh)) {
                calcCalcRate(startTime, calcRateThresh)
                break
            }

            if (num % BigInt(1) == BigInt(0)) {
                num = num / BigInt(2)
                
                if (num == BigInt(1)) {
                    lastSuccessWrite = {
                        "number": `${oNum}`,
                        "startedAt": new Date().toISOString()
                    }
        
                    fs.writeFileSync('../src/lastSuccessful.json', JSON.stringify(lastSuccessWrite));
        
                    oNum = oNum + BigInt(1)
                    num = oNum
                    startNum += 1
                    console.log(`${new Date().toISOString()} -- Loop reached. NEXT: ${oNum.toLocaleString("en-US")}`)
                }
            } else {
                num = num * BigInt(3) + BigInt(1)
        
                if (num == BigInt(1)) {
                    lastSuccessWrite = {
                        "number": `${oNum}`,
                        "startedAt": new Date().toISOString()
                    }
        
                    fs.writeFileSync('../src/lastSuccessful.json', JSON.stringify(lastSuccessWrite));
        
                    oNum = oNum + BigInt(1)
                    num = oNum
                    startNum += 1
                    console.log(`${new Date().toISOString()} -- Loop reached. NEXT: ${oNum.toLocaleString("en-US")}`)
                }
            }
        }
    })
}

function calcCalcRate(startTime,threshold) {
    let timeTaken = Date.now() - startTime;

    fs.appendFile('runRate.txt', `${new Date().toISOString()} -- ${timeTaken}ms / ${timeTaken / 1000}s / ${Math.round(timeTaken / 1000 / 60)}min to calculate ${threshold.toLocaleString("en-US")} nums\n`, function(err) {
        if(err){
            throw err
        }
    });

    startNum = 0
    main()
}

main()