var rule =
   {
    title: '热播之家',
    host: 'https://rebozj.pro',
    url:'/show/fyfilter.html',
	filterable:1,//是否启用分类筛选,
	filter_url:'{{fl.cateId}}-{{fl.area}}-{{fl.by or "time"}}-{{fl.class}}-{{fl.lang}}-{{fl.letter}}---fypage---{{fl.year}}',
	filter: 'H4sIAAAAAAAAA+1ZX08bRxB/hk9R3TMPdwYbyDfoZ6jy4KZWG5VSCWglFCGRGFPbEGyixi6B8EfF2CnYHJCSYGPzZbx352/Rs3d3Zs5xpi52W7UxT/x+c7s3M7s7O7/zk/Gxz/w/wzIefPHE+Da2bDwwHkWXYp9/ZUwY89HvYj52NlPuRU3sb/jUj9G5H2KdZ+d9i0iUWvFSm/aBZaxMKDpdatb3FB1BOrcnUkVFTwPtJi+ceELRM0gXt8VNTdGzQDtPs85qTr/SxMlTRZzFQl+c5C/NakrzIWPlYduiAp2LLi4G4sRZPh5n71cq0DNWBXqmR4GeyVAAQomnnWevlE2BnmlRAOZMn7v13/ScEsC4Z2dubluPkwD8XH/R2nmj/ZSg5+ooAOMKP6FNgZ7LoQCMq1yLalmPkwBsW+sic6ltEoAtc+z9CusggbY1bw+9iq1sCoAv5ZNm41D7IoG2tQ6umjdZZVNA27y7rL9qyqYAzrnpJfdhzg6AcYU73EUKQD6fNlqvGjqfEtCtGl2IRYM7dc8Wm9V+d+pxsbWzrjMkAUR6suO8P9eRSoCZtZ2bBmS2A8DjxpbYrWuPJYAsXL1EmwKQhY0LtCkA4/IFZ+9Mj5MAV+QNjlMA/Gy8Q5sC6ItNfbED457bonqix0kA49YyfqZEUh8AxGQ93UzZTe3gkiqMJ/3Q2bjzh8Fh1xieSFw3a/rcKkDXfTkWXQiu+83bZq3e57qHzNCU4jr/En4S+UnKh5APUd5C3qK8ibxJeGsWeGuW8jPIz1B+GvlpykeQj1A+jHyY8hivReO1MF6LxmthvBaN18J4LRqvhfG2Lx+yUnPR+a8DK+Wdl73Sar8ndLfuP6/3gQTkxKBNATiFl8doUwBOTL4unufRjJicKWKWgJxFtClAzjexSUDOIolEArLbRSWOu70NaA6/XCYZ3HohqpkP0ufkr1v5t2qKpcf+o1Dqq1XH/llZvnm8tIgJPF8TSV3+Fh99vxBrv/XhhBEevOvBzSfrqlu79VJV3W/gVvbLql9Ag9YZmmw//QErOU7OWdEvsEGrNYROJvxnc/Rxx4RH5eq/U66ANzFek8ZrYrwmjdfEeE0ar4nxmjReE+M1abwmxuv/O4Ty+e8Vj/GxMSM0eP3AVfSrfrNaRNVAFl4WD2Ka6qocxITpdn5/J45zxBQZpvrhlAqnjLh+k1UqjHLgVAynjDjlwKkDThlx6o5TRpxi5JTffVUTq+A6WxG7kTYIXkbaFwkG7d/lTtXjJOirf++lT4anmtYT/vOwyh3QTzT3VVRc9ni19fEMsWorZ/uCRLw+0kMBj9TJ/+K6/0TVyV9SGZupf6RXMCYHbxUmh3l9exVb1F/qZZMAAmQ+mnFXyn0/mrkHsEcOyObhmgHoLgIfSLmPi9zHzL/34xtzjcjGTnssQbCzwy3eBuwlPCrMwyrM6sxODX5mMXmqvU+XnNtT/bIP2viANdy1TYLWSNdmCFqnh1krejgXoJgQAxTjcIBiwg5QXUIn8Byl+mrbudac+8GGa6Pv+QMRK624dn/tzj0taJsE/Uik3vWX/ZmDESTcLcCJMbZ6M0KNvScYEcf9VMMKp1pGJN7r90kAc2b33TPIsgT9tPd+uE4uj7G3AdgOj8QutDoSgC/xsne0qn2RAGLIbokKnEMJ+hFxwfPbddLiCS91CeveATDO3haFKz1OAvDzdN9Jg58SwJyXNWctqeeUAGxbJTerGyoFhngzczKXWy0ueyPJZIwk00gyDSiZxsdW/gAaMgDamyIAAA==',
	filter_def:{
		1:{cateId:'1'},
		2:{cateId:'2'},
		3:{cateId:'3'},
		4:{cateId:'4'},
		5:{cateId:'5'}
	},
    searchUrl: '/search/**----------fypage---.html',
    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
    filterable: 0,//是否启用分类筛选,
    headers: {
        'User-Agent': 'UC_UA',
        
    },
    class_parse: '.stui-header__menu li:lt(6);a&&Text;a&&href;.*/(.*?).html',
    play_parse: true,
    lazy: '',
    limit: 6,
    推荐: 'ul.stui-vodlist.clearfix;li;a&&title;.lazyload&&data-original;.pic-text&&Text;a&&href',
    double: true, // 推荐内容是否双层定位
    一级: '.stui-vodlist li;a&&title;a&&data-original;.pic-text&&Text;a&&href',
    二级: {
        "title": ".stui-content__detail .title&&Text;.stui-content__detail p:eq(-2)&&Text",
        "img": ".stui-content__thumb .lazyload&&data-original",
        "desc": ".stui-content__detail p:eq(0)&&Text;.stui-content__detail p:eq(1)&&Text;.stui-content__detail p:eq(2)&&Text",
        "content": ".detail&&Text",
        "tabs": ".nav.nav-tabs li",
        "lists": ".stui-content__playlist:eq(#id) li"
    },
    搜索: 'ul.stui-vodlist&&li;a&&title;.lazyload&&data-original;.pic-text&&Text;a&&href;.text-right&&Text',
}