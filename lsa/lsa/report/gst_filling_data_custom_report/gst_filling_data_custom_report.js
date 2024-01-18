// Copyright (c) 2024, Mohan and contributors
// For license information, please see license.txt

frappe.query_reports["Gst Filling Data Custom Report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("ID"),
			"fieldtype": "Link",
			"options": "Gst Filling Data"
		},
		{
			"fieldname": "gst_type",
			"label": __("GST Type"),
			"fieldtype": "Select",
            "options": [
				"All",
				"Regular",
				"Composition",
				"QRMP"	
			]
		},
		{
			"fieldname": "fy",
			"label": __("Fiscal Year"),	
			"fieldtype": "Link",
			"options": "Gst Yearly Summery Report"
		},
		{
			"fieldname": "month",
			"label": __("Month"),
			"fieldtype": "Select",
            "options": ["All","JAN","FEB","MAR","JAN-MAR","APR","MAY","JUN","APR-JUN",
                		"JUL","AUG","SEP","JUL-SEP","OCT","NOV","DEC","OCT-DEC"]
		},
		{
			"fieldname": "executive",
			"label": __("Executive"),
			"fieldtype": "Data"
		},
{
			"fieldname": "gst_yearly_filling_summery_id",
			"label": __("GstYearly Filing Summery Id"),
			"fieldtype": "Link",
			"options": "Gst Yearly Filing Summery"

		}
	]
};

