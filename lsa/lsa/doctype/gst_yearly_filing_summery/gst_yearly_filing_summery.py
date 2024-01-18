# Copyright (c) 2023, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GstYearlyFilingSummery(Document):
	pass

	
@frappe.whitelist()
def create_gst_yearly_filing_manually(gst_yearly_summary_report,gstfile,
									  company_name,customer_id,customer_status,executive_name,gst_type):
	try:
		existing_doc=frappe.get_all("Gst Yearly Filing Summery",
                                    filters={"gst_file_id":gstfile})
		if not(existing_doc):
			new_doc = frappe.new_doc('Gst Yearly Filing Summery')

			new_doc.gst_yearly_summery_report_id = gst_yearly_summary_report
			new_doc.fy = gst_yearly_summary_report
			new_doc.cid = customer_id
			new_doc.gst_file_id = gstfile
			new_doc.customer_status = customer_status
			new_doc.gstin = gstfile
			new_doc.gst_executive = executive_name
			new_doc.gst_type = gst_type
			new_doc.created_manually=1

			new_doc.save()
			return "Gst Yearly Filing Summery created successfully."
		else:
			return "Gst Yearly Filing Summery you are trying to create already exists"
	except Exception as e:
		print(e)
		return {"status":"Failed","dvalues":e}

@frappe.whitelist()
def checking_user_authentication(user_email):
	try:
		status=False
		user_roles = frappe.get_all('Has Role', filters={'parent': user_email}, fields=['role'])

		# Extract roles from the result
		roles = [role.get('role') for role in user_roles]
		doc_perm_records = frappe.get_all('DocPerm',
									 filters = {'parent': 'Gst Yearly Filing Summery','create': 1},
									 fields=["role"])
		for doc_perm_record in doc_perm_records:
			if  doc_perm_record.role in roles:
				status=True
				break
		return {"status":status,"value":[roles,doc_perm_records]}
		
	except Exception as e:
		print(e)
		return {"status":"Failed"}


	


