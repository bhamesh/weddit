// Copyright (c) 2016, Bhamesh Kore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Weddit Candidate', {
	refresh: function(frm) {

	},
	validate: function(frm) {
		if (frm.doc.mobile_no.length !=10) 
		{
			frappe.throw (__("mobile number invalid!");
		}
	}
});
