// Copyright (c) 2024, Mohan and contributors
// For license information, please see license.txt

frappe.query_reports["Custom IT Assessee Filing Data"] = {
	"filters": [
		{
			"fieldname": "ay",
			"label": __("Fiscal Year"),
			"fieldtype": "Link",
			"options": "IT Assessee File Yearly Report"
		},
	]
};

