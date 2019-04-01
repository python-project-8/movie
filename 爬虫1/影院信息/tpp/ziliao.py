from lxml import etree

tree = etree.parse('tppyuanma.html')

ret = tree.xpath("//ul/li/div/div/h4")
print(ret)
