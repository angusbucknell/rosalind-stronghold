#Given: At most 15 UniProt Protein Database access IDs.
#Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

import re
import urllib.request
results = {}

def search(string, search, ID):
    # Finds matches within the read FASTA page for the regex condition
    matches = list(re.finditer(search, string))
    start_pos = []
    # matches[i].start takes the start position from the all list elements
    for i in range(0,len(matches)):
        start_pos.append(matches[i].start()+1)
    # appends the dict with UniProt ID, and the start pos for all matches
    if len(start_pos) != 0:
        results[ID] = start_pos

file = open("X", "r")
protIDs = file.read().splitlines()

for i in range(0, len(protIDs)):
    link = "https://www.uniprot.org/uniprot/{}.fasta".format(protIDs[i])
    page = urllib.request.urlopen(link)
    # reads the UniProt FASTA page
    data = page.read().decode("utf-8")
    seq = "".join(data.splitlines()[1:])
    # seach function is used combined with necessary regex condition with lookahead.
    search(seq, "N(?=[^P][ST][^P])", protIDs[i])

for key, value in results.items():
    print(key)
    print(*value)





