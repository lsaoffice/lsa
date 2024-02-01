import frappe
import requests
from frappe import _
from frappe.utils import today
from datetime import datetime



@frappe.whitelist()
def sync_sales_orders_followup(so_id):
    try:
        
        followup_values={"values":[],}
        if True:
            existing_followups=frappe.get_all("Customer Followup",
                                    fields=["name","sales_order_summary"])
            existing_so_followups=[i.name for i in existing_followups if so_id in i.sales_order_summary]
            # print(existing_sales_orders)
            if existing_so_followups:
                for existing_so_followup in existing_so_followups:
                    # print(existing_sales_order)
                    followup=frappe.get_doc("Customer Followup",existing_so_followup)


                    followup_values["values"]+=[[followup.customer_id,followup.name,
                                                followup.status,followup.total_remaining_balance,
                                                followup.followup_date,followup.next_followup_date,
                                                followup.executive_name,followup.followup_note]]
            #############################################################################################
            existing_payments=frappe.get_all("Payment Entry Reference",
                                              filters={"reference_name":so_id},
                                                fields=["name","creation","parent","total_amount","outstanding_amount",
                                                        "allocated_amount"])
            existing_payments_list=[]
            for existing_payment in existing_payments:
                existing_payment_list=[existing_payment.parent,existing_payment.total_amount,
                                       existing_payment.outstanding_amount,existing_payment.allocated_amount,
                                       existing_payment.creation]
                existing_payments_list.append(existing_payment_list)
            print(existing_payments_list)
            return {"status":"Synced successfully.","followup_values":followup_values,"payment_values":existing_payments_list}
        # else:
        #     return {"status":"Synced successfully."}
    except Exception as e:
        frappe.msgprint(f"Error: {e}")
        return False
# @frappe.whitelist()
# def sync_sales_orders_customer(customer_id):
#     try:

#         ############################Sales Order############################################################################

#         existing_sales_orders=frappe.get_all("Sales Order",
#                                     filters={"customer":customer_id,
#                                              "status":['in', ["Draft","On Hold","To Deliver and Bill","To Bill","To Deliver"]]})
#         # print(existing_sales_orders)
#         so_details={}
#         custom_count_of_so_due=0
#         custom_total_amount_due_of_so=0.00
#         custom_details_of_so_due=[]

#         if existing_sales_orders:

#             for existing_sales_order in existing_sales_orders:
#                 # print(existing_sales_order)
#                 sales_order=frappe.get_doc("Sales Order",existing_sales_order.name)
#                 if sales_order.rounded_total>sales_order.advance_paid:
#                     custom_count_of_so_due+=1
#                     custom_total_amount_due_of_so+=(sales_order.rounded_total-sales_order.advance_paid)
#                     custom_details_of_so_due.append(sales_order.name)
#                     so_details[sales_order.name]=[sales_order.rounded_total,sales_order.advance_paid,
#                                                   sales_order.rounded_total-sales_order.advance_paid,
#                                                   sales_order.custom_so_from_date,sales_order.custom_so_to_date,
#                                                   sales_order.status,sales_order.custom_followup_count,
#                                                   sales_order.customer_name,sales_order.customer]
#             custom_details_of_so_due=", ".join(custom_details_of_so_due)


#         ##############################################followup button##############################################################
        
#         followup_button=False
#         if custom_total_amount_due_of_so>0:
#             followups=frappe.get_all("Customer Followup", filters={"customer_id":customer_id},fields=["name","status"])
#             open_followup=[i for i in followups if i.status=="Open"]
#             if followups and not(open_followup):
#                 next_followup_date=""
#                 for followup in followups:
#                     followup_doc=frappe.get_doc("Customer Followup",followup.name)
#                     if followup_doc.status == "Closed" and followup_doc.next_followup_date:
#                         date_format = "%Y-%m-%d"
#                         this_followup_date=datetime.strptime(str(followup_doc.next_followup_date)
#                                                              , date_format).date()
#                         # print(this_followup_date)
#                         if next_followup_date=="" or this_followup_date >=next_followup_date :
#                             # print("next",next_followup_date,"this",this_followup_date)
#                             next_followup_date = this_followup_date
#                 if next_followup_date:
#                     today_date = datetime.now().date()
#                     if next_followup_date<=today_date:
#                         # print("this followup true",next_followup_date,today_date)
#                         followup_button=True
#                 else:
#                     # print("else followup true")
#                     followup_button=True
#             elif open_followup:
#                 pass
#             else:
#                 # print("outer followup true")
#                 followup_button=True


#             ############################Follow up############################################################################
                
#             followup_values={"Open":[],"Closed":[],"values":[],}
#             if custom_total_amount_due_of_so>0:
#                 existing_followups=frappe.get_all("Customer Followup",
#                                         filters={"customer_id":customer_id,
#                                                 # "status":['in', ["Draft","On Hold","To Deliver and Bill","To Bill","To Deliver"]]
#                                                 })
#                 # print(existing_sales_orders)
#                 if existing_followups:
#                     last_closed_followup_date="Dummy"
#                     next_followup_date="Dummy"

#                     for existing_followup in existing_followups:
#                         # print(existing_sales_order)
#                         followup=frappe.get_doc("Customer Followup",existing_followup.name)

#                         if followup.status == "Open":
#                             open_followup=followup.name
#                             followup_nature="Open"
#                             open_followup_date=followup.followup_date
#                             followup_values["Open"]=[open_followup,followup_nature,open_followup_date]
#                         elif followup.status == "Closed" and not(followup_values["Open"]):
#                             print("next",next_followup_date,"this",followup.next_followup_date)
#                             if last_closed_followup_date=="Dummy" or \
#                                   last_closed_followup_date<followup.followup_date:
#                                 print("next update")
#                                 last_followup=followup.name
#                                 followup_nature="Closed"
#                                 next_followup_date=followup.next_followup_date
#                                 last_closed_followup_date=followup.followup_date
#                                 last_followup_comment=followup.followup_note
#                                 followup_values["Closed"]=[last_followup,followup_nature,next_followup_date,last_followup_comment]


#                         followup_values["values"]+=[[followup.customer_id,followup.name,
#                                                     followup.status,followup.total_remaining_balance,
#                                                     followup.followup_date,followup.next_followup_date,
#                                                     followup.executive_name,followup.followup_note]]

#             return {"status":"Synced successfully.","followup_button":followup_button,"values":[so_details,custom_count_of_so_due,
#                                                               custom_total_amount_due_of_so,custom_details_of_so_due],
#                                                               "followup_values":followup_values}
#         else:
#             return {"status":"Synced successfully."}
#     except Exception as e:
#         frappe.msgprint(f"Error: {e}")
#         return False
    

