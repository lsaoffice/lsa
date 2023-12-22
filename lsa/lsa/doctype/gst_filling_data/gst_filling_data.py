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

    def update_field(self, gst_yearly_filing_summery, field_name):
        # Get the field value from the current form
        field_value = getattr(self, field_name)

        # Check if the field value is not equal to 0
        if getattr(gst_yearly_filing_summery, field_name) != 0:
            # Increment the field by the current value
            setattr(gst_yearly_filing_summery, field_name, getattr(gst_yearly_filing_summery, field_name) + field_value)
        else:
            # Set the field to the current value if it's 0
            setattr(gst_yearly_filing_summery, field_name, field_value)

