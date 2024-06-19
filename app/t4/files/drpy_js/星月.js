var rule = {
模板:'自动',
模板修改: $js.toString(() => {
        muban.自动.二级.tabs = '#mobile-tab-box&&.tab-item';
               }),
title:'星月',
host:'http://107.151.243.94:5566',
url:'/index.php/vod/show/id/fyclass/page/fypagr.html',
searchUrl:'index.php/vod/search/page/fypage/wd/**.html',
class_parse: '.navbar-items&&li:gt(0):lt(6);a&&Text;a&&href;.*/(.*?).html',
play_parse: true,
  lazy: `js:
var kcode = JSON.parse(request(input).match(/var player_.*?=(.*?)</)[1]);
var kurl = unescape(base64Decode(kcode.url));
var jurl= 'http://xn--kiv066b.icu/player/?url='+kurl;
var jcode =JSON.parse(request(jurl).match(/var config=(.*?)var version/)[1]);
jurl = jcode.url;
if (/m3u8|mp4/.test(jurl)) {
input = { jx: 0, parse: 0, url: jurl }
} else {
input = { jx: 0, parse: 1, url: jurl }
}`,
搜索: '.module-items&&.module-item;.module-card-item-title&&a&&Text;img&&data-original;.module-item-note&&Text;.module-card-item-title&&a&&href',
}