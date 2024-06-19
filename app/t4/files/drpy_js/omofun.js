var rule={
  title: 'omofun动漫视频网',
  host: 'https://omofuns.xyz/index.php',
  homeUrl:'/label/new.html',
  url: '/vod/show/id/fyclass/page/fypage.html',
  searchable: 0,
  quickSearch: 0,
  filterable: 1,
  
 class_name:'电影&电视剧&综艺&动漫&绅士专区',
class_url:'1&2&3&4&5',

    
cate_exclude: "动漫资讯",





     searchable:5,
    quickSearch:0,
    headers:{
        'User-Agent':'MOBILE_UA'
    },
    timeout:5000,
    class_parse: 'ul.navbar-items&&a;a&&Text;a&&href;(\\d+)',
    play_parse:true,
 
    推荐: 'body&&.module-poster-item;.a&&Text;.lazyload&&data-original;.module-item-note&&Text;a&&href',
     一级: 'body&&.module-poster-item;.a&&Text;.lazyload&&data-original;.module-item-note&&Text;a&&href',
    二级: {
        "title": "h1&&Text",
        "img": "..module-item-pic&&img&&data-original",
        "desc": ".module-info-item:eq(4)&&Text;.module-info-item:eq(2)&&Text;.module-info-item:eq(1)&&Text;li.col-xs-12--span:eq(0)&&Text;;",
        "content": ".show-desc&&Text",
        "tabs": "#y-playList&&.tab-item",
        "lists": ".module-list:eq(#id) a",
    },

    searchUrl:'/phsch/page/fypage/wd/**.html',
    detailUrl:'/index.php/vod/detail/id/fyid.html', //非必填,二级详情拼接链接
    搜索:'body&&.module-card-item;.module-card-item-title&&Text;img&&data-original;.module-info-item-content&&Text;a&&href',
}