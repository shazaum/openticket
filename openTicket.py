#!/usr/bin/env python

import pycurl

def openTicket(): 
	postTicket = '{"ticket":{"subject":"Assunto", "comment": { "value":"Descricao do chamado/ticket" }}}'
	c = pycurl.Curl()
	c.setopt(c.URL, 'https://domain.zendesk.com/api/v2/tickets.json')
	c.setopt(c.POSTFIELDS, postTicket)
	c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
	c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
	c.setopt(c.USERPWD, 'user@domain.com:minhasenha')
	c.perform()
openTicket()
