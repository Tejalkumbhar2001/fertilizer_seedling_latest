// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Germination Test', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child_entries',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child_entri',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed',
			doc:frm.doc
		})
	}
});
