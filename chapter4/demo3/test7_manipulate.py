from pyquery import PyQuery as pq

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc = pq(html)
# li = doc(".item-0.active")
# print(li)
# li.removeClass("active")
# print(li)
# li.addClass("ccc")
# print(li)

# li = doc(".item-0.active")
# print(li)
# li.attr("name","fffffff")
# print(li)
# li.text("jjjjjjjjjj")
# print(li)
# li.html("<p>eeeeeeeeee</p>")
# print(li)

li = doc(".item-1")
print(li)
li.find("a").remove()
print(li)