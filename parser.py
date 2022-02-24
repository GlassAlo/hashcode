from asyncio.windows_events import NULL
from operator import concat
import sys
import skill
import contributor

with open(sys.argv[1]) as file:
    lines = file.readlines()

words = []

# List of the words in the file
for line in lines:
    for word in line.split():
        words.append(word)

contributor_nbr = int(words[0])

projet = int(words[1])

contrib_array = [[]]
i_arr = 0
line_count = 1
while line_count < len(lines) - 1 and len(contrib_array) <= contributor_nbr:
    # Remove end of line
    contrib_array.append([])
    line = lines[line_count].replace('\n', '')
    # Get name of the contributor
    name = line.split()[0]
    # Get thee number of skills
    nbr_skills = int(line.split()[1])
    contrib_array[i_arr].append(name)
    for x in range(0, nbr_skills):
        contrib_array[i_arr].append(lines[line_count + x + 1].replace('\n', ''))
    line_count += nbr_skills + 1
    i_arr += 1

# Create the contributor objects
contributors = []
for i in range(0, contributor_nbr):
    contributors.append(contributor.Contributor(contrib_array[i][0], contrib_array[i][1:]))

while line_count < len(lines) - 1:
    # Remove end of line
    contrib_array.append([])
    line = lines[line_count].replace('\n', '')
    # Get name of the contributor
    name = line.split()[0]
    # Get thee number of skills
    nbr_skills = int(line.split()[4])
    contrib_array[i_arr].append(name)
    for x in range(0, nbr_skills):
        contrib_array[i_arr].append(lines[line_count + x + 1].replace('\n', ''))
    line_count += nbr_skills + 1
    i_arr += 1

contrib_array.pop()
i_arr = 0
line_count = 1
while i_arr < contributor_nbr:
    i_arr += 1
print(contrib_array)
print(contributor_nbr)
# Retun a contributor who has the shill C++
for i_arr in range(i_arr, len(contrib_array)):
    print(contrib_array[i_arr][0])
    for i in range(0, contributor_nbr):
        for y in range(len(contrib_array[i])):
            if contrib_array[i][y].split(' ')[0] == contrib_array[i_arr][1].split(' ')[0]:
                print(contrib_array[i][0])
