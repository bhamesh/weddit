# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "weddit"
app_title = "Weddit"
app_publisher = "Bhamesh Kore"
app_description = "Matrimonial Profile Matching"
app_icon = "octicon octicon-organization"
app_color = "red"
app_email = "bhams91.kore@gmail.com"
app_license = "GPL v3"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/weddit/css/weddit.css"
# app_include_js = "/assets/weddit/js/weddit.js"

# include js, css files in header of web template
# web_include_css = "/assets/weddit/css/weddit.css"
# web_include_js = "/assets/weddit/js/weddit.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "weddit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

website_generators = ["weddit"]

# Installation
# ------------

# before_install = "weddit.install.before_install"
# after_install = "weddit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "weddit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"weddit.tasks.all"
# 	],
# 	"daily": [
# 		"weddit.tasks.daily"
# 	],
# 	"hourly": [
# 		"weddit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"weddit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"weddit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "weddit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "weddit.event.get_events"
# }

