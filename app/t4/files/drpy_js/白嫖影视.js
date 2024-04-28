muban.首图2.二级.title = '.stui-content__detail .title--span&&Text;.stui-content__detail p&&a&&Text';
muban.首图2.二级.content = 'p.col-pd&&Text';
muban.首图2.二级.tabs = '.stui-pannel_hd h3';
muban.首图2.二级.lists = '.stui-content__playlist:eq(#id) li';
muban.首图2.二级.desc = 'p.data:eq(3)&&Text;p.data&&a:eq(-1)&&Text;p.data&&a:eq(-2)&&Text;p.data:eq(1)&&Text;p.data:eq(2)&&Text';
var rule = {
	title: '白嫖影视',
	模板: '首图2',
	host: 'https://www.baipiaoys.com:9092',
	url:'/show/fyfilter.html',
    filterable:1,//是否启用分类筛选,
    filter_url:'{{fl.地区}}{{fl.剧情}}{{fl.类型}}{{fl.语言}}{{fl.字母}}/page/fypage{{fl.年代}}',
	filter:'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',
	filter_def: {
		1: { 类型: '/id/1' },
		2: { 类型: '/id/2' },
		3: { 类型: '/id/3' },
		4: { 类型: '/id/4' },
		5: { 类型: '/id/5' }
	},
	searchUrl:'/search/page/fypage/wd/**.html',
	tab_exclude:'影片|评论|榜单',
	lazy: `js:
	let html=request(input);
	let jscode=pdfh(html,'body&&script:eq(2)&&Text');
	let jsurl=jscode.match(/"url":"(.*?)"/)[1];
	input='https://www.baipiao-ys.cc:6062/player/analysis.php?v='+jsurl;
	`,
}