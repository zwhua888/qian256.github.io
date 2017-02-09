import glob
filenames = glob.glob('_posts/*md')

total_tags = []
for filename in filenames:
	f = open(filename, 'r')
	crawl = False
	for line in f:
		if crawl:
			current_tags = line.strip().split()
			if current_tags[0] == 'tags:':
				total_tags.extend(current_tags[1:])
				crawl = False
				break
		if line.strip() == '---':
			if not crawl:
				crawl = True
			else:
				crawl = False
				break
	f.close()
total_tags = set(total_tags)
for tag in total_tags:
	f = open('tags/' + tag + '.md', 'w')
	write_str = '---\nlayout: tagpage\ntag: ' + tag + '\n---\n'
	f.write(write_str)
	f.close()
