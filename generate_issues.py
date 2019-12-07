import os, os.path
import sys

while True:
	title_name = input("enter the title\n")
	issue_num = input("enter the issue number\n")
	date_published = input("enter publish date\n")
	isbn = input("enter isbn\n")

	# read lines until empty line
	print("enter content\n")
	content = ""
	while True:
		tmp_content = sys.stdin.readline()
		if tmp_content == '\n':
			break
		else:
			content += tmp_content

	file_txt = ''
	file_txt += '---\n'
	file_txt += 'title: ' + title_name + '\n'
	file_txt += 'num: ' + issue_num + '\n'
	file_txt += 'img: ' + issue_num.replace('.','_') + '.jpg\n'
	file_txt += 'date_published: ' + date_published + '\n'
	file_txt += 'isbn: ' + isbn + '\n'
	file_txt += 'amazon: NONE\n'
	file_txt += '---\n'
	file_txt += '\nContent\n\n'
	file_txt += content.replace('\n', '\n\n').replace('“', '"').replace('”', '"').replace('’', '\'')

	file = open("_issues/" + title_name.lower().replace('/','').replace(' ','').replace('.','_') + ".md", "w")
	file.write(file_txt)
	file.close()

	input("Press Enter to continue...")
