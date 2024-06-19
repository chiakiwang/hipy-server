#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import base64
from urllib.parse import unquote

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "py橙汁"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"电影":"1",
			"电视剧":"2",
			"综艺":"3",
			"动漫":"4",
			"纪录片":"5",
			"体育":"35"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})

		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']	
		return result
	def homeVideoContent(self):
		result = {
		    'list': []
		}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		if 'id' not in extend.keys():
			extend['id'] = tid
		extend['page'] = pg
		filterParams = ["id", "", "by", "class", "", "", "", "", "page", "", "", "year"]
		params = ["", "", "", "", "", "", "", "", "", "", "", ""]
		for idx in range(len(filterParams)):
			fp = filterParams[idx]
			if fp in extend.keys():
				params[idx] = extend[fp]
		suffix = '-'.join(params)
		url = 'https://www.orangek.cn/show/{0}.html'.format(suffix)
		rsp = self.fetch(url, headers=self.header)
		root = self.html(self.cleanText(rsp.text))
		aList = root.xpath("//div[@class='module']/a")
		videos = []
		for a in aList:
			name = a.xpath("./@title")[0]
			pic = a.xpath(".//img/@data-original")[0]
			if not pic.startswith('https'):
			    pic = 'https://www.orangek.cn' + pic
			remark = a.xpath("./div[1]/div[1]/text()")[0]
			sid = a.xpath("./@href")[0]
			sid = self.regStr(sid,"/detail/(\\S+).html")
			videos.append({
				"vod_id":sid,
				"vod_name":name,
				"vod_pic":pic,
				"vod_remarks":remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def detailContent(self,array):
		tid = array[0]
		url = 'https://www.orangek.cn/detail/{0}.html'.format(tid)
		rsp = self.fetch(url)
		root = self.html(self.cleanText(rsp.text))
		node = root.xpath("//div[@class='content']")[0]
		pic = node.xpath("//div[@class='module-main']//div[@class='module-item-pic']/img/@data-original")[0]
		title = node.xpath("//div[@class='module-main']//div[@class='module-item-pic']/img/@alt")[0]
		detail = node.xpath("//div[@class='module-info-introduction-content show-desc']/p/text()")[0]

		vod = {
			"vod_id":tid,
			"vod_name":title,
			"vod_pic":pic,
			"type_name":"",
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":"",
			"vod_actor":"",
			"vod_director":"",
			"vod_content": detail
		}

		infoArray = node.xpath("//div[@class='module-main']//div[@class='module-info-item']")
		for info in infoArray:
			content = info.xpath('string(.)')
			if content.startswith('类型'):
				vod['type_name'] = content.replace('类型：','')
			if content.startswith('年份'):
			 	vod['vod_year'] = content
			if content.startswith('地区'):
				vod['vod_area'] = content
			if content.startswith('更新'):
			 	vod['vod_remarks'] = content.replace('\n','').replace('\t','')
			if content.startswith('主演'):
				vod['vod_actor'] = content.replace('\n','').replace('\t','').replace('主演：','').replace('演员：','')
			if content.startswith('导演'):
				vod['vod_director'] = content.replace('\n','').replace('\t','').replace('导演：','')
			if content.startswith('简介'):
				vod['vod_content'] = content.replace('\n','').replace('\t','').replace('简介：','')

		vod_play_from = '$$$'
		playFrom = []
		vodHeader = root.xpath("//div[@id='y-playList']/div/span/text()")
		for v in vodHeader:
			playFrom.append(v)
		vod_play_from = vod_play_from.join(playFrom)
		
		vod_play_url = '$$$'
		host = 'https://www.orangek.cn'
		playList = []
		vodList = root.xpath("//div[contains(@class,'module-play-list-content')]")
		for vl in vodList:
			vodItems = []
			aList = vl.xpath('./a')
			for tA in aList:
				href = tA.xpath('./@href')[0]
				name = tA.xpath('./span/text()')[0]
				vodItems.append(name + "$" + host + href)
			joinStr = '#'
			joinStr = joinStr.join(vodItems)
			playList.append(joinStr)
		vod_play_url = vod_play_url.join(playList)

		vod['vod_play_from'] = vod_play_from
		vod['vod_play_url'] = vod_play_url

		result = {
			'list':[
				vod
			]
		}
		return result

	def searchContent(self,key,quick):
		url = ''.format(key)
		rsp = self.fetch(url)
		root = self.html(rsp.text)
		aList = root.xpath("//ul[@class='stui-vodlist__media col-pd clearfix']/li/div[1]/a")
		videos = []
		for a in aList:
			name = a.xpath('./@title')[0]
			pic = a.xpath('./@data-original')[0]
			mark = a.xpath("./span[@class='pic-text text-right']/text()")[0]
			sid = a.xpath("./@href")[0]
			sid = self.regStr(sid,"/detail/(\\S+).html")
			videos.append({
				"vod_id":sid,
				"vod_name":name,
				"vod_pic":pic,
				"vod_remarks":mark
			})

		result = {
			'list':videos
		}
		return result

	config = {
		"player": {"languang":{"show":"OR(自建)","des":"","ps":"1","parse":"https://player.123tv.icu/player/ec.php?code=qw&if=1&url="},"qq":{"show":"腾讯视频","des":"https://jx.777jiexi.com/player/?url=","ps":"1","parse":"https://jx.xmflv.com/?url="},"qiyi":{"show":"爱奇艺","des":"https://jx.yangtu.top/?url=","ps":"1","parse":"https://jx.yparse.com/index.php?url="},"youku":{"show":"优酷","des":"","ps":"1","parse":"http://119.91.123.253:2345/Api/yun.php?url="},"mgtv":{"show":"芒果","des":"","ps":"1","parse":"https://jx.xmflv.com/?url="},"bilibili":{"show":"哔哩哔哩","des":"","ps":"1","parse":"https://jx.xmflv.com/?url="},"ikm3u8":{"show":"iK","des":"ikun","ps":"1","parse":"https://p.orangek.org/player/ec.php?code=qw&if=1&url="},"ffm3u8":{"show":"FF","des":"非凡","ps":"1","parse":"https://p.orangek.org/player/ec.php?code=qw&if=1&url="},"lzm3u8":{"show":"LZ","des":"量子","ps":"1","parse":"https://p.orangek.org/player/ec.php?code=qw&if=1&url="},"snm3u8":{"show":"SO","des":"索尼","ps":"1","parse":"https://p.orangek.org/player/ec.php?code=qw&if=1&url="}},
		"filter": {"1": [{"key": "class", "name": "剧情", "value": [{"n": "全部", "v": ""}, {"n": "喜剧", "v": "喜剧"}, {"n": "爱情", "v": "爱情"}, {"n": "恐怖", "v": "恐怖"}, {"n": "动作", "v": "动作"}, {"n": "科幻", "v": "科幻"}, {"n": "剧情", "v": "剧情"}, {"n": "战争", "v": "战争"}, {"n": "警匪", "v": "警匪"}, {"n": "犯罪", "v": "犯罪"}, {"n": "动画", "v": "动画"}, {"n": "奇幻", "v": "奇幻"}, {"n": "冒险", "v": "冒险"}, {"n": "恐怖", "v": "恐怖"}, {"n": "悬疑", "v": "悬疑"}, {"n": "惊悚", "v": "惊悚"}, {"n": "青春", "v": "青春"}, {"n": "情色", "v": "情色"}]}, {"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"},{"n": "2023", "v": "2023"},{"n": "2022", "v": "2022"}, {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"}, {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"}, {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"}, {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"}, {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}, {"n": "2007", "v": "2007"}, {"n": "2006", "v": "2006"}, {"n": "2005", "v": "2005"}, {"n": "2004", "v": "2004"}, {"n": "2003", "v": "2003"}, {"n": "2002", "v": "2002"}, {"n": "2001", "v": "2001"}, {"n": "2000", "v": "2000"}]},{"key": "by", "name": "排序", "value": [{"n": "最新", "v": "time"}, {"n": "最热", "v": "hits"}, {"n": "评分", "v": "score"}]}], "2": [{"key":"class","name":"剧情","value":[{"n":"全部","v":""},{"n":"古装","v":"古装"},{"n":"战争","v":"战争"},{"n":"青春偶像","v":"青春偶像"},{"n":"喜剧","v":"喜剧"},{"n":"家庭","v":"家庭"},{"n":"犯罪","v":"犯罪"},{"n":"动作","v":"动作"},{"n":"奇幻","v":"奇幻"},{"n":"剧情","v":"剧情"},{"n":"历史","v":"历史"},{"n":"经典","v":"经典"},{"n":"乡村","v":"乡村"},{"n":"情景","v":"情景"},{"n":"商战","v":"商战"},{"n":"网剧","v":"网剧"},{"n":"其他","v":"其他"}]}, {"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"},{"n": "2023", "v": "2023"},{"n": "2022", "v": "2022"}, {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"}, {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"}, {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"}, {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"}, {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}, {"n": "2006", "v": "2006"}, {"n": "2005", "v": "2005"}, {"n": "2004", "v": "2004"}]},{"key": "by", "name": "排序", "value": [{"n": "最新", "v": "time"}, {"n": "最热", "v": "hits"}, {"n": "评分", "v": "score"}]}], "3": [  {"key":"class","name":"剧情","value":[{"n":"全部","v":""},{"n":"选秀","v":"选秀"},{"n":"情感","v":"情感"},{"n":"访谈","v":"访谈"},{"n":"播报","v":"播报"},{"n":"旅游","v":"旅游"},{"n":"音乐","v":"音乐"},{"n":"美食","v":"美食"},{"n":"纪实","v":"纪实"},{"n":"曲艺","v":"曲艺"},{"n":"生活","v":"生活"},{"n":"游戏互动","v":"游戏互动"},{"n":"财经","v":"财经"},{"n":"求职","v":"求职"}]},{"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"},{"n": "2023", "v": "2023"},{"n": "2022", "v": "2022"}, {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"}, {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"}, {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"}, {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"}, {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}, {"n": "2007", "v": "2007"}, {"n": "2006", "v": "2006"}, {"n": "2005", "v": "2005"}, {"n": "2004", "v": "2004"}, {"n": "2003", "v": "2003"}, {"n": "2002", "v": "2002"}, {"n": "2001", "v": "2001"}, {"n": "2000", "v": "2000"}]}, {"key": "by", "name": "排序", "value": [{"n": "最新", "v": "time"}, {"n": "最热", "v": "hits"}, {"n": "评分", "v": "score"}]}], "4": [{"key": "class", "name": "剧情", "value": [{"n": "全部", "v": ""}, {"n": "情感", "v": "情感"}, {"n": "科幻", "v": "科幻"}, {"n": "热血", "v": "热血"}, {"n": "推理", "v": " 推理"}, {"n": "搞笑", "v": "搞笑"}, {"n": "冒险", "v": "冒险"}, {"n": "萝莉", "v": "萝莉"}, {"n": "校园", "v": "校园"}, {"n": "动作", "v": "动作"}, {"n": "机战", "v": "机战"}, {"n": "运动", "v": "运动"}, {"n": "战争", "v": "战争"}, {"n": " 少年", "v": "少年"}, {"n": "少女", "v": "少女"}, {"n": "社会", "v": "社会"}, {"n": "原创", "v": "原创"}, {"n": "亲子", "v": "亲子"}, {"n": "益智", "v": "益智"}, {"n": "励志", "v": "励志"}, {"n": "其他", "v": "其他"}]},{"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"},{"n": "2023", "v": "2023"},{"n": "2022", "v": "2022"}, {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"}, {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"}, {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"}, {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"}, {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}, {"n": "2007", "v": "2007"}, {"n": "2006", "v": "2006"}, {"n": "2005", "v": "2005"}, {"n": "2004", "v": "2004"}, {"n": "2003", "v": "2003"}, {"n": "2002", "v": "2002"}, {"n": "2001", "v": "2001"}, {"n": "2000", "v": "2000"}]}, {"key": "by", "name": "排序", "value": [{"n": "最新", "v": "time"}, {"n": "最热", "v": "hits"}, {"n": "评分", "v": "score"}]}],"35":[{"key":"class","name":"类型","value":[{"n":"全部类型","v":""},{"n":"足球","v":"足球"},{"n":"篮球","v":"篮球"},{"n":"网球","v":"网球"},{"n":"斯诺克","v":"斯诺克"}]},{"key": "year", "name": "年份", "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"},{"n": "2023", "v": "2023"},{"n": "2022", "v": "2022"}, {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"}, {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"}, {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"}, {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"}, {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}, {"n": "2007", "v": "2007"}, {"n": "2006", "v": "2006"}, {"n": "2005", "v": "2005"}, {"n": "2004", "v": "2004"}, {"n": "2003", "v": "2003"}, {"n": "2002", "v": "2002"}, {"n": "2001", "v": "2001"}, {"n": "2000", "v": "2000"}]},{"key":"by","name":"排序","value":[{"n":"全部排序","v":""},{"n":"时间排序","v":"time"},{"n":"人气排序","v":"hits"},{"n":"评分排序","v":"score"}]}]}
	}
	header = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
	}
	def playerContent(self,flag,id,vipFlags):
		rsp = self.fetch(id,headers=self.header)
		root = self.html(self.cleanText(rsp.text))
		scripts = root.xpath("//script/text()")
		jo = {}
		result = {}
		for script in scripts:
			if(script.startswith("var player_")):
				target = script[script.index('{'):]
				jo = json.loads(target)
				break;
		parseUrl = ""
		playerConfig = self.config['player']		
		if jo['from'] in self.config['player']:
			playerConfig = self.config['player'][jo['from']]
			videoUrl = jo['url']
			playerUrl = playerConfig['parse']
			result["parse"] = playerConfig['ps']
			result["playUrl"] = playerUrl
			result["url"] = videoUrl
			result["header"] = ''
		return result
	
	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]