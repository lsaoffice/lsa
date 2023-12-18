# Copyright (c) 2023, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GstFilingDataReport(Document):

    def on_submit(self):
        try:
            # Get the values of gst_yearly_summery_report and gst_type fields
            gst_yearly_summery_report = self.gst_yearly_summery_report
            gst_type = self.gst_type

            # Apply filter on "Gst Yearly Filing Summery" DocType
            filter_conditions = {
                "gst_yearly_summery_report_id": gst_yearly_summery_report,
                "gst_type": gst_type
            }

            # Fetch records based on filter conditions
            matching_records = frappe.get_all("Gst Yearly Filing Summery", filters=filter_conditions, fields="gst_yearly_summery_report_id,gst_file_id,gst_type,name")
            # frappe.msgprint(matching_records)

            # Process matching records as needed
            for record in matching_records:
                # print("Debug: Printing record before frappe.msgprint")
                # print(record)
                gst_filling_data = frappe.new_doc("Gst Filling Data")
                gst_filling_data.gst_yearly_filling_summery_id = record.name
                gst_filling_data.gstfile = record.gst_file_id
                gst_filling_data.month = self.month
                gst_filling_data.gst_filling_report_id = self.name
                gst_filling_data.gst_type = record.gst_type

                gst_filling_data.insert()
            frappe.msgprint("New Records Created in Gst Filling Data!")

        except Exception as e:
            frappe.msgprint(f"An error occurred: {e}")