# Copyright (c) 2023, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class ITAssesseeFilingData(Document):
	def before_insert(doc):
          existing_doc = frappe.get_all(doc.doctype, filters={ 'ay': doc.ay,"it_assessee_file":doc.it_assessee_file })
          if existing_doc:
              frappe.throw(("The IT Assessee Filing Data  already exists."))



@frappe.whitelist()
def create_it_assessee_filing_data(yearly_report, current_form_name):
    try:
        existing_doc=frappe.get_all("IT Assessee Filing Data",
                                    filters={"it_assessee_file":current_form_name})
        if not(existing_doc):
            filing_data_doc = frappe.new_doc('IT Assessee Filing Data')
            filing_data_doc.ay = yearly_report
            filing_data_doc.it_assessee_file = current_form_name
            filing_data_doc.created_manually=1
            filing_data_doc.save()

            return "IT Assessee Filing Data created successfully."
        else:
            return "IT Assessee Filing Data you are trying to create already exists"
    except frappe.exceptions.ValidationError as e:
        frappe.msgprint(f"Validation Error: {e}")
        return False
    except Exception as e:
        frappe.msgprint(f"Error: {e}")
        return False

