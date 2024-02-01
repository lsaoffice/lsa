# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = [
        # Customer details columns
       {"label": "CID", "fieldname": "customer_id", "fieldtype": "Link", "options": "Customer", "width": 100},
	   {"label": "ID", "fieldname": "id", "fieldtype": "Link", "options": "Gst Yearly Filing Summery", "width": 200},
	   {"label": "Company", "fieldname": "company", "fieldtype": "Data", "width": 300},
        {"label": "GSTIN", "fieldname": "gstfile", "fieldtype": "Link", "options": "Gstfile", "width": 150},
		{"label": "GST Type", "fieldname": "gst_type", "fieldtype": "Data", "width": 110},
        {"label": "FY", "fieldname": "fy", "fieldtype": "Link", "options": "Gst Yearly Summery Report", "width": 100},
        {"label": "Total Sales Taxable", "fieldname": "sales_total_taxable", "fieldtype": "Currency", "width": 130},
        {"label": "Total Purchase Taxable", "fieldname": "purchase_total_taxable", "fieldtype": "Currency", "width": 130},
        {"label": "Total Tax Paid Amount", "fieldname": "tax_paid_amount", "fieldtype": "Currency", "width": 130},
        {"label": "Total Interest Paid Amount", "fieldname": "interest_paid_amount", "fieldtype": "Currency", "width": 100},
        {"label": "Total Penalty Paid Amount", "fieldname": "penalty_paid_amount", "fieldtype": "Currency", "width": 100},
		]

	data=get_data(filters)
	return columns, data

def get_data(filters):
	data = []

	gst_yearly_filling_summery_filter={}
	if (filters.get("gstfile_enabled")):
		if (filters.get("gstfile_enabled"))=="Enabled":
			gst_yearly_filling_summery_filter["gstfile_enabled"]=1
		elif (filters.get("gstfile_enabled"))=="Disabled":
			gst_yearly_filling_summery_filter["gstfile_enabled"]=0

	gst_yearly_filling_summery_filter={}
	if (filters.get("gstfile_enabled")):
		if (filters.get("gstfile_enabled"))=="Enabled":
			gst_yearly_filling_summery_filter["gstfile_enabled"]=1
		elif (filters.get("gstfile_enabled"))=="Disabled":
			gst_yearly_filling_summery_filter["gstfile_enabled"]=0
	if (filters.get("gst_yearly_summery_report_id")):
		gst_yearly_filling_summery_filter["gst_yearly_summery_report_id"]=filters.get("gst_yearly_summery_report_id")


	gst_yearly_filling_summery_s = frappe.get_all("Gst Yearly Filing Summery", 
											   filters=gst_yearly_filling_summery_filter,
											   fields=["name","gst_yearly_summery_report_id","gstin","gst_type","company","cid",
														"sales_total_taxable","purchase_total_taxable","tax_paid_amount",
														"interest_paid_amount","penalty_paid_amount"])

	for gst_yearly_filling_summery in gst_yearly_filling_summery_s:
		
		if gst_yearly_filling_summery:
			data_row = {
				"customer_id": gst_yearly_filling_summery.cid,
				"id":gst_yearly_filling_summery.name,
				"company": gst_yearly_filling_summery.company,
				"gstfile": gst_yearly_filling_summery.gstin,
				"gst_type":gst_yearly_filling_summery.gst_type,
				"fy": gst_yearly_filling_summery.gst_yearly_summery_report_id,
				"sales_total_taxable": gst_yearly_filling_summery.sales_total_taxable,
				"purchase_total_taxable": gst_yearly_filling_summery.purchase_total_taxable,
				"tax_paid_amount": gst_yearly_filling_summery.tax_paid_amount,
				"interest_paid_amount": gst_yearly_filling_summery.interest_paid_amount,
				"penalty_paid_amount": gst_yearly_filling_summery.penalty_paid_amount,
			}
			
			data.append(data_row)

	return data




