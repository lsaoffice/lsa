# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"fieldname": "cid", "label": ("CID"), "fieldtype": "Link", "options": "Customer","width": 100},
        {"fieldname": "customer_status", "label": ("Customer Status"), "fieldtype": "Data", "width": 100},
        {"fieldname": "name", "label": ("ID"), "fieldtype": "Link", "options": "Gst Filling Data", "width": 100},
        {"fieldname": "filing_status", "label": ("Filing Status"), "fieldtype": "Data", "width": 170},
        {"fieldname": "gstfile", "label": ("GSTIN"), "fieldtype": "Link", "options": "Gstfile", "width": 165},
        {"fieldname": "gstfile_enabled", "label": ("Gstfile Enable"), "fieldtype": "Check", "width": 50},
        {"fieldname": "company", "label": ("Company"), "fieldtype": "Data", "width": 220},
        {"fieldname": "mobile_no_gst", "label": ("Mobile No GST"), "fieldtype": "Data", "width": 120},
        {"fieldname": "gst_user_name", "label": ("GST User Name"), "fieldtype": "Data", "width": 120},
        {"fieldname": "gst_password", "label": ("GST Password"), "fieldtype": "Data", "width": 120},
        {"fieldname": "proprietor_name", "label": ("Proprietor Name"), "fieldtype": "Data", "width": 120},
        {"fieldname": "executive", "label": ("Executive"), "fieldtype": "Data", "width": 150},
        {"fieldname": "gst_type", "label": ("GST Type"), "fieldtype": "Data", "width": 100},
        {"fieldname": "month", "label": ("Month"), "fieldtype": "Data", "width": 100},
        {"fieldname": "fy", "label": ("Fiscal Year"), "fieldtype": "Data", "width": 100},
        {"fieldname": "gst_yearly_filling_summery_id", "label": ("GstYearly Filling Summery Id"), "fieldtype": "Link", "options": "Gst Yearly Filing Summery", "width": 300},
        {"fieldname": "filing_notes", "label": ("Filing Notes"), "fieldtype": "Data", "width": 150},
    ]

	# Construct additional filters based on the provided filters
    additional_filters = {}
    if filters.get("name"):
        additional_filters["name"] = filters["name"]
    if filters.get("gst_type"):
        if filters.get("gst_type")!="All":
            additional_filters["gst_type"] = filters["gst_type"]
        
    if filters.get("fy"):
        additional_filters["fy"] = filters["fy"]
    if filters.get("month"):
        if filters.get("month")!="All":
            additional_filters["month"] = ["like", f"%{filters['month']}%"]
    if filters.get("executive"):
        additional_filters["executive"] = ["like", f"%{filters['executive']}%"]
    if filters.get("gst_yearly_filling_summery_id"):
        additional_filters["gst_yearly_filling_summery_id"] = filters["gst_yearly_filling_summery_id"]
        
    # Fetch data using Frappe ORM
    data = frappe.get_all(
        "Gst Filling Data",
        filters=additional_filters,
        fields=["cid","customer_status", "name", "filing_status", "gstfile","gstfile_enabled","company",
                "mobile_no_gst","gst_user_name","gst_password", "proprietor_name", "executive", 
                "gst_type", "month", "fy","gst_yearly_filling_summery_id", "filing_notes"],
        as_list=True
    )


    return columns, data






