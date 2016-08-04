# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bhamesh Kore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import mimetypes 
import re
from frappe import _
from frappe.model.document import Document

VALID_IMAGE_MIMETYPES = ["image"]

class WedditCandidate(Document):
	def validate(self):
		self.validate_mobile_no()
		self.validate_family_members()
		self.validate_mobile()

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

	def valid_url_mimetype(url, mimetype_list=VALID_IMAGE_MIMETYPES):
		# http://stackoverflow.com/a/10543969/396300 
		mimetype, encoding = mimetypes.guess_type(url)
		if mimetype:
			return any([mimetype.startswith(m) for m in mimetype_list])
		else:
			return False 
		
	def validate_mobile(self):
		number = re.compile(r'[^0-9]').sub('', self.mobile_no)
		if len(number) != 10:
			# 7-digit number, should include area code
			frappe.throw(_("INCLUDE YOUR AREA CODE OR ELSE."))

	def format_number(self):
	 	if len(self.mobile_no) == 10:
			# basically return XXX-XXX-XXXX
	 		return re.compile(r'^(\d{3})(\d{3})(\d{4})$').sub('$1-$2-$3', self.mobile_no)
	 	else:
	 		# basically return +XXX-XXX-XXX-XXXX
	 		return re.compile(r'^(\d+)(\d{3})(\d{3})(\d{4})$').sub('+$1-$2-$3-$4', self.mobile_no)