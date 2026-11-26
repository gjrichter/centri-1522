import re,csv,json
x=open('cl.xml',encoding='utf8').read()
names={}
for i,b in re.findall(r'<structure:Code id="(IT[A-Z0-9]{3})"[^>]*>(.*?)</structure:Code>',x,re.S):
    m=re.findall(r'xml:lang="it"[^>]*>([^<]*)',b); names[i]=m[-1] if m else None
pop={}
for r in csv.DictReader(open('pop.csv')):
    if r['TIME_PERIOD']=='2024' and r['REF_AREA'] in names and len(r['REF_AREA'])==5: pop[names[r['REF_AREA']]]=int(r['OBS_VALUE'])
norm=lambda s:re.sub(r"[^a-z]","",s.lower())
pn={norm(k):v for k,v in pop.items()}
pn[norm('Aosta')]=pn[norm("Valle d'Aosta / Vallée d'Aoste")]; pn[norm('Bolzano')]=pn[norm('Bolzano / Bozen')]; pn[norm("Forli'-Cesena")]=pn[norm('Forlì-Cesena')]
o=json.load(open('prov_1522.json'))
for p in o:
    p['pop2024']=pn[norm(p['provincia'])]
    p['per100k']=round(p['chiamate_4t']/p['pop2024']*1e5,1)
    p['centri_per100k']=round(p['centri']/p['pop2024']*1e5,2)
json.dump(o,open('prov_1522.json','w'),ensure_ascii=False)
rows=[{k:v for k,v in p.items() if k!='quarters'} for p in o]
w=csv.DictWriter(open('prov_1522.csv','w'),fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
