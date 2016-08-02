# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bhamesh Kore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class WedditCandidate(Document):
	def validate(self):
		if len(self.mobile_no) != 10:
			frappe.throw(_("Mobile number invalid!"))
