# Copyright (c) 2023, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ITAssesseeFileYearlyReport(Document):
	def on_submit(self):
            try:
                # Fetch records from Gstfile with filter gst_type = 'regular'
                it_assessee_file = frappe.get_all("IT Assessee File", filters={"enabled": 1}, fields=["name"])
                # print(it_assessee_file)

                # Create new records in GST Monthly Filing
                new_records = []
                for record in it_assessee_file:
                    new_record = frappe.get_doc({
                        "doctype": "IT Assessee Filing Data",
                        "it_assessee_file": record.name,
                        "ay": self.name,
                        # Set other fields as needed
                        # "some_other_field": "Some Value"
                    })

                    new_record.insert()
                    new_records.append(new_record.as_dict())

                frappe.msgprint("New Records Created in IT Assessee Filing Data!")

                return {"success": True}
            except Exception as e:
                frappe.log_error(frappe.get_traceback(), "Error in fetch_and_insert_records")
                return {"success": False, "error_message": str(e)}

