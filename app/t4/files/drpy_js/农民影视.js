// 发布页 https://www.nmdvd.com/
/**
 * 环境变量设置方法1: DR-PY 后台管理界面
    * CMS后台管理 > 设置中心 > 环境变量 > {"nmjx_url":"XXXXXXX"} > 保存
 * 环境变量设置方法2: 手动替换
    * 底下代码 "$nmjx_url" 比如 "http://localhost:5708/nm?all=&url="
 */
var rule={
	title:'农民影视',
	//host:'https://www.nmddd.com',
	host:'https://www.nmdvd.com/',
	hostJs:`print(HOST);let html=request(HOST,{headers:{"User-Agent":MOBILE_UA}});
	let src = jsp.pdfh(html,"body&&a:eq(1)&&href")||jsp.pdfh(html,"body&&a:eq(1)&&Text");
	if(!src.startsWith('http')){src='https://'+src};print("抓到主页:"+src);HOST=src`,
	url:'/vod-list-id-fyfilter.html',
	// /vod-list-id-2-pg-1-order--by-time-class-0-year-2023-letter--area--lang-.html
	filterable:1,//是否启用分类筛选,
	filter_url:'{{fl.cateId}}-pg-fypage-order--by-{{fl.by or "time"}}-class-0-year-{{fl.year}}-letter-{{fl.letter}}-area-{{fl.area}}-lang-',
	filter: {
		"1":[{"key":"cateId","name":"类型","value":[{"n":"全部","v":"1"},{"n":"动作片","v":"5"},{"n":"喜剧片","v":"6"},{"n":"爱情片","v":"7"},{"n":"科幻片","v":"8"},{"n":"恐怖片","v":"9"},{"n":"剧情片","v":"10"},{"n":"战争片","v":"11"},{"n":"惊悚片","v":"16"},{"n":"奇幻片","v":"17"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"大陆"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"韩国","v":"韩国"},{"n":"日本","v":"日本"},{"n":"泰国","v":"泰国"},{"n":"新加坡","v":"新加坡"},{"n":"马来西亚","v":"马来西亚"},{"n":"印度","v":"印度"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"加拿大","v":"加拿大"},{"n":"西班牙","v":"西班牙"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"},{"n":"1999","v":"1999"},{"n":"1998","v":"1998"},{"n":"1997","v":"1997"},{"n":"1996","v":"1996"},{"n":"1995","v":"1995"},{"n":"1994","v":"1994"},{"n":"1993","v":"1993"},{"n":"1992","v":"1992"},{"n":"1991","v":"1991"},{"n":"1990","v":"1990"},{"n":"1989","v":"1989"},{"n":"1988","v":"1988"},{"n":"1987","v":"1987"},{"n":"1986","v":"1986"},{"n":"1985","v":"1985"},{"n":"1984","v":"1984"},{"n":"1983","v":"1983"},{"n":"1982","v":"1982"},{"n":"1981","v":"1981"},{"n":"1980","v":"1980"},{"n":"1979","v":"1979"},{"n":"1978","v":"1978"},{"n":"1977","v":"1977"},{"n":"1976","v":"1976"},{"n":"1975","v":"1975"},{"n":"1974","v":"1974"},{"n":"1973","v":"1973"},{"n":"1972","v":"1972"},{"n":"1971","v":"1971"},{"n":"1970","v":"1970"},{"n":"1969","v":"1969"},{"n":"1968","v":"1968"},{"n":"1967","v":"1967"},{"n":"1966","v":"1966"},{"n":"1965","v":"1965"},{"n":"1964","v":"1964"},{"n":"1963","v":"1963"},{"n":"1962","v":"1962"},{"n":"1961","v":"1961"},{"n":"1960","v":"1960"}]},{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
		"2":[{"key":"cateId","name":"类型","value":[{"n":"全部","v":"2"},{"n":"国产剧","v":"12"},{"n":"港台泰","v":"13"},{"n":"日韩剧","v":"14"},{"n":"欧美剧","v":"15"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"大陆"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"韩国","v":"韩国"},{"n":"日本","v":"日本"},{"n":"泰国","v":"泰国"},{"n":"新加坡","v":"新加坡"},{"n":"马来西亚","v":"马来西亚"},{"n":"印度","v":"印度"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"加拿大","v":"加拿大"},{"n":"西班牙","v":"西班牙"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"},{"n":"1999","v":"1999"},{"n":"1998","v":"1998"},{"n":"1997","v":"1997"},{"n":"1996","v":"1996"},{"n":"1995","v":"1995"},{"n":"1994","v":"1994"},{"n":"1993","v":"1993"},{"n":"1992","v":"1992"},{"n":"1991","v":"1991"},{"n":"1990","v":"1990"},{"n":"1989","v":"1989"},{"n":"1988","v":"1988"},{"n":"1987","v":"1987"},{"n":"1986","v":"1986"},{"n":"1985","v":"1985"},{"n":"1984","v":"1984"},{"n":"1983","v":"1983"},{"n":"1982","v":"1982"},{"n":"1981","v":"1981"},{"n":"1980","v":"1980"},{"n":"1979","v":"1979"},{"n":"1978","v":"1978"},{"n":"1977","v":"1977"},{"n":"1976","v":"1976"},{"n":"1975","v":"1975"},{"n":"1974","v":"1974"},{"n":"1973","v":"1973"},{"n":"1972","v":"1972"},{"n":"1971","v":"1971"},{"n":"1970","v":"1970"},{"n":"1969","v":"1969"},{"n":"1968","v":"1968"},{"n":"1967","v":"1967"},{"n":"1966","v":"1966"},{"n":"1965","v":"1965"},{"n":"1964","v":"1964"},{"n":"1963","v":"1963"},{"n":"1962","v":"1962"},{"n":"1961","v":"1961"},{"n":"1960","v":"1960"}]},{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
		"3":[{"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"大陆"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"韩国","v":"韩国"},{"n":"日本","v":"日本"},{"n":"泰国","v":"泰国"},{"n":"新加坡","v":"新加坡"},{"n":"马来西亚","v":"马来西亚"},{"n":"印度","v":"印度"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"加拿大","v":"加拿大"},{"n":"西班牙","v":"西班牙"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"},{"n":"1999","v":"1999"},{"n":"1998","v":"1998"},{"n":"1997","v":"1997"},{"n":"1996","v":"1996"},{"n":"1995","v":"1995"},{"n":"1994","v":"1994"},{"n":"1993","v":"1993"},{"n":"1992","v":"1992"},{"n":"1991","v":"1991"},{"n":"1990","v":"1990"},{"n":"1989","v":"1989"},{"n":"1988","v":"1988"},{"n":"1987","v":"1987"},{"n":"1986","v":"1986"},{"n":"1985","v":"1985"},{"n":"1984","v":"1984"},{"n":"1983","v":"1983"},{"n":"1982","v":"1982"},{"n":"1981","v":"1981"},{"n":"1980","v":"1980"},{"n":"1979","v":"1979"},{"n":"1978","v":"1978"},{"n":"1977","v":"1977"},{"n":"1976","v":"1976"},{"n":"1975","v":"1975"},{"n":"1974","v":"1974"},{"n":"1973","v":"1973"},{"n":"1972","v":"1972"},{"n":"1971","v":"1971"},{"n":"1970","v":"1970"},{"n":"1969","v":"1969"},{"n":"1968","v":"1968"},{"n":"1967","v":"1967"},{"n":"1966","v":"1966"},{"n":"1965","v":"1965"},{"n":"1964","v":"1964"},{"n":"1963","v":"1963"},{"n":"1962","v":"1962"},{"n":"1961","v":"1961"},{"n":"1960","v":"1960"}]},{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
		"4":[{"key":"cateId","name":"类型","value":[{"n":"全部","v":"4"},{"n":"动漫剧","v":"18"},{"n":"动漫片","v":"19"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"大陆"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"韩国","v":"韩国"},{"n":"日本","v":"日本"},{"n":"泰国","v":"泰国"},{"n":"新加坡","v":"新加坡"},{"n":"马来西亚","v":"马来西亚"},{"n":"印度","v":"印度"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"加拿大","v":"加拿大"},{"n":"西班牙","v":"西班牙"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"},{"n":"1999","v":"1999"},{"n":"1998","v":"1998"},{"n":"1997","v":"1997"},{"n":"1996","v":"1996"},{"n":"1995","v":"1995"},{"n":"1994","v":"1994"},{"n":"1993","v":"1993"},{"n":"1992","v":"1992"},{"n":"1991","v":"1991"},{"n":"1990","v":"1990"},{"n":"1989","v":"1989"},{"n":"1988","v":"1988"},{"n":"1987","v":"1987"},{"n":"1986","v":"1986"},{"n":"1985","v":"1985"},{"n":"1984","v":"1984"},{"n":"1983","v":"1983"},{"n":"1982","v":"1982"},{"n":"1981","v":"1981"},{"n":"1980","v":"1980"},{"n":"1979","v":"1979"},{"n":"1978","v":"1978"},{"n":"1977","v":"1977"},{"n":"1976","v":"1976"},{"n":"1975","v":"1975"},{"n":"1974","v":"1974"},{"n":"1973","v":"1973"},{"n":"1972","v":"1972"},{"n":"1971","v":"1971"},{"n":"1970","v":"1970"},{"n":"1969","v":"1969"},{"n":"1968","v":"1968"},{"n":"1967","v":"1967"},{"n":"1966","v":"1966"},{"n":"1965","v":"1965"},{"n":"1964","v":"1964"},{"n":"1963","v":"1963"},{"n":"1962","v":"1962"},{"n":"1961","v":"1961"},{"n":"1960","v":"1960"}]},{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
		"26":[{"key":"area","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"大陆"},{"n":"香港","v":"香港"},{"n":"台湾","v":"台湾"},{"n":"美国","v":"美国"},{"n":"韩国","v":"韩国"},{"n":"日本","v":"日本"},{"n":"泰国","v":"泰国"},{"n":"新加坡","v":"新加坡"},{"n":"马来西亚","v":"马来西亚"},{"n":"印度","v":"印度"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"加拿大","v":"加拿大"},{"n":"西班牙","v":"西班牙"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2007","v":"2007"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"},{"n":"1999","v":"1999"},{"n":"1998","v":"1998"},{"n":"1997","v":"1997"},{"n":"1996","v":"1996"},{"n":"1995","v":"1995"},{"n":"1994","v":"1994"},{"n":"1993","v":"1993"},{"n":"1992","v":"1992"},{"n":"1991","v":"1991"},{"n":"1990","v":"1990"},{"n":"1989","v":"1989"},{"n":"1988","v":"1988"},{"n":"1987","v":"1987"},{"n":"1986","v":"1986"},{"n":"1985","v":"1985"},{"n":"1984","v":"1984"},{"n":"1983","v":"1983"},{"n":"1982","v":"1982"},{"n":"1981","v":"1981"},{"n":"1980","v":"1980"},{"n":"1979","v":"1979"},{"n":"1978","v":"1978"},{"n":"1977","v":"1977"},{"n":"1976","v":"1976"},{"n":"1975","v":"1975"},{"n":"1974","v":"1974"},{"n":"1973","v":"1973"},{"n":"1972","v":"1972"},{"n":"1971","v":"1971"},{"n":"1970","v":"1970"},{"n":"1969","v":"1969"},{"n":"1968","v":"1968"},{"n":"1967","v":"1967"},{"n":"1966","v":"1966"},{"n":"1965","v":"1965"},{"n":"1964","v":"1964"},{"n":"1963","v":"1963"},{"n":"1962","v":"1962"},{"n":"1961","v":"1961"},{"n":"1960","v":"1960"}]},{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}]
	},
	filter_def:{
		1:{cateId:'1'},
		2:{cateId:'2'},
		3:{cateId:'3'},
		4:{cateId:'4'},
		26:{cateId:'26'}
	},
	searchUrl:'/index.php?m=vod-search&wd=**',
	searchable:2,//是否启用全局搜索,
	headers:{//网站的请求头,完整支持所有的,常带ua和cookies
		'User-Agent': 'MOBILE_UA',
	},
	// class_parse: '#topnav li:lt(4);a&&Text;a&&href;.*/(.*?).html',
    class_name:'电影&连续剧&综艺&动漫&短剧',//静态分类名称拼接
    class_url:'1&2&3&4&26',//静态分类标识拼接
	play_parse: true,
	lazy:`
	let nmjx_url="$nmjx_url";
	var _0xodE='jsjiami.com.v7';const _0x470a6f=_0x5b8d;(function(_0x1ab653,_0x330322,_0x1a8968,_0x487b97,_0x4d7fc1,_0x434710,_0x5deb0e){return _0x1ab653=_0x1ab653>>0x6,_0x434710='hs',_0x5deb0e='hs',function(_0x2eb8fb,_0x2dc311,_0x2d713d,_0x72ea40,_0x3064cb){const _0x44b0d2=_0x5b8d;_0x72ea40='tfi',_0x434710=_0x72ea40+_0x434710,_0x3064cb='up',_0x5deb0e+=_0x3064cb,_0x434710=_0x2d713d(_0x434710),_0x5deb0e=_0x2d713d(_0x5deb0e),_0x2d713d=0x0;const _0x561c15=_0x2eb8fb();while(!![]&&--_0x487b97+_0x2dc311){try{_0x72ea40=-parseInt(_0x44b0d2(0x8f,'yRLt'))/0x1+parseInt(_0x44b0d2(0x7d,'H%rj'))/0x2*(parseInt(_0x44b0d2(0x96,'XRFC'))/0x3)+parseInt(_0x44b0d2(0x8a,'[eKj'))/0x4+-parseInt(_0x44b0d2(0x77,'pjSM'))/0x5*(-parseInt(_0x44b0d2(0x94,'U*$J'))/0x6)+parseInt(_0x44b0d2(0x7b,'qy]*'))/0x7*(parseInt(_0x44b0d2(0x95,'ddmn'))/0x8)+parseInt(_0x44b0d2(0x86,'Iq*x'))/0x9*(-parseInt(_0x44b0d2(0x87,'Y5BJ'))/0xa)+parseInt(_0x44b0d2(0x73,'XRFC'))/0xb*(-parseInt(_0x44b0d2(0x92,'*k!u'))/0xc);}catch(_0xd4b26d){_0x72ea40=_0x2d713d;}finally{_0x3064cb=_0x561c15[_0x434710]();if(_0x1ab653<=_0x487b97)_0x2d713d?_0x4d7fc1?_0x72ea40=_0x3064cb:_0x4d7fc1=_0x3064cb:_0x2d713d=_0x3064cb;else{if(_0x2d713d==_0x4d7fc1['replace'](/[yFYqDnKXLukpUxGJNW=]/g,'')){if(_0x72ea40===_0x2dc311){_0x561c15['un'+_0x434710](_0x3064cb);break;}_0x561c15[_0x5deb0e](_0x3064cb);}}}}}(_0x1a8968,_0x330322,function(_0x270684,_0x1fb509,_0x4fecfd,_0x5dd048,_0x584c47,_0x176f94,_0x103483){return _0x1fb509='\x73\x70\x6c\x69\x74',_0x270684=arguments[0x0],_0x270684=_0x270684[_0x1fb509](''),_0x4fecfd='\x72\x65\x76\x65\x72\x73\x65',_0x270684=_0x270684[_0x4fecfd]('\x76'),_0x5dd048='\x6a\x6f\x69\x6e',(0x1638b1,_0x270684[_0x5dd048](''));});}(0x3300,0x30e88,_0x3795,0xce),_0x3795)&&(_0xodE=0x3199);pdfh=jsp['pdfh'],pdfa=jsp['pdfa'];let html=request(input),mac_url=html[_0x470a6f(0x8d,'XRFC')](/mac_url='(.*?)';/)[0x1],mac_from=html['match'](/mac_from='(.*?)'/)[0x1];log('flag:'+flag+_0x470a6f(0x72,'eEwD')+mac_from);let is_sniffer=/^线路/[_0x470a6f(0x7e,'pjSM')](flag)||/one|zhou/[_0x470a6f(0x88,'ddmn')](mac_from),index=parseInt(input[_0x470a6f(0x6f,'@u]Y')](/num-(\\d+)/)[0x1])-0x1,playUrls=mac_url[_0x470a6f(0x8e,'ytDW')]('#'),playUrl=playUrls[index][_0x470a6f(0x89,'FjX^')]('$')[0x1];log(playUrl);let scripts=html['match'](/script src="(.*?)"/g),js_url='';for(let i=0x0;i<scripts[_0x470a6f(0x7f,'xf]%')];i++){let script=scripts[i][_0x470a6f(0x75,'VAUL')](/src="(.*?)"/)[0x1];if(!script[_0x470a6f(0x70,'lD]S')](_0x470a6f(0x74,'xf]%'))&&!script['includes'](_0x470a6f(0x93,'vCi)'))){js_url=urljoin(input,script);break;}else{if(script[_0x470a6f(0x91,'!#Cv')](_0x470a6f(0x79,'FjX^'))&&!script[_0x470a6f(0x71,'lD]S')]('config')){js_url=urljoin(input,script);break;}}}function _0x5b8d(_0xfb97a1,_0x342c26){const _0x3795aa=_0x3795();return _0x5b8d=function(_0x5b8d7b,_0x352294){_0x5b8d7b=_0x5b8d7b-0x6e;let _0x1794b4=_0x3795aa[_0x5b8d7b];if(_0x5b8d['AXshqi']===undefined){var _0x4e321c=function(_0x35b660){const _0x273289='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';let _0x54c565='',_0x74154='';for(let _0x4f2784=0x0,_0x20ca2d,_0x2070f5,_0x145f90=0x0;_0x2070f5=_0x35b660['charAt'](_0x145f90++);~_0x2070f5&&(_0x20ca2d=_0x4f2784%0x4?_0x20ca2d*0x40+_0x2070f5:_0x2070f5,_0x4f2784++%0x4)?_0x54c565+=String['fromCharCode'](0xff&_0x20ca2d>>(-0x2*_0x4f2784&0x6)):0x0){_0x2070f5=_0x273289['indexOf'](_0x2070f5);}for(let _0x168ee7=0x0,_0x142537=_0x54c565['length'];_0x168ee7<_0x142537;_0x168ee7++){_0x74154+='%'+('00'+_0x54c565['charCodeAt'](_0x168ee7)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x74154);};const _0x3c00bc=function(_0x41a412,_0x1aa495){let _0x41dd19=[],_0x549407=0x0,_0x5d4aaa,_0x166b95='';_0x41a412=_0x4e321c(_0x41a412);let _0x46f59c;for(_0x46f59c=0x0;_0x46f59c<0x100;_0x46f59c++){_0x41dd19[_0x46f59c]=_0x46f59c;}for(_0x46f59c=0x0;_0x46f59c<0x100;_0x46f59c++){_0x549407=(_0x549407+_0x41dd19[_0x46f59c]+_0x1aa495['charCodeAt'](_0x46f59c%_0x1aa495['length']))%0x100,_0x5d4aaa=_0x41dd19[_0x46f59c],_0x41dd19[_0x46f59c]=_0x41dd19[_0x549407],_0x41dd19[_0x549407]=_0x5d4aaa;}_0x46f59c=0x0,_0x549407=0x0;for(let _0x422905=0x0;_0x422905<_0x41a412['length'];_0x422905++){_0x46f59c=(_0x46f59c+0x1)%0x100,_0x549407=(_0x549407+_0x41dd19[_0x46f59c])%0x100,_0x5d4aaa=_0x41dd19[_0x46f59c],_0x41dd19[_0x46f59c]=_0x41dd19[_0x549407],_0x41dd19[_0x549407]=_0x5d4aaa,_0x166b95+=String['fromCharCode'](_0x41a412['charCodeAt'](_0x422905)^_0x41dd19[(_0x41dd19[_0x46f59c]+_0x41dd19[_0x549407])%0x100]);}return _0x166b95;};_0x5b8d['DrKbVN']=_0x3c00bc,_0xfb97a1=arguments,_0x5b8d['AXshqi']=!![];}const _0x28f1ba=_0x3795aa[0x0],_0x5a9cb3=_0x5b8d7b+_0x28f1ba,_0x1c342c=_0xfb97a1[_0x5a9cb3];return!_0x1c342c?(_0x5b8d['XAtfAM']===undefined&&(_0x5b8d['XAtfAM']=!![]),_0x1794b4=_0x5b8d['DrKbVN'](_0x1794b4,_0x352294),_0xfb97a1[_0x5a9cb3]=_0x1794b4):_0x1794b4=_0x1c342c,_0x1794b4;},_0x5b8d(_0xfb97a1,_0x342c26);}log('js_url:'+js_url),html=request(js_url);let jx_path=html['match'](/this.Path="(.*?)"/)[0x1];jx_path=urljoin(HOST,jx_path),log(_0x470a6f(0x76,'[TyW')+jx_path);let jx_js_url=jx_path+mac_from+'.js';log(_0x470a6f(0x7a,'fmxj')+js_url),html=request(jx_js_url);let jx_php_url=html[_0x470a6f(0x78,'PF61')](/src="(.*?)'/)[0x1];if(is_sniffer){html=request(nmjx_url+jx_php_url);let urls=JSON['parse'](html)[_0x470a6f(0x81,'xf]%')];log(urls),playUrl=urls[0x0]+playUrl;}else playUrl=jx_php_url+playUrl;log('解析播放地址:'+playUrl),html=req(playUrl,{'headers':{'User-Agent':MOBILE_UA}})[_0x470a6f(0x82,'Iq*x')];function _0x3795(){const _0x4141cc=(function(){return[_0xodE,'UjLqspjGiauWmkiyKN.KcWonmD.xYFvuyJ7yXDUn==','W5blCSkSCW','W7ZcMhJcShn3uCkwemkS','W6BcGNRcRNjGy8km','W45xWOlcJfRcSmk9bLZdOa','W6FcKK0QnCk0WQNcTW','W7pcJaP1','W5lcHHLiWOW','rG4ls8kBWPy2bq','W5ehlSkGW44NW7FdJclcPSoP','WR1id3Sa','ESkBWR1kW4bz','W4pcGt7dQ8o4WQdcQG','A8oGimk3WPJdKqFdPSoAWQr3Fwa'].concat((function(){return['WQbLW5OPWPnKW43cKfZcRWe','WPlcPLFcLSkSW4dcQCoUxLuSW5y','WPXxBCoL','W7FcNrbIW7tcVW','W5OiWRdcGeVcT8kJea','W7/cMqPK','WQhdKCkfhHFcG8kq','iMGKWOzS','W7pdJmkkW45RWOJdP1Dau8kax3O','r8k9yL7cTG','W7dcJCoywKxdNSoDsCkoASoBuMW','zCo5W6rwCq1pbq','CrJdKu0','ASkfWRXaW5S','W4hdVSo5WPznxSk8W57dNriRWQS'].concat((function(){return['huyZsSkvWQSxBa','W5KADwlcGYvC','WRVdGM4Ila','vZ3dLe/cSW','WQHLW5SVWPqMW7JcQ1lcNZNcJW','556i5A+C55I26zcyW5C','E8k6w2ddJYhcNmkZ','ECoBW5ztbSkgWOrLvqpcRmkH','cmkGieVdI8kf','gvCnW6f5sCohrW','prxdRu5AWPNcVW','W6xdONGKlSkeWP0','kCoXWOzFDv7dUX5vW6afW6ZdVq'];}()));}()));}());_0x3795=function(){return _0x4141cc;};return _0x3795();};let realUrl;is_sniffer?realUrl=html[_0x470a6f(0x85,'Jl2S')](/video src="(.*?)"/)[0x1]:realUrl=html[_0x470a6f(0x83,'rWWu')](/url='(.*?)'/)[0x1];log(_0x470a6f(0x90,'$z2[')+realUrl);realUrl&&(input={'parse':0x0,'url':realUrl});var version_ = 'jsjiami.com.v7';
	`,
	lazy2 : `
	// let location = JSON.parse(request('https://www.wzget.cn/02w9z',{withHeaders:true,redirect:0})).location;
	let location = JSON.parse(request('https://www.wzget.cn/02w9z',{withHeaders:true,redirect:null})).location;
	//let location = request('https://www.wzget.cn/02w9z',{withHeaders:true,redirect:0});
	log(location);`,
	lazy_old:`
	pdfh = jsp.pdfh;
	pdfa = jsp.pdfa;
	// log(input);
	let html=request(input);
	// log(html);
	let mac_url = html.match(/mac_url='(.*?)';/)[1];
	let mac_from = html.match(/mac_from='(.*?)'/)[1];
	log(mac_from);
	let index = parseInt(input.match(/num-(\\d+)/)[1])-1;
	let playUrls = mac_url.split('#');
	let playUrl = playUrls[index].split('$')[1];
	// log('index:'+index);
	// log(mac_url);
	log(playUrl);
	let jx_js_url = 'https://m.nmddd.com/player/'+mac_from+'.js';
	html = request(jx_js_url);
	// log(html);
	let jx_php_url = html.match(/src="(.*?)'/)[1];
	// log(jx_php_url);
	if(mac_from=='one'){
	// html = request('https://api.cnmcom.com/webcloud/nmm.php');
	html = request(jx_php_url);
	//log(html);
	let v7js = pdfa(html,'body&&script').find((it)=>{
		return pdfh(it,'body&&Html').includes('jsjiami.com');
	});
	// v7js = pdfh(v7js,'script&&Html').split('*/')[1];
	v7js = pdfh(v7js,'script&&Text') || pdfh(v7js,'script&&Html');
	v7js = v7js.replace(/debugger/g,'console.log("debugger")');
	log(v7js);
	// function playlist(obj){log(obj)};
	var window={location:{href:""},onload:function(){}};function URL(href){return{searchParams:{get:function(){return""}}}}var elements={WANG:{src:""}};var document={getElementById:function(id){return elements[id]}};
	function setInterval(){}
	eval(v7js+'\\nrule.playlist=playlist;');
	log(typeof(rule.playlist));
	let urls = [];
	let lines = pdfa(html, "body&&li").map(x => {
		let textContent = pdfh(x, "body&&Text");
		log(textContent);
		rule.playlist({
			textContent: textContent
		});
		urls.push(elements.WANG.src)
	});
	log(urls);
	playUrl = urls[0]+playUrl;
	}else{
	playUrl = jx_php_url+playUrl;
	}
	log(playUrl);
	html = request(playUrl);
	// log(html);
	let realUrl; 
	if(mac_from=='one'){
	realUrl = html.match(/video src="(.*?)"/)[1];
	}else{
	realUrl = html.match(/url='(.*?)'/)[1];
	}
	// log(realUrl);
	if(realUrl){
		input = {parse:0,url:realUrl};
	}
	`,

	limit:6,
	double: true, // 推荐内容是否双层定位
	推荐:'.globalPicList;.resize_list;*;*;*;*',
	一级:'.globalPicList li;.sTit&&Text;img:eq(-1)&&src;.sBottom--em&&Text;a&&href',
	二级:{
		"title":".title&&Text;.type-title&&Text",
		"img":".page-hd&&img&&src",
		"desc":".desc_item:eq(3)&&Text;.desc_item:eq(4)--span&&Text;;.desc_item:eq(1)--span&&Text;.desc_item:eq(2)--span&&Text",
		"content":".detail-con p&&Text",
		"tabs":".hd li",
		"lists":".numList:eq(#id) li"
	},
	搜索:'.ulPicTxt.clearfix li;*;img&&data-src;.sDes:eq(1)&&Text;*',

	// //是否启用辅助嗅探: 1,0
	// sniffer:1,
	// // 辅助嗅探规则js写法
	// isVideo:`js:
	// 	log(input);
	// 	if(/video\\/tos/.test(input)){
	// 		input = true
	// 	}else if(/\\.m3u8/.test(input)){
	// 		input = true
	// 	}else{
	// 		input = false
	// 	}
	// `,
}