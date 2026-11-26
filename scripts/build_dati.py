import json, csv, openpyxl, collections, urllib.request, re
wb=openpyxl.load_workbook('istat/Il_1522_dati_provinciali_trimestrali_2013_III-trim-2024.xlsx',data_only=True)
rows=list(wb['tav.1'].iter_rows(values_only=True))
years=rows[4]; q=rows[5]
cols=[]; y=None
for i in range(2,len(rows[4])):
    if years[i]: y=years[i]
    cols.append((i,y,q[i]))
calls={}; reg=None
for r in rows[6:]:
    if r[0] and r[0] in ('N.D.','ITALIA') : break
    if r[0]: reg=r[0]
    p=r[1]
    if not p or p=='N.D.': continue
    calls[p]={'reg':reg,'v':{(y,qq):(r[i] or 0) for i,y,qq in cols}}
# geometry
t=json.load(open('prov24.topojson')); geoms=list(t['objects'].values())[0]['geometries']
gn={g['properties']['name']:g['properties'] for g in geoms}
norm=lambda s:re.sub(r"[^a-z]","",s.lower().replace("’","'"))
gm={norm(k):k for k in gn}
alias={'Reggio Emilia':"Reggio nell'Emilia",'Pesaro Urbino':'Pesaro e Urbino','Olbia-Tempio':'Sassari','Reggio Calabria':'Reggio di Calabria','Forlì Cesena':"Forli'-Cesena"}
unm=[]
cen=json.load(urllib.request.urlopen('https://piersoft.github.io/centri-antiviolenza/data/centri.geojson'))['features']
ncent=collections.Counter(); 
for f in cen:
    c=int(f['properties']['istat'][:3])
    if f['properties']['regione'].startswith('Sard'):
        c={'Sassari':90,'Nuoro':91,'Cagliari':92,'Oristano':95,'Sud Sardegna':111,'Gallura Nord-Est Sardegna':90,'Sulcis Iglesiente':111}[f['properties']['provincia']]
    ncent[c]+=1
out=[]; used=set(); merged={}
for p,d in calls.items():
    k=gm.get(norm(p)) or gm.get(norm(alias.get(p,p)))
    if not k: unm.append(p); continue
    used.add(k)
    if k in merged:
        for kk in d['v']: merged[k]['v'][kk]+=d['v'][kk]
    else:
        merged[k]={'reg':d['reg'],'v':dict(d['v'])}
for k,d in merged.items():
    g=gn[k]; v=d['v']
    last4=sum(v[k2] for k2 in [(2023,'4° trim'),(2024,'1° trim'),(2024,'2° trim'),(2024,'3° trim')])
    ann={yy:sum(v[(yy,qq)] for qq in ['1° trim','2° trim','3° trim','4° trim']) for yy in range(2013,2024)}
    code=g['prov_istat_code_num']
    out.append(dict(provincia=k,regione=d['reg'],codice=g['uts_istat_code_num'],pcode=code,
      chiamate_4t=last4,al_giorno=round(last4/366,2),centri=ncent.get(code,0),
      per_centro_giorno=round(last4/366/ncent[code],3) if ncent.get(code) else '',
      quarters=[v[(yy,qq)] for yy in range(2013,2025) for qq in ['1° trim','2° trim','3° trim','4° trim'] if (yy,qq) in v],
      **{f'a{yy}':ann[yy] for yy in ann}))
print('unmatched calls',unm); print('geom not used',[k for k in gn if k not in used])
print('centers by pcode not in out',{c:n for c,n in ncent.items() if c not in {o['pcode'] for o in out}})
print(len(out), sum(o['chiamate_4t'] for o in out), sum(o['centri'] for o in out))
json.dump(out,open('prov_1522.json','w'),ensure_ascii=False)
w=csv.DictWriter(open('prov_1522.csv','w'),fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
