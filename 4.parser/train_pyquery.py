from pyquery import PyQuery as pq

html = '''
<div>
<ul id='id_test'>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
<li class="multi-item-0 multi-item-1"><a href="link6.html">six item</a></li>
<li class="item-0 multi-item-1" name="item"><a href="link6.html">seven item</a></li>
</ul>
</div>
'''

# doc = pq(html)
# print(doc('li'))

# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))

# doc = pq(html)
# print(doc('#id_test .item-0 a'))
# print(type(doc('#id_test .item-0 a')))

# doc = pq(html)
# items = doc('.item-inactive')
# print(items)
# node = items.find('a')
# print(node)

# doc = pq(html)
# item = doc('.item-0.multi-item-1')
# # item = doc('.multi-item-1')
# # item = doc('.item-0')
# print(item)

# doc = pq(html)
# lis = doc('li').items()
# for li in lis:
#     print(li, type(li))

# Get attr
doc = pq(html)
item = doc('.item-0.multi-item-1 a')
print(item.attr('href'))
print(item.attr.href)
print(item.text())
item = doc('.item-0.multi-item-1')
print(item.text())
print(item.html())