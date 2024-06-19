var rule = {
            title: '速播小屋',
            host: 'http://vzjkqi.subowu22.com',
          // url: '/show/fyclass/page/fypage/',
         url: '/show/fyfilter/page/fypage/',
          filterable: 1,//是否启用分类筛选,
headers: {
        'User-Agent': 'MOBILE_UA',
    },
    filter_url: '{{fl.cateId}}',
    filter: {
        "dianying": [{
            "key": "cateId",
            "name": "类型",
            "value": [
            {"v": "dongzuo", "n": "动作片"}, 
            {"v": "xiju", "n": "喜剧片"},
            {"v": "aiqing","n": "爱情片"}, 
            {"v": "kehuan", "n": "科幻片"}, 
            {"v": "kongbu", "n": "恐怖片"},
            {"v": "jingdian", "n": "经典片"}, 
            {"v": "zhanzheng","n": "战争片"}, 
            {"v": "jilu", "n": "纪录片"}]
        }],
        "dianshi": [{
            "key": "cateId",
            "name": "类型",
            "value": [
            {"v": "guochanju", "n": "国产剧"},
            {"v": "hanju", "n": "韩国剧"},
            {"v": "oumeiju", "n": "欧美剧"}, 
            {"v": "riju", "n": "日本剧"}, 
            {"v": "gangaoju", "n": "香港剧"}, 
            {"v": "taiwanju", "n": "台湾剧"}]
        }],
        "zongyi": [{
            "key": "cateId",
            "name": "类型",
            "value": [ ]
        }],
        "dongman": [{
            "key": "cateId","name": "类型",
            "value": [ ]
        }]
    },
    filter_def: {
        dianying: {cateId: 'dianying'},
        dianshi: {cateId: 'dianshi'},
        zongyi: {cateId: 'zongyi'},
        dongman: {cateId: 'dongman'}
    },
class_name: '电影&电视剧&综艺&动漫',
    class_url: 'dianying&dianshi&zongyi&dongman',
    play_parse: true,
            searchUrl: '/search**/page/fypage/',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 1,//是否启用分类筛选,

            play_parse: true,
            lazy: '',
            limit: 5,
            推荐: '.module-list;.module-items&&.module-item;a&&title;img&&data-src;.module-item-text&&Text;a&&href',
            double: true, // 推荐内容是否双层定位
            一级: '.module-items .module-item;a&&title;img&&data-src;.module-item-text&&Text;a&&href',
            二级: {
                "title": "h1&&Text;.tag-link&&Text",
                "img": ".module-item-pic&&img&&data-src",
                "desc": ".video-info-items:eq(0)&&Text;.video-info-items:eq(1)&&Text;.video-info-items:eq(2)&&Text;.video-info-items:eq(3)&&Text",
                "content": ".vod_content&&Text",
                "tabs": ".module-tab-item",
                "lists": ".module-player-list:eq(#id)&&.scroll-content&&a"
            },
            搜索: '.module-items .module-search-item;a&&title;img&&data-src;.video-serial&&Text;a&&href',
        }