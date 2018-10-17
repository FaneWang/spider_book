import re
import json

def parseOnePage(html):
    pattern = re.compile(
        '<dd>.*?>(.*?)</i>.*?data-src="(.*?)".*?<a.*?title="(.*?)".*?</a>.*?"star">(.*?)</p>.*?>(.*?)</p>.*?<p.*?<i.*?>(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',
        re.S)
    # pattern = re.compile(
    #     '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' +
    #     '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' +
    #     '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>', re.S)
    # 该句不会匹配成功，因为没有匹配换行符，所以尽量不要再换行的位置使用精确匹配
    # pattern = re.compile('<dd><i.*?board-index.*?>(.*?)</i>', re.S)
    # pattern = re.compile('<dd>.*?>(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": item[2],
            "actor": item[3].strip()[3:] if len(item[3]) > 3 else "",
            "time": item[4].strip()[5:] if len(item[4]) > 5 else "",
            "score": item[5].strip() + item[6].strip()
        }

def writeToFile(content):
    with open("result.txt","a",encoding="utf-8") as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False) + "\n")


if __name__ == "__main__":
    html = '''<dd>
        <i class="board-index board-index-1">1</i>
        <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
            <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
            <img data-src="http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬"
                class="board-img" />
        </a>
        <div class="board-item-main">
            <div class="board-item-content">
                <div class="movie-item-info">
                    <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
                    <p class="star">
                        主演：张国荣,张丰毅,巩俐
                    </p>
                    <p class="releasetime">上映时间：1993-01-01</p>
                </div>
                <div class="movie-item-number score-num">
                    <p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>
                </div>
            </div>
        </div>
    </dd>'''

    parseOnePage(html)