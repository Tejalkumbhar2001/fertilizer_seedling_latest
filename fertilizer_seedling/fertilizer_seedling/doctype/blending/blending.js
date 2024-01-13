// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Blending', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Blending', {
	foundation_batch_id: function(frm) {
		frm.clear_table("blending_child_table");
		frm.refresh_field('blending_child_table');
		frm.call({
			method:'get_lot_info',
			doc:frm.doc
		})
	}
});





frappe.ui.form.on('Blending', {
    after_save: function(frm) {
        // Call server-side method after saving
        frappe.call({
            method: 'changes_status',
            doc: frm.doc,
            callback: function(response) {
                // Handle the response here
                if (response.message) {
                    console.log(response.message);
                }
            }
        });
    }
	
});

