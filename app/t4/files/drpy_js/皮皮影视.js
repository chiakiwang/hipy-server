var rule = {
    模板: 'mxpro',
    title: '皮皮影视',
    host: 'https://www.pptv06.com',
    class_parse: '.navbar-items li:gt(0):lt(8);a&&Text;a&&href;/(\\d+).html',
    tab_exclude: '排序',
    url: '/vodshow/fyclass--------fypage---.html',
    searchUrl: '/vodsearch/**----------fypage---.html',
    lazy: $js.toString(() => {
		var html = JSON.parse(request(input).match(/r player_.*?=(.*?)</)[1])
    var url = html.url
    if (html.encrypt == '1') {
        url = unescape(url);
    } else if (html.encrypt == '2') {
        url = unescape(base64Decode(url));
    }
    if (/m3u8/.test(url)) {
          input = {
				jx: 0,
				url: url,
				parse: 0
			}
        
    } else {
         eval(request(HOST + '/static/js/playerconfig.js'));
        var jx =HOST+ MacPlayerConfig.player_list[html.from].parse;
        if (jx == '') {
            jx =HOST+ MacPlayerConfig.parse
        }
log (jx)
       eval(request(jx + url,{
      headers: {
                'Referer': input
            }
        }).match(/var config = {[\s\S]*?}/)[0])
        
        log(config.url)
        
        
        eval(getCryptoJS())

       
        function rc4(data, key, t) {
            var pwd = key || 'ffsirllq';
            var cipher = '';
            var key = [];
            var box = [];
            var pwd_length = pwd.length;
            if (t == 1) {
                var data = window0.atob(data);
            } else {
                var data = encodeURIComponent(data);
            }

            var data_length = data.length;

            for (i = 0; i < 256; i++) {
                key[i] = pwd[i % pwd_length].charCodeAt();
                box[i] = i;
            }
            for (j = i = 0; i < 256; i++) {
                j = (j + box[i] + key[i]) % 256;
                tmp = box[i];
                box[i] = box[j];
                box[j] = tmp;
            }
            for (a = j = i = 0; i < data_length; i++) {
                a = (a + 1) % 256;
                j = (j + box[a]) % 256;
                tmp = box[a];
                box[a] = box[j];
                box[j] = tmp;
                k = box[((box[a] + box[j]) % 256)];
                cipher += String.fromCharCode(data[i].charCodeAt() ^ k);
            }
            if (t == 1) {
                return decodeURIComponent(cipher);
            } else {
                return window0.btoa(cipher);
            }
        }
        var play = rc4(config.url, "202205051426239465", 1)
        
        
        input = {
				jx: 0,
				url: play,
				parse: 0
			}

    }
}),
}