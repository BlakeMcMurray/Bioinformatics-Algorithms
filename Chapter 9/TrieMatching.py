import requests 
inputFile = "/Users/blakemcmurray/acanedoAnnotated.txt"
outputFile = "/Users/blakemcmurray/outPutJSON.txt"
otherFile = "/Users/blakemcmurray/testOut.txt"
json = []
tagListMaster = []
lastColumn = {}
def returnFirstGOQuery(keyWord):
    params = {'query': keyWord}
    r = requests.get('http://www.ebi.ac.uk/QuickGO/services/ontology/go/search', params=params)
    query = r.json()
    return(query["results"][0]["id"],query["results"][0]["name"])
count = 0
with open(inputFile,"r") as inFile:
    with open(outputFile,"w") as outFile:
        lines = inFile.readlines()
        for line in lines:
            line = line.split("\t")
            jsonDict = {"seqname":line[0], "source":line[1], "feature":line[2],"start":line[3], "end":line[4], "score":line[5], "strand":line[6],"frame":line[7],'ID': '-', 'Dbxref': '-', 'Is_circular': '-', 'Name': '-', 'collected-by': '-', 'collection-date': '-', 'country': '-', 'gbkey': '-', 'genome': '-', 'isolation-source': '-', 'lat-lon': '-', 'mol_type': '-', 'nat-host': '-', 'strain': '-', 'gene_biotype': '-', 'locus_tag': '-', 'pseudo': '-', 'Parent': '-', 'Note': '-', 'inference': '-', 'product': '-', 'transl_table': '-', 'old_locus_tag': '-', 'protein_id': '-', 'partial': '-', 'start_range': '-', 'end_range': '-', 'gene': '-', 'anticodon': '-', 'bound_moiety': '-', 'regulatory_class': '-','Blast': '-','PFAM': '-','Prosite': '-','kegg': '-','GOID': '-','GOName': '-','uniprot': '-','comment': '-'}

            tagger = line[8].split(';')
            for i in range(len(tagger)):
                lastColumn[tagger[i][0:tagger[i].find("=")]] = tagger[i][tagger[i].find("=") +1 :].strip()
              
            jsonDict.update(lastColumn)
            print(jsonDict["product"])

                goQuery = returnFirstGOQuery(jsonDict["product"])
                jsonDict["GOID"] = str(goQuery[0])
                jsonDict["GOName"] = str(goQuery[1])
            json.append(jsonDict)            
        outFile.write(str(json))
    outFile.close()
inFile.close()





            
            
