from xml.etree import cElementTree as ET
xmlstr = """
    <h>
	<page>
	  <title>Chapter 1</title>
	  <content>Welcome to Chapter 1</content>
	</page>
    </h>
	"""
root = ET.fromstring(xmlstr)
for page in list(root):
	    title = page.find('title').text
	    content = page.find('content').text
	    print('title: %s; content: %s' % (title, content))