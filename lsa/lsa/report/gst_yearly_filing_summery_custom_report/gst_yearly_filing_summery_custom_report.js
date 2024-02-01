// Copyright (c) 2024, Mohan and contributors
// For license information, please see license.txt

frappe.query_reports["Gst Yearly Filing Summery custom report"] = {
	"filters": [
	{
			"fieldname": "gst_yearly_summery_report_id",
			"label": __("Fiscal Year"),
			"fieldtype": "Link",
			"options": "Gst Yearly Summery Report"
		},

	]
};
