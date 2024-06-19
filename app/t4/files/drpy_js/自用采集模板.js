var rule = {
  title: '喵派对',
  host: 'https://www.lezy.lol',
  homeTid: '13',
  homeUrl: '/api.php/provide/vod/?ac=detail&t={{rule.homeTid}}',
  detailUrl: '/api.php/provide/vod/?ac=detail&ids=fyid',
  searchUrl: '/api.php/provide/vod/?wd=**&pg=fypage',
  url: '/api.php/provide/vod/?ac=detail&pg=fypage&t=fyclass',
  headers: {
    'User-Agent': 'MOBILE_UA',
  },
  timeout: 5000,
  class_parse: 'json:class;',
  limit: 20,
  multi: 1,
  searchable: 2,
  play_parse: true,
  parse_url: '',
  lazy: "js:\n      if(/\\.(m3u8|mp4)/.test(input)){\n        input = {parse:0,url:input}\n      } else {\n        if (rule.parse_url.startsWith('json:')) {\n          let purl = rule.parse_url.replace('json:','')+input;\n          let html = request(purl);\n          input = {parse:0,url:JSON.parse(html).url}\n        } else {\n          input= rule.parse_url+input;\n        }\n      }\n      ",
  推荐: '*',
  一级: 'json:list;vod_name;vod_pic;vod_remarks;vod_id;vod_play_from',
  二级: 'js:\n      let html=request(input);\n      html=JSON.parse(html);\n      let data=html.list;\n      VOD=data[0];',
  搜索: '*',
}