var rule = {
  类型:'听书',
  title:'海洋听书网',
  host:'http://m.ychy.org/category.html',
  url:'http://m.ychy.org/list/fyclass-fypage.html',
  编码:'GB18030',
  searchUrl:'http://m.ychy.org/search.asp?page=fypage&searchword=**&searchtype=-1',
  searchable:2,
  quickSearch:0,
  filterable:1,
  filter:'',
  filter_url:'',
  filter_def:{},
  headers:{
      'User-Agent':'MOBILE_UA',
  },
  timeout:5000,
  class_parse:'.fleiList dt;a&&Text;a&&href;(\\d+)',
  cate_exclude:'',
  play_parse:true,
  lazy:$js.toString(()=>{
    input = {parse:1,url:input,js:''};
  }),
  double:true,
  一级:'.list-ul li;span&&Text;img&&src;p&&Text;a&&href',
  二级:{
    title:'h2&&Text',
    img:'.bookimg&&img&&src',
    desc:'.bookinfo&&div:eq(4)&&Text;.bookinfo&&div:eq(2)&&Text;.bookinfo&&div:eq(1)&&Text',
    content:'.book_intro&&Text',
    tabs:'.bookbutton',
    lists:'.compress&&li',
    tab_text:'body&&Text',
    list_text:'body&&Text',
    list_url:'a&&href',
  },
  
  搜索: $js.toString(()=>{
        let d = [];
        pdfh = jsp.pdfh;pdfa = jsp.pdfa;pd = jsp.pd;
        let html = request(input);
        var list = pdfa(html, '.book_slist&&.bookbox');
        list.forEach(function(it) {
            d.push({
                title: pdfh(it, 'h4&&Text'),
                desc: pdfh(it, '.update&&Text'),
                pic_url: pd(it, 'img&&orgsrc'),
                url: 'http://m.ychy.org/book/' + pdfh(it, '.bookbox&&bookid') + '.html'
            })
        });
        setResult(d); 
  }),
  
}

