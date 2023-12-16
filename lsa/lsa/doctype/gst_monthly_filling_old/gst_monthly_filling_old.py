

# Assuming "GST Monthly Filling" is the correct doctype name
import frappe
from frappe.model.document import Document

class GSTMonthlyFillingold(Document):
    pass

@frappe.whitelist()
def fetch_and_insert_records(selected_month):
    try:
        # Fetch records from Gstfile with filter gst_type = 'regular'
        gstfile_records = frappe.get_all("Gstfile", filters={"gst_type": "regular"}, fields=["gst_number"])

        # Create new records in GST Monthly Filling
        new_records = []
        for record in gstfile_records:
            new_record = GSTMonthlyFillingold(doctype="GST Monthly Filling", gst_file_id=record.gst_number, month=selected_month)
            # Set other fields as needed
            # new_record.some_other_field = "Some Value"
            new_record.insert()
            new_records.append(new_record.as_dict())

        frappe.msgprint("New Records Created in GST Monthly Filling!")
        return {"success": True}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error in fetch_and_insert_records")
        return {"success": False, "error_message": str(e)}
