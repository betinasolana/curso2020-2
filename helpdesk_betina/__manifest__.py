# Copyright 2020 HERGAR
# Betina Solana - b_solana@hergar.com
#
{
	"name": "Helpdesk Betina Solana", # este es el único campo obligatorio para que funcione
	"sumary": "Mi modulo",
	"version": "13.0.1.0.0",
	"category": "Helpdesk",
	"website": "",
	"author": "Betina",
	"maintainers": "[betinasolana]", # usuario de github
	"license":"AGPL-3",
	"application":True,
	"installable": True,
	"depends": [ "base"], #Aqui se indican los modulos que quiere que instale cuando instales este modulo
	"data": [
		'security/helpdesk_security.xml',
		'security/ir.model.access.csv',
		'views/helpdesk_ticket_views.xml'
	],
	"demo":[],
	"description": "" #Esta descripcion del modulo puede ser sustituido por un archivo fuera que se llama README.md
}
