var rule = {
  title: '可可影视',
  host: 'https://keke5.app',
  // url: '/show/fyclass-----2-fypage.html',
  url: '/show/fyclass-fyfilter-fypage.html',
  filter_url:'{{fl.类型}}-{{fl.地区}}-{{fl.语言}}-{{fl.年份}}-{{fl.排序}}',
  searchUrl: '/search?k=**&page=fypage',
  searchable: 2,
  quickSearch: 0,
  filterable: 1,
  headers: {
    'User-Agent': 'MOBILE_UA',
  },
  class_parse: '#nav-swiper&&.nav-swiper-slide;a&&Text;a&&href;/(\\w+).html',
  cate_exclude:'Netflix|今日更新|专题列表|排行榜',
  tab_order:['超清', '蓝光', '极速蓝光'],
  play_parse: true,
  lazy: '',
  limit: 20,
  推荐: '.section-box:eq(2)&&.module-box-inner&&.module-item;*;*;*;*',
  double: false,
  一级: '.module-box-inner&&.module-item;.v-item-title:eq(-1)&&Text;img&&data-original;.v-item-bottom&&span&&Text;a&&href',
  二级: {
    title: '.detail-title&&Text;.detail-tags&&a:eq(-2)&&Text',
    img: '.detail-pic&&img&&data-original',
    desc: '.detail-info-row-main:eq(-2)&&Text;.detail-tags&&a&&Text;.detail-tags&&a:eq(1)&&Text;.detail-info-row-main:eq(1)&&Text;.detail-info-row-main&&Text',
    content: '.detail-desc&&Text',
    tabs: '.source-item-label',
    lists: '.episode-list:eq(#id) a',
  },
  搜索: '.search-result-list&&a;.title&&Text;*;.search-result-item-header&&Text;a&&href;.desc&&Text',
  图片替换:'https://keke5.app=>https://vres.a357899.cn',
  filter:'H4sIAAAAAAAAA+2Zz08bRxTH/5c9c7ANanFuPbRSpSqX9lCpiiIOrhQ1pYemVasIyWAbjCHYIMfEsQOkYDAJ/gFBjllj+5/ZmV3/F931m/dmjNqXbUMjVfEF8XnfmdnZ2bfzvrN+bEWtO989tn5I/G7dsdzzntjbsGasxYUfEyb/uvDwl8S44aIfFpn6KFUPwj5YSzMQvZt49P3DB7+p8N3Pv/niqy+/JVWsn8hURokKSCtV/QhqAKTl6k6/ihoAam72XI+pADW5XJDJktIUkJbKyZXnqAHQmLmW23+FYwKQdrItrnqoAdCYK2duaRvHBKB7qK3pfgpIW90ZlU9RA6Axs88cex3HBKB+W6sif4H9AEjLH3mHtNYApDU7wm6gBoCac33gNdtKU0BzaRw7gwOcC4DWNr3sHmljoDXbb7jra7hmAMazdYs9/WwDIC09dF/XUANAzVveFFVbaQqW7gUqpLGotsWmrdOYOEwai6OTUXkVF6HbEJW+CmGL0XFZdlsTLVRIP4C2vBpMjgEhWpbBlh/EZQGg5dytyeoZLicAXXv/VPdTQMuyca41BTTmm6daU0CzHbzVmgLSnrSFfYwagB6zbY7ZNvs53asR9VNA9769JzJdvHcAut7bS682xOsB6HQ5kBtD/2FQxiDTVYdpt78rS/RwiGnO6bzfQWTxjdNMLVpFH+VuB1sQG9uOaBdFBt8UzfQkakM376d6GR8GMV1l8Aau69i0EZkhuudMx+nhNqbATHWv1fDqSZ3qxKFSvdL32+PgAHSTF0daU2AkmtYUGMmrNQVG8mpNgZGgRj+AsIsgri6dXt9435HDLEIsEptTsfG/RnxWx2fNeEzHY2Y8quNRMx7R8QjFo5HxNA9Ji0bu+3/i1CBys0EkaBDRDeKTDaLxeOS+/0c3mL/ZYD5oMK8byMql3MVXIdA+jU8srNzaEXZeLyzx5MK6vWtRyN5cWFlNyhK+IzEz7KbwQetl9VppkcVtdy6Yxb0Zv9d/400UhfEmnMfgfAvnI1ivwNVuxgtxdZ3zO5w3CeoS3Z+CMF6I8yacpwnqGV1PQRj/4e94+hkpCOMDOe81SvVFdwXnAnDb/oPC1i37D84l/FvnwTkIznmw7uKdPonzGJw3mdbNad38eOvm7Aeqm7m6TC7L69cTpzgdCnX2586A3HcBZu9m6yRX77iaxpxHZWHPPaN6DhDKPzA1mzs3+3ngvUyiBkBaJSfLWFQUhPEdbi9vHMoAqN/BS1GhPQYAtc8WH/hpBRL8T5k5LPhrj7sdAB3U7AvRKODGD0C73Ysd+QxXWoGu5hv+GlI1H0MYh/CXDui2vhhwVfPd1fz9vhW8nxeYfjGYfjGYOh+Tp87n/+185m7L+bj2K9F/itkMQFp137Ft94RKMDHNrdnWvRWQlj4X+UPdW3Mov8R992f8Evdt3610xSHtTQA029yKW2niVAF0xf377/6cP+OcwdeJhZ9/WlSaApon99sM45c4fybLz51r2lABpr8lTKvItIp8xFXkk39eRXTYnMsouer9QZkHQJlerIomnlcU0KzKBf90g5kOQP1Oh14nh/0A6HprT9ziPl4PIExVYX/ZZs5V7OmWOYWzv2xzJ/tMRzRT+o0M4EMnjp8hS38CUp0s8TchAAA=',
  一级f:`js:
    let urls = [
    'https://keke5.app/show/1-----1-1.html',
    'https://keke5.app/show/2-----1-1.html',
    'https://keke5.app/show/3-----1-1.html',
    'https://keke5.app/show/4-----1-1.html',
    'https://keke5.app/show/6-----1-1.html',
    ];
    let filters = {};
    pdfa = jsp.pdfa;
    pdfh = jsp.pdfh;
    for(let url of urls){
    let fclass = url.match(/show\\/(\\d+)-/)[1];
    console.log(fclass);
    let html = request(url);
    let tabs = pdfa(html, '.filter-row');
    let data = [];
    for (let tab of tabs) {
        let title = pdfh(tab, 'strong&&Text').replace(':','');
        let lis = pdfa(tab, 'a');
        let _map = {key: title, name: title};
        let value = [];
        for (let li of lis) {
            let n = pdfh(li, 'a&&Text').trim();
            let v=n;
            if(/全部|地区|综合|类型/.test(n)){
                v = '';
            }else{
                v = pdfh(li,'a&&href');
                try {
                    v = v.match(/-(.*?)1-1\.html/)[1].replace(/-/g,'');
                }catch (e) {
                    v = v.match(/-(.*?)-1\.html/)[1].replace(/-/g,'');
                }
                v = decodeURIComponent(v);
            }
            value.push({
                'n': n, 'v': v
            });
        }
        _map['value'] = value;
        data.push(_map);
    }
    filters[fclass] = data;
    }
    VODS = [filters];
    console.log(gzip(JSON.stringify(filters)));
    `,
}