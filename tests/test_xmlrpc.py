# $Id: test_xmlrpc.py,v 1.1 2001/08/20 10:41:02 kjetilja Exp $

## PycURL module
import pycurl

# Header fields passed in request
xmlrpc_header = [
    "User-Agent: pycurl xmlrpc test", "Content-Type: text/xml"
    ]

# XML-RPC request body
xmlrpc_req = """
<?xml version='1.0'?>
<methodCall>
<methodName>examples.getStateName</methodName>
<params>
<param>
<value><int>5</int></value>
</param>
</params>
</methodCall>
"""

# Engage
c = pycurl.init()
c.setopt(pycurl.URL, 'http://betty.userland.com/RPC2')
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.HTTPHEADER, xmlrpc_header)
c.setopt(pycurl.POSTFIELDS, xmlrpc_req)
print 'Response from http://betty.userland.com/\n'
c.perform()
c.cleanup()