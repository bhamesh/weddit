# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bhamesh Kore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class WedditCandidate(Document):
	def validate(self):
		self.validate_mobile_no()
		self.validate_family_members()

	def validate_mobile_no(self):
		if len(self.mobile_no) != 10:
			frappe.throw(_("Mobile number invalid!"))

	def validate_family_members(self):
		member_list = []

		for member in self.family_members:
			if member.relation.lower() in ["mother", "father"]:
				member_list.append(member.relation)

		if len(member_list)!= len(set(member_list)):
			frappe.throw(_("Father or Mother cannot repeat in relation"))
		
			
