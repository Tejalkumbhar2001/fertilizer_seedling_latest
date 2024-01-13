# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Blending(Document):
	
	@frappe.whitelist()
	def get_lot_info(self):
		if self.foundation_batch_id:
			
			doc = frappe.get_all("Seed Quality Inspection", 
							filters={"batch_id": self.foundation_batch_id},
							fields=["lot_number","lot_wt","check","procurement_no"],)
				
			if(doc):
				for d in doc:
					if not d.check :
						self.append('blending_child_table', {
													"lot_number":d.lot_number,
													"lot_weight":d.lot_wt,
													"procurement_no":d.procurement_no,
													'procurement_date': frappe.get_value("Seed Procurement",{'foundation_batch_id':self.foundation_batch_id,'procurement_no':d.procurement_no},'date')
												})
		
		self.calculate_child_table()	
			
	
	@frappe.whitelist()
	def changes_status(self):
		# frappe.msgprint('hiii') 
		name = frappe.get_all("Seed Quality Inspection", 
							filters={"batch_id":self.foundation_batch_id},
							fields=["name"])
		# frappe.msgprint(str(name)) 
		if(name):
			for n in name:
				frappe.db.set_value('Seed Quality Inspection', n, 'check', '1')
		
	def on_trash(self):
		self.uncheck_field()
		
	
	def uncheck_field(self):
		if self.foundation_batch_id:
			name_list = frappe.get_all("Seed Quality Inspection", 
								filters={"batch_id": self.foundation_batch_id},
								fields=["name", "check"])
			
			if(name_list):
				for item in name_list:
					if item.check:
						frappe.db.set_value('Seed Quality Inspection', item, 'check', '0')


	@frappe.whitelist()
	def calculate_child_table(self):		
		table = self.get('blending_child_table')
		total = 0
		
		for i in table:
			total += i.lot_weight
			# frappe.msgprint(str(total))
		self.total_weight = total
		# self.get_procurement_date()
		

	# @frappe.whitelist()
	# def get_procurement_date(self):
	# 	if self.foundation_batch_id:
	# 		pdate = frappe.get_all("Seed Procurement",
	# 						filters={'foundation_batch_id':self.foundation_batch_id},
	# 						fields=["date"])
	# 		# frappe.msgprint(str(pdate))
	# 		for pd in pdate:
	# 			self.append('blending_child_table',{
	# 				         "procurement_date":pd.date
	# 			})