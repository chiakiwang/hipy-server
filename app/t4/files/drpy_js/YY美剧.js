var rule = {
    title: 'YY美剧',
    host: 'https://yayameiju.cc',
    //hostJs: 'print(HOST);let html=request(HOST,{headers:{"User-Agent":MOBILE_UA}});let src = jsp.pdfh(html,"ul&&li&&a&&href");print(src);HOST=src.replace("/index.php","")',
    // homeUrl: '/',

    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
   
    //filterable: 0,//是否启用分类筛选,
    //url: '/frim/fyclass.html',

    headers: {//网站的请求头,完整支持所有的,常带ua和cookies
        'User-Agent':'MOBILE_UA',
        // "Cookie": "searchneed=ok"
    },
    timeout: 5000,
    //detailUrl: '/vod/fyid.html',
    searchUrl: '/search.php?searchword=**',

    //class_name: '美剧&最新美剧&灵异/惊悚&魔幻/科幻&犯罪/历史&都市/情感&动漫/卡通&选秀/综艺&电影&泰剧&日韩剧&剧集',
    //class_url: 'list1&list36&list30&list31&list32&list33&list34&list35&list2&list4&list7&list12',
    class_parse: 'ul.nav li;a&&Text;a&&href;.*/list(\\d+).html', 

    play_parse: true,
    lazy: '',
    limit: 6,

    推荐: '.clearfix .video-pic;a&&title;.loading&&data-original;.text-bg-r&&Text;a&&href',
    double: true, // 推荐内容是否双层定位
    一级: '.video-pic;a&&title;.loading&&data-original;.text-bg-r&&Text;a&&href',
    二级: {
          "title": "h1&&Text;ul.info.clearfix;li&&Text",
          "img": ".lazyload&&data-original",
          "desc": ";;;li.col-md-12--span:eq(2)&&Text;li.col-md-6--span:eq(1)&&Text",
          "content": "li.col-md-12:eq(3)&&Text",
          "tabs": "div.panel.clearfix&&a",
          "lists": ".playlists:eq(#id)&&li",
          "list_url": "a&&href"        
        },
        
    搜索: '*',
}
