# Copyright (c) 2023, Mohan and contributors
# For license information, please see license.txt
 
import frappe
from frappe.utils import escape_html
 
def execute(filters=None):
    # Define columns for the report
    columns = [
        {"label": "CID", "fieldname": "customer_id", "fieldtype": "Link", "options": "Customer", "width": 100, "height": 100},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 200, "height": 100},
        {"label": "Mobile No.", "fieldname": "mobile number", "fieldtype": "Data", "width": 120, "height": 100},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100, "height": 100},
        {"label": "Enabled", "fieldname": "enable", "fieldtype": "Data", "width": 50, "height": 100},
        {"label": "Service Count", "fieldname": "service_count", "fieldtype": "Int", "width": 150, "height": 100},
    ]
    
    # Get all service doctypes from "Customer Chargeable Doctypes"
    unsorted_services = frappe.get_all("Customer Chargeable Doctypes", fields=["name", "doctype_name"])
    
    # Calculate the count for each service doctype
    counts = {service.doctype_name: len(frappe.get_all(service.doctype_name)) for service in unsorted_services}
    
    # Sort the services based on the counts in descending order
    services = sorted(unsorted_services, key=lambda x: counts[x["doctype_name"]], reverse=True)
    
    # Add columns for each service
    for service in services:
        # Add column for service count
        servic_doc = {"label": str(service.doctype_name)[:-4] + " Count", "fieldname": service.name + " count", "fieldtype": "Int", "width": 50, "height": 100}
        columns.append(servic_doc)
        
        # Add column for service customer
        servic_doc = {"label": str(service.doctype_name)[:-4] + " Customer", "fieldname": service.name + " customer", "fieldtype": "Text Editor", "width": 250, "height": 100}
        columns.append(servic_doc)
        
    # Get data for the report
    data = get_data(services, filters)
 
    return columns, data
 
def get_data(services, filters):
    data = []
    
    #filters
    service_filter = filters.get("service_user")
    status_filter = filters.get("status")
    enabled_filter = filters.get("enabled")
 
    # Get all customers
    customers = frappe.get_all("Customer", fields=["name", "customer_name", "mobile_no", "disabled", "custom_customer_status_"])
    
    # Iterate through each customer
    for i in customers:
        data_row = {
            "customer_id": i.name,
            "customer_name": i.customer_name,
            "mobile number": i.mobile_no,
            "status": i.custom_customer_status_
        }
        
        # Set enable status based on 'disabled' field
        data_row["enable"] = "No" if i.disabled else "Yes"
        
        service_count = 0
        # Iterate through each service doctype
        for service in services:
            # Get services for the customer
            c_service = frappe.get_all(service.doctype_name, fields=["description", "current_recurring_fees"], filters={"customer_id": i.name, "enabled": 1})
            description_value = ""
            
            # Iterate through each service record
            for j in c_service:
                description_list = j.description.split("-")
                if len(description_list) == 2:
                    description_value += f"{description_list[0]}-({description_list[1]}) (Rs {j.current_recurring_fees}), "
                else:
                    description_value += f"{description_list[0]}-(Rs {j.current_recurring_fees}), "
                service_count += 1
            
            # Set description value for service customer
            data_row[service.name + " customer"] = description_value
            data_row[service.name + " count"] = len(c_service)
        
        # Set total service count for the customer
        data_row["service_count"] = service_count
        data += [data_row]
    
    # Filter data based on service_user
 
    if service_filter == "Customers without Services":
        filtered_data = [d for d in data if d["service_count"] == 0]
        data = filtered_data
    elif service_filter == "Customers with Services":
        filtered_data = [d for d in data if d["service_count"] != 0]
        data = filtered_data
 
    for i in data:
        if enabled_filter=="All" and status_filter=="All":
            pass
        elif enabled_filter=="All":
            data=[d1 for d1 in data if d1["status"]==status_filter]
        elif status_filter=="All":
            data=[d2 for d2 in data if d2["enable"]==enabled_filter]
        else:
            data=[d2 for d2 in data if d2["enable"]==enabled_filter]
            data=[d1 for d1 in data if d1["status"]==status_filter]
 
    return data
