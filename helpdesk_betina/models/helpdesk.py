# archivo helpdesk.py

from odoo import models, fields

class HelpdeskTicket(models.Model):
	_name = 'helpdesk.ticket'
	_description = 'Helpdesk Ticket'  #'nombre de como quieres que se muestr'

	name = fields.Char(
		string = 'Name',
		required=True
	)
	description = fields.Text(
		string = 'Description'
	)
	date = fields.Date (
		string = 'Date'
	)
	state = fields.Selection(
		[	('new', 'New'),
			('assigned', 'Assigned'),
			('progress', 'Progress'),
			('waiting', 'Waiting'),
			('done', 'Done'),
			('cancelled', 'Cancelled')
		],
		string='State',
		default='new'
	)
	dedicated_time = fields.Float(
		string='time'
	)
	assigned = fields.Boolean(
		string='Assigned',
		readonly=True
	) #Si quiero en un futuro cambiar el readonly a false, no vale con quitarlo. Hay que ponerlo a false. Si estuviera instalado ya de antes es necesario
	date_due = fields.Date(
		string='Date Due'
	)
	corrective_action = fields.Html(
		help='Detail of corrective action after this issue'
	)
	preventive_action = fields.Html(
		help='Detail of preventive action after this issue'
	)

	user_id = fields.Many2one(
		comodel_name='res.users',
		string='Assigned to')

	def set_assigned(self):
		self.ensure_one() #¿Que es ensure_one()?
		self.write({
			'assigned':True,
			'state':'assigned',
			'user_id':self.env.user.id #aqui estoy pasando el id int
		})

	def set_assigned_multi(self):
		for ticket in self:
			ticket.set_assigned()

	def set_progress(self):
		self.ensure_one()
		self.state = 'progress'

	def set_waiting(self):
		self.ensure_one()
		self.state = 'waiting'

	def set_done(self):
		self.ensure_one()
		self.state = 'done'

	def set_cancel(self):
		self.ensure_one()
		self.state = 'cancel'

#Vamos a hacer un boton que cambie el valor del assigned de false a true
# def sset_assigned(self,env,cr,uid,ids,context) Esto seria la cabecera del metodo en versiones anteriores
#def set_assigned(self):
#	self.ensure_one() #¿Que es ensure_one()?
#	self.assigned = True

# si self = helpdesk.ticket(34) Esto funciona
# si self = helpdesk.ticket(34,56) Esto no funciona xq es un recordset.
# Habría que hacerlo asi, hay que recorrer los ticket y a cada uno asignarle el true al campo assigned.
# Ver ejemplo:
