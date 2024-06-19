var rule = {
    title: '动漫狂',
    编码: 'big5',
    host: 'https://www.cartoonmad.com',
    url: '/m/?page=fypage&act=fyclass',
    class_name: '推荐&最新上架&热门连载',
    class_url: '0&1&2',
    searchUrl: '/m/?keyword=**&act=7',
    searchable: 2, //是否启用全局搜索,
    quickSearch: 0, //是否启用快速搜索,
    filterable: 0, //是否启用分类筛选,
    headers: {
        'User-Agent': 'UC_UA', // "Cookie": ""
    },
    //class_parse: '.type li;a&&Text;a&&href;/(\\w.*)',
    play_parse: true,
    lazy: `js:
        var html = fetch(input);
        var contents = pdfa(html, 'body&&.pages')
var content = contents.map(x => pdfh(x, 'a&&href').split('.')[0]);
var firstpage = input.split('comic/')[1].split('.')[0];
var htmlpage= content[content.length-2];
var page = []
    for (var i = firstpage; i <= htmlpage; i++) {
        page.push({
            url: 'https://cc.fun8.us/post/'+i+'.html'
        })
    }
var pics = bf(page).map(img => "https:"+pdfh(img, 'body&&img&&src').replace(' ',''))
            input = {
                jx: 0,
                url: 'pics://' + pics.join('&&'),
                parse: 0
            }`,
    limit: 6,
    推荐: 'body&&.comic_prev;.a1&&Text;img&&src;.a2&&Text;a:eq(2)&&href',
    double: true, // 推荐内容是否双层定位
    一级: 'body&&.comic_prev;.a1&&Text;img&&src;.a2&&Text;a:eq(2)&&href',
    二级: {
        "title": "tbody:eq(2)&&td:eq(9)&&Text",
        "img": ".stui-content__thumb .lazyload&&data-original",
        "desc": "tbody:eq(2) td:eq(6)&&Text;tbody:eq(2) td:eq(13)&&Text",
        "content": "tbody:eq(2) td:eq(16)&&Text",
        "tabs": "",
        "lists": "fieldset:eq(1)&&a",
        "list_text": "",
        "list_url": ""
    },
    搜索: 'body&&.comic_prev;.a1&&Text;img&&src;.a2&&Text;a:eq(2)&&href',
}