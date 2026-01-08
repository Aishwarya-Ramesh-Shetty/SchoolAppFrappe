# Copyright (c) 2026, Aishwarya Shetty and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SchoolSalary(Document):
	def validate(self):
		self.total_payable = (self.basic_salary or 0) + (self.allowances or 0) - (self.deductions or 0)
