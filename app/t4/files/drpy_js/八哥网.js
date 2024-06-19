var rule = {
  title:'八哥网',
  host:'https://www.bagehd.com/',
  编码:'GB18030',
  url:'/ltype/indexfyfilter_fypage.html[ltype/indexfyfilter.html]',
  searchUrl:'/search.asp?page=fypage&searchword=**&searchtype=-1',
  searchable:2,
  quickSearch:0,
  filterable:1,
  filter_url:'{{fl.tag}}',
  filter:{
        "movie":[{"key":"tag","name":"类型","value":[{"n":"动作片","v":"5"},{"n":"喜剧片","v":"6"},{"n":"爱情片","v":"7"},{"n":"科幻片","v":"8"},{"n":"恐怖片","v":"9"},{"n":"剧情片","v":"10"},{"n":"战争片","v":"11"},{"n":"人文片","v":"12"}]}]
        ,"ds":[{"key":"tag","name":"类型","value":[{"n":"国产剧","v":"13"},{"n":"香港剧","v":"14"},{"n":"台湾剧","v":"15"},{"n":"韩国剧","v":"27"},{"n":"印泰剧","v":"38"},{"n":"欧美剧","v":"29"},{"n":"海外剧","v":"30"},{"n":"日本剧","v":"28"}]}]
       , "zy":[{"key":"tag","name":"类型","value":[{"n":"动画片","v":"35"},{"n":"OVA剧场","v":"36"}]}]
        ,"dm":[{"key":"tag","name":"类型","value":[{"n":"综艺片","v":"31"},{"n":"纪录片","v":"32"},{"n":"音乐MV","v":"33"},{"n":"体育竞技","v":"34"},{"n":"搞笑短片","v":"39"}]}]
    },

  filter_def:{
		movie:{tag:'类型'},
		ds:{tag:'类型'},
        zy:{tag:'类型'},
        dm:{tag:'类型'},
	},
  headers:{
      'User-Agent':'MOBILE_UA',
  },
  class_name:'电影&电视剧&动漫&综艺',
  class_url:'movie&ds&zy&dm',
  timeout:5000,
  //class_parse:'div.AnavL a;a&&Text;a&&href;./(.*?)\.html',
  cate_exclude:'',
  play_parse:true,
  lazy:`
    if(/\\.m3u8$/.test(input)){
        input = {
            parse:0,
            url:getProxyUrl()+'&url='+input,
            jx:0
        }
    }
    `,
  double:true,
  //推荐:'列表1;列表2;标题;图片;描述;链接;详情',
  一级:'#list_con:eq(1)&&li;a:eq(1)&&title;img&&src;span:eq(1)&&Text;a&&href',
  二级:{
    title:'.moviedteail&&img&&alt;.moviedteail_list_short&&a&&title',
    img:'.moviedteail&&img&&src',
    desc:';.moviedteail li:eq(5)&&Text;.moviedteail li:eq(6)&&Text;.moviedteail li:eq(2)&&Text;.moviedteail li:eq(4)&&Text',
    content:'简介',
    tabs:'div.box_tt_tab h2',
    lists:'.diversityTV_list a',
    tab_text:'body&&Text',
    list_text:'body&&Text',
    list_url:'a&&href',
    list_url_prefix: '',
  },
  搜索:'#list_con li;*;*;*;*',
}