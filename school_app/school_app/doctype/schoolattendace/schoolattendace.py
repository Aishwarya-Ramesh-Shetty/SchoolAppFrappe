# Copyright (c) 2026, Aishwarya Shetty and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SchoolAttendace(Document):
	def validate(self):
		if frappe.db.exists("SchoolAttendace", {
			"employee": self.employee,
			"date": self.date,
			"name": ("!=", self.name)
		}):
			frappe.throw(f"Attendance for Employee {self.employee} on {self.date} already exists!")
