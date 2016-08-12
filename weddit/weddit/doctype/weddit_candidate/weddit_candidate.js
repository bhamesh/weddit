// Copyright (c) 2016, Bhamesh Kore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Weddit Candidate', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){	
			frm.add_custom_button(__('Find Duplicates'), function(frm){
				frappe.call({
					method: "weddit.api.find_duplicate_nacmes",
					args: {
						"name": cur_frm.doc.first_name
					},
					callback: function(r){
						frappe.msgprint(r.message);
					}
				});
			});
		}
	},
	validate: function(frm) {  
		if (frm.doc.mobile_no.length != 10)
		{
			frappe.throw (__("Please enter valid number!"));
		}
	}
});

// function allnumeric(inputtxt)  
//    {  
//       var numbers = /^[0-9]+$/;  
//       if(inputtxt.value.match(numbers))  
//       {  b
//       alert('Your Registration number has accepted....');  
//       document.form1.text1.focus();  
//       return true;  
//       }  
//       else  
//       {  
//       alert('Please input numeric characters only');  
//       document.form1.text1.focus();  
//       return false;  
//       }  
//    }  