#!/usr/bin/env python3

import argparse
import hashlib
import json
import logging
import os
import pickle
import time
import uuid

import pprint

logging.basicConfig(level=logging.DEBUG, filename='./debug.log', filemode='a')
logging.debug("start")


version = 0.1.1
issues_dir = "./issues"



class Issue(object):


	def __init__(self, committer, text, status=None, issue_id=None):
		self.committer = committer
		self.text = text
		if not status:
			status = "open" # TODO Enum
		self.status = status
		created_at = int(time.time())
		self.created_at = created_at
		self.updated_at = created_at
		if not issue_id:
			issue_id = uuid.uuid4().hex
		self.issue_id = issue_id


	def save(self):
		filename = issues_dir + "/" + self.issue_id
		with open(filename, 'w') as issue_file:
			json.dump(self.__dict__, issue_file)


	def load(self):
		pass


	def get_comments(self):
		pass


	def show(self):
		print("Issue: " + self.issue_id)
		print(self.text)


	def load(issue_id):
		filename = issues_dir + "/" + issue_id
		with open(filename, 'r') as issue_file:
			issue = json.load(issue_file)
		if not issue:
			pass # TODO

		i = Issue(issue['committer'], issue['text'], issue['status'], issue['issue_id'])
		i.created_at = issue['created_at']
		i.updated_at = issue['updated_at']

		return i


class IssueComment(object):


	def __init__(self, issue_id, text, commenter, created_at=None):
		self.issue_id = issue_id
		self.text = text
		self.commenter = commenter
		if not created_at:
			created_at = int(time.time())
		self.created_at = created_at
		self.updated_at = created_at


	def get_text(self):
		pass



def main(args):

	if args.list:
		list_issues()

	if args.issue_show:
		i = Issue.load(args.issue_show)
		i.show()

	if args.issue_create:
		i = Issue("Some User", args.issue_create)
		i.save()
		print("Created issue: " + i.issue_id)

	return



def list_issues():

	for issue_id in os.listdir(issues_dir):
		filename = issues_dir + "/" + issue_id
		with open(filename, 'r') as issue_file:
			issue = json.load(issue_file)
		if not issue:
			pass # TODO

		i = Issue(issue['committer'], issue['text'], issue['status'], issue['issue_id'])
		i.created_at = issue['created_at']
		i.updated_at = issue['updated_at']
		i.show()
		print("")





if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Track bugs in a Git repo")
	parser.add_argument('-l', '--list', help="List all issues", action="store_true")
	parser.add_argument('--issue-show',  type=str, help="Show issue")
	parser.add_argument('--issue-create',  type=str, help="Create issue")
	args = parser.parse_args()

	main(args)
