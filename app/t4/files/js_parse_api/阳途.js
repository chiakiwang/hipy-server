// http://localhost:5707/parse/api/阳途.js?url=https://m.iqiyi.com/v_1pj3ayb1n70.html
function lazy() {
    try {
        realUrl = snifferMediaUrl('https://jx.yangtu.top/?url=' + input).url;
        return realUrl
    } catch (e) {
        log(e.message)
        return input
    }
}

