
# Copyright (c) 2023, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

class Gstfile(Document):

	def before_insert(self):

		pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]\w{3}$'
		field_value = self.gst_number
		if not re.match(pattern,field_value):
			frappe.throw("Please Enter Valid GST Number")

	def on_update(self):
		gst_filling_data_s=frappe.get_all("Gst Filling Data",
                                    filters={"gstfile":self.name})
		print(gst_filling_data_s)
		for gst_filling_data in gst_filling_data_s:
			gst_filling_data_doc=frappe.get_doc("Gst Filling Data",gst_filling_data.name)
			gst_filling_data_doc.save()
			



