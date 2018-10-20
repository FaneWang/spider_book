from bs4 import BeautifulSoup
import re

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,"lxml")
# print(soup.find_all(name="ul")[0])
# print(soup.find_all(attrs={"id":"list-1"}))
# print(soup.find_all(id="list-1"))
# print(soup.find_all(class_="element"))
# print(soup.find_all(text=re.compile('Foo')))
print(soup.find(class_="element").find_parents(name="div"))
print(soup.find_parents(class_="element"))