import frappe

@frappe.whitelist()
def find_duplicate_names(name=None):
	duplicates = frappe.get_all("Weddit Candidate", filters={"first_name": name})
	cdt_names = ""
	for i in duplicates:
		cdt_names += "<a href='/desk#Form/Weddit Candidate/" + str(i.name) + "'>" + str(i.name) + "</a><br>"
	return cdt_names
