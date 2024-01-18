import frappe
from frappe.model.document import Document

class GstFillingData(Document):
    def on_submit(self):
        # Get the gst_yearly_filling_summery_id from the current form
        gst_yearly_filling_summery_id = self.gst_yearly_filling_summery_id

        # Search for the Gst Yearly Filing Summery document
        gst_yearly_filing_summery = frappe.get_doc("Gst Yearly Filing Summery", {"name": gst_yearly_filling_summery_id})

        # Update sales_total_taxable
        self.update_field(gst_yearly_filing_summery, 'sales_total_taxable')

        # Update purchase_total_taxable
        self.update_field(gst_yearly_filing_summery, 'purchase_total_taxable')

        # Update tax_paid_amount
        self.update_field(gst_yearly_filing_summery, 'tax_paid_amount')

        # Update interest_paid_amount
        self.update_field(gst_yearly_filing_summery, 'interest_paid_amount')

        # Update penalty_paid_amount
        self.update_field(gst_yearly_filing_summery, 'penalty_paid_amount')

        # Save the changes
        gst_yearly_filing_summery.save()

    def on_cancel(self):
        # Get the gst_yearly_filling_summery_id from the current form
        gst_yearly_filling_summery_id = self.gst_yearly_filling_summery_id

        # Search for the Gst Yearly Filing Summery document
        gst_yearly_filing_summery = frappe.get_doc("Gst Yearly Filing Summery", {"name": gst_yearly_filling_summery_id})

        # Update sales_total_taxable
        self.update_field(gst_yearly_filing_summery, 'sales_total_taxable', subtract=True)

        # Update purchase_total_taxable
        self.update_field(gst_yearly_filing_summery, 'purchase_total_taxable', subtract=True)

        # Update tax_paid_amount
        self.update_field(gst_yearly_filing_summery, 'tax_paid_amount', subtract=True)

        # Update interest_paid_amount
        self.update_field(gst_yearly_filing_summery, 'interest_paid_amount', subtract=True)

        # Update penalty_paid_amount
        self.update_field(gst_yearly_filing_summery, 'penalty_paid_amount', subtract=True)

        # Save the changes
        gst_yearly_filing_summery.save()

    def update_field(self, gst_yearly_filing_summery, field_name, subtract=False):
        # Get the field value from the current form
        field_value = getattr(self, field_name)

        # Check if subtract flag is set
        if subtract:
            # Subtract the field value from the current value
            setattr(gst_yearly_filing_summery, field_name, getattr(gst_yearly_filing_summery, field_name) - field_value)
        else:
            # Increment the field by the current value
            setattr(gst_yearly_filing_summery, field_name, getattr(gst_yearly_filing_summery, field_name) + field_value)


@frappe.whitelist()
def create_gst_filing_data(gst_yearly_filling_summery_id,gstfile,gst_type,fy,gst_filing_data_report):
    try:
        existing_doc=frappe.get_all("Gst Filling Data",
                                    filters={"gst_yearly_filling_summery_id":gst_yearly_filling_summery_id,
                                             "gst_filling_report_id":gst_filing_data_report})
        if not(existing_doc):
            gst_filing_data_report_doc=frappe.get_all("Gst Filing Data Report",
                                    filters={"name":gst_filing_data_report},
                                    fields=["name","month","quarterly"])
            gst_filling_data = frappe.new_doc('Gst Filling Data')
            if gst_filing_data_report_doc[0].month:
                gst_filling_data.month = gst_filing_data_report_doc[0].month
                gst_filling_data.gst_filling_report_id=gst_filing_data_report_doc[0].name
            else:
                gst_filling_data.month = gst_filing_data_report_doc[0].quarterly
                gst_filling_data.gst_filling_report_id=gst_filing_data_report_doc[0].name
            gst_filling_data.gst_yearly_filling_summery_id = gst_yearly_filling_summery_id
            gst_filling_data.gstfile = gstfile
            gst_filling_data.created_manually=1
            gst_filling_data.insert()
            gst_filling_data.save()

            return "Gst Filing Data created successfully."
        else:
            return "Gst Filling Data you are trying to create already exists"
    except frappe.exceptions.ValidationError as e:
        frappe.msgprint(f"Validation Error: {e}")
        return False
    except Exception as e:
        frappe.msgprint(f"Error: {e}")
        return False

@frappe.whitelist()
def checking_user_authentication(user_email):
	try:
		status=False
		user_roles = frappe.get_all('Has Role', filters={'parent': user_email}, fields=['role'])

		# Extract roles from the result
		roles = [role.get('role') for role in user_roles]
		doc_perm_records = frappe.get_all('DocPerm',
									 filters = {'parent': 'Gst Filling Data','create': 1},
									 fields=["role"])
		for doc_perm_record in doc_perm_records:
			if  doc_perm_record.role in roles:
				status=True
				break
		return {"status":status,"value":[roles,doc_perm_records]}
		
	except Exception as e:
		print(e)
		return {"status":"Failed"}

