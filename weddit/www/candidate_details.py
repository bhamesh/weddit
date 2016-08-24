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
def save_fm(fmid, firstname, lastname, relation):
	# return "{fm};{fn};{ln};{rl}".format(fm=fmid,fn=firstname,ln=lastname,rl=relation);

	fm = frappe.get_doc("Weddit Candidate Family Member",fmid)
	fm.first_name = firstname
	fm.last_name = lastname
	fm.relation = relation
	fm.save()
	frappe.db.commit()
	return "Candidate Family Details update Successfully"


@frappe.whitelist()
def add_fm(wcid,firstname, lastname, relation):
	# return "{fm};{fn};{ln};{rl}".format(fm=fmid,fn=firstname,ln=lastname,rl=relation);

	nfm = frappe.new_doc("Weddit Candidate Family Member")
	nfm.parent = wcid
	nfm.parenttype = "Weddit Candidate"
	nfm.parentfield = "family_members"
	nfm.first_name = firstname
	nfm.last_name = lastname
	nfm.relation = relation
	nfm.insert()
	frappe.db.commit()
	return "New Family Member Add Successfully"


@frappe.whitelist()
def delete_fm(fmid):
	frappe.delete_doc("Weddit Candidate Family Member",fmid)
	# nfm.parent = wcid
	# nfm.parenttype = "Weddit Candidate"
	# nfm.parentfield = "family_members"
	frappe.db.commit()
	return "Delete Family Member Successfully"
