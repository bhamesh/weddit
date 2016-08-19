import frappe
import frappe.database
def get_context(context):
	
	context.doc = frappe.get_doc("Weddit Candidate", "WCDT00001")

@frappe.whitelist()
def edit_data(docname, firstname, lastname,dateofbirth,mobileno,gen,marstat,relgn,cas,mothtng,city):
	wc = frappe.get_doc("Weddit Candidate",docname)
	wc.first_name = firstname
	wc.last_name = lastname
	wc.date_of_birth = dateofbirth
	wc.mobile_no = mobileno
	wc.gender = gen
	wc.marital_status = marstat
	wc.religion = relgn
	wc.caste=  cas
	wc.mother_tongue = mothtng
	wc.city = city  
	wc.save()
	frappe.db.commit()
	return "Candidate update Successfully"


	@frappe.whitelist()
def update_details(docname, firstname):