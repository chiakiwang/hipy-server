var rule = {
    title: '次元城动漫[漫]',
    host: 'https://www.cycanime.com',
    class_name: 'TV动漫&剧场&4k',
    class_url: '20&21&26',
    searchUrl: '/index.php/ajax/suggest?mid=1&wd=**&limit=50',
    searchUrl: '/search/wd/**/page/fypage.html',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'MOBILE_UA',
    },
    url: '/index.php/api/vod#type=fyclassfyfilter&page=fypage',
    filterable: 0,
    filter_url: '&class={{fl.class}}&year={{fl.year}}&letter={{fl.letter}}&by={{fl.by}}',
    filter: 'H4sIAAAAAAAAA+2W204TURSG32WuMdnT0nbDnZzP57PhopImEhETWk0IIUFOloNQDLSigGJCLCIWhJCWgr4MM9O+hdPO2mstDzE10cSYudv/989u55t0uteUpmuVd6a0+6FJrVIbGQuGw1qZNh58ELKjdZo19lbs/Dg49ihUvG7cxsZCMj+XLGA7aNNlQK9mb9Jxa2sVCsrqCmv7sxGLQg0Bd8fWjI9HaqsTcN/ccW5/Ru1zAnaXKSt6qjonYHf4JXexrDon4PcdPDUyWfV9TlCdGX1hxhPQQSjlPs3YnvVhQ+1zAnaJAyOdVp0T8D7fbdC9QMB9n7LmvHpmELB7s2+8OladE7B7skLPBQI6LD7Pbx8qByfgvrWkFVtU+5yA3c6l/TRU5wTV5V+f3WRi0EFQXS62m1tbgg4C3WfMnInjfRYDdnPL5uxL1TkBu7P9/O5ba+u9qjHjFem0GV03NzPqCsz4HE7Wc6lzuoIyfsbVkbWZZZ+BGd0WlHRhNT1c4M67NBkKTtCrZGTOb7LXJb5KHuEpB1ZcMu4l7uXcQ9zDuU5c51wQF4zrFcjtJeOSuOQ8QDzAuZ+4n3MfcR/n5KtzX518de6rk6/OfXXy1bmvTr469xXkK7ivIF/BfQX5Cu4ryFdwX0G+gvsK8hXcV5Cv4L6CfAX3FeQruK8gX0G+ekWF8i0uGZfEJecB4gHO/cT9nPuI+zgvJ17OuZe4l3MPcQ/nOnGdc0Gc+0ryldxXkq/kvpJ8JfeV5Cu5ryRfyX0l+UruK8lXcl9JvpL7SvKV3FeSr73kfztjoUgkxP94jhNm6lmJfzy3AdxGUgWkCkk1kGokNUBqkNQCqUVSB6QOST2QeiQNQBqQNAJpRNIEpAlJM5BmJC1AWpC0AmlF0gakDUk7kHYkHUA6kHQC6UTSBaQLSTeQbiQ9QHqQ9ALpRdIHpA9JP5B+JANABpAMAhlEMgRkCIm4pd6Bwor/VO5O0s/ETFzkE+c//EzM1SVzZ8aMn8BHREbtq/F0LJb2QAblvdFImJe51LwRVbNEeOThRKjw9cNlmuefGDl/OVb+hdHxvxgPf3cEdAcidyByByK1dAcidyByByJ3IPp+IPL+qYFoOXlzvaOObieUMrb8dMRwj2736HaPbrV0j2736HaPbvfo/vbonv4K+TrlXkAbAAA=',
    filter_def: {},
    detailUrl: '/bangumi/fyid',
    play_parse: true,
   // sniffer: 1,
   // is_video: 'obj/tos|bd.xhscdn|/ugc/',
    lazy: $js.toString(() => {
        var html = request(input)
  
    html = JSON.parse(html.match(/r player_.*?=(.*?)</)[1])
    var url = html.url
    if (html.encrypt == '1') {
        url = unescape(url);
    } else if (html.encrypt == '2') {
        url = unescape(base64Decode(url));
    }
    
        eval(request(HOST + '/static/js/playerconfig.js'));
        var jx = MacPlayerConfig.player_list[html.from].parse;
        if (jx == '') {
            jx = MacPlayerConfig.parse
        }
log (jx)
            
	  eval(getCryptoJS())

        function decrypt(jx, url) {
            const sortByKey = (key, arr, callback) => {
                let f = (a, b) => callback(a[key], b[key]);
                return arr.sort(f);
            }
           var html=request(jx + url, {
        headers: {
            'Referer':''
            }
        })
eval(html.match(/var config = {[\s\S]*?}/)[0]+'}')
            log(config.url)
            
            var _pr = pdfh(html, "meta[name=\"viewport\"]&&id").replace("now_", "");
            var _pu = pdfh(html, "meta[charset=\"UTF-8\"]&&id").replace("now_", "");
            let _puArr = [],
                _newArr = [],
                _code = '';
            for (var i = 0; i < _pu.length; i++) {
                _puArr.push({
                    'id': _pu[i],
                    'text': _pr[i]
                });
            }
            _newArr = sortByKey("id", _puArr, (a, b) => a - b);
            for (var i = 0; i < _newArr.length; i++) {
                _code += _newArr[i]['text'];
            }
            let vkey = CryptoJS.MD5(_code + "YLwJVbXw77pk2eOrAnFdBo2c3mWkLtodMni2wk81GCnP94ZltW").toString();
            let key = CryptoJS.enc.Utf8.parse(vkey.substring(16));
            let iv = CryptoJS.enc.Utf8.parse(vkey.substring(0, 16));
            let decrypted = CryptoJS.AES.decrypt(config.url, key, {
                iv: iv,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            });
            return decrypted.toString(CryptoJS.enc.Utf8);
        }

log(jx)
log(url)
        var play = decrypt(jx, url)

input = {
parse: 0, 
url: play,
 js: ''
 };
    }),
    limit: 6,
    推荐: '.list-vod.flex .public-list-box;a&&title;.lazy&&data-original;.public-list-prb&&Text;a&&href',
    一级: $js.toString(() => {
        let body = input.split("#")[1];
        let t = Math.round(new Date / 1e3).toString();
        let key = md5("DS" + t + "DCC147D11943AF75");
        let url = input.split("#")[0];
        body = body + "&time=" + t + "&key=" + key;
        print(body);
        fetch_params.body = body;
        let html = post(url, fetch_params);
        let data = JSON.parse(html);
        VODS = data.list.map(function (it) {
            it.vod_pic = urljoin2(input.split("/i")[0], it.vod_pic);
            return it
        });
    }),
    二级: {
        title: '.slide-info-title&&Text;.slide-info:eq(3)--strong&&Text',
        img: '.detail-pic&&data-original',
        desc: '.fraction&&Text;.slide-info-remarks:eq(1)&&Text;.slide-info-remarks:eq(2)&&Text;.slide-info:eq(2)--strong&&Text;.slide-info:eq(1)--strong&&Text',
        content: '#height_limit&&Text',
        tabs: '.anthology.wow.fadeInUp.animated&&.swiper-wrapper&&a',
        tab_text: '.swiper-slide&&Text',
        lists: '.anthology-list-box:eq(#id) li',
    },
    搜索: 'json:list;name;pic;;id',
    搜索: $js.toString(() => {
        let html = fetch(input);
        let list = pdfa(html, ".public-list-box");
        VODS = list.map(x => {
            return {
                vod_name: pdfh(x, ".thumb-txt&&Text"),
                vod_pic: pdfh(x, ".lazy&&data-src"),
                vod_remarks: pdfh(x, ".public-list-prb&&Text"),
                vod_content: pdfh(x, ".thumb-blurb&&Text"),
                vod_id: pdfh(x, "a&&href")
            }
        });
    }),
    图片替换: '&amp;=>&'
}