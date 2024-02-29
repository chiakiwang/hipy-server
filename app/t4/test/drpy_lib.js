const CryptoJS = require('./crypto-js')
const cheerio = require('./cheerio.min')
const 模板 = require('./模板')
const gbkTool = require('./gbk')
const pmEnv = require('./pm_env')

function base64Encode(text){
    return CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(text));
    // return text
}

function base64Decode(text){
    return CryptoJS.enc.Utf8.stringify(CryptoJS.enc.Base64.parse(text));
    // return text
}

function md5(text) {
    return CryptoJS.MD5(text).toString();
}
// console.log('CryptoJS:',CryptoJS)
// console.log('cheerio:',cheerio)
// console.log('模板:',模板)
// console.log('gbkTool:',gbkTool)
console.log('pmEnv:',pmEnv)
console.log('env:',pmEnv.get_env())

let strTool = gbkTool()
let input = strTool.encode('斗罗大陆')
console.log('input:',input)
module.exports = {
    base64Encode,
    base64Decode,
    md5,
    CryptoJS
}