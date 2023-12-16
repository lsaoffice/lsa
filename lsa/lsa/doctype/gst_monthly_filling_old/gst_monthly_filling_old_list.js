frappe.listview_settings['GST Monthly Filling old'] = {
    onload: function(listview) {
        // Add your custom button
        listview.page.add_inner_button(__("Your Button Label"), function() {
            // Handle button click action

            // Show prompt to select a month
            frappe.prompt(
                [
                    {'fieldname': 'selected_month', 'fieldtype': 'Select', 'label': 'Select Month', 'options': 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec'}
                ],
                function(values){
                    // Make a server-side call to fetch and insert records with the selected month
                    frappe.call({
                        method: "lsa.lsa.doctype.gst_monthly_filling.gst_monthly_filling.fetch_and_insert_records",
                        args: {
                            selected_month: values.selected_month
                        },
                        callback: function(response) {
                            if (response.success) {
                                frappe.msgprint("New Records Created in GST Monthly Filling old!");
                            } else {
                                // Log the error details to the console
                                console.error("Error creating records in GST Monthly Filling old:", response);
                                
                                // Display a more informative error message
                                var errorMessage = response.error_message || "Unknown error";
                                frappe.msgprint("Error creating records in GST Monthly Filling old: " + errorMessage);
                            }
                        }
                    });
                },
                __('Select Month'),
                __('Submit')
            );
        });
    }
};
