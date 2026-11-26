# Chiamate al 1522 e centri antiviolenza

Due mappe interattive (ixmaps-gl) sulle chiamate al numero antiviolenza e stalking **1522** per provincia e sui **430 centri antiviolenza** dell'elenco ufficiale.

**Online:** [gjrichter.github.io/centri-1522](https://gjrichter.github.io/centri-1522/) · [timeline](https://gjrichter.github.io/centri-1522/timeline.html)

- **`index.html`** — un anno (ottobre 2023 – settembre 2024), per provincia.
- **`timeline.html`** — i 47 trimestri dal 1° 2013 al 3° 2024, con cursore, play (0,5×–3×) e grafico nazionale.

## Cosa c'è nelle mappe

Colore delle province (coropletica) e **lollipop** mostrano lo stesso valore, scelto con l'interruttore in alto a destra: **N. assoluti** (predefinito) oppure **ogni 100.000 abitanti**. I punti sono i 430 centri (blu: contatto h24; nero: con orari di apertura).

- **Interruttori** per accendere e spegnere coropletica, lollipop e centri.
- **Orbita**: inclina la mappa e la ruota in continuo; parte da sola all'apertura e si ferma trascinando la mappa o con il pulsante.
- **Tooltip** delle province: valore, media al giorno, centri e curva trimestrale 2013 – III 2024. Tooltip dei centri: nome, comune, telefono.
- **Informazioni sui dati**: pulsante nel pannello dei controlli che apre un overlay con la descrizione di fonti, elaborazione e limiti (testo diverso nelle due pagine).
- **Grafico nazionale** (solo `timeline.html`, in basso): linea piena = **totale ISTAT** per trimestre (riga «ITALIA» della Tavola 1, comprese le chiamate senza provincia); linea punteggiata = somma delle sole chiamate con provincia, cioè quelle che finiscono sulla mappa. La distanza tra le due linee è la quota non attribuita a una provincia. Una linea verticale tratteggiata segna la discontinuità di serie del 2023.

## Cosa mostrano (e cosa no)

- Sono **chiamate al 1522, non quelle ricevute dai singoli centri**: quel dato non è pubblicato. Il 1522 orienta verso i centri.
- Chiamate da utenti, telefoniche e via chat; sono chiamate, non persone.
- **Solo una parte delle chiamate ha una provincia.** Negli ultimi 12 mesi il totale ISTAT è 69.470 chiamate, di cui 43.735 (63%) con provincia; la quota era dell'88–93% nel 2013–2016 e del 61–63% nel 2023–2024. I valori per provincia (mappa, lollipop, tasso) sono quindi una **sottostima**, e la loro serie risente di questo calo: il totale ISTAT è passato da 32.367 chiamate nel 2013 a 51.713 nel 2023 (+60%), la somma delle province da 28.626 a 31.580 (+10%).
- Dal 2023 la serie ISTAT ha una discontinuità (cambio di archiviazione): il confronto con gli anni precedenti va fatto con cautela.
- Il tasso usa la popolazione ISTAT al 1° gennaio 2024 per tutti gli anni: per i trimestri più vecchi è un'approssimazione. Nella timeline il tasso è trimestrale.
- Alcune province hanno valori molto alti (per esempio Ferrara): la causa non è stata verificata.
- Province del 2024; Olbia-Tempio è accorpata a Sassari; Carbonia-Iglesias, Ogliastra e Medio Campidano non hanno valori nel periodo. Caltanissetta non ha centri nell'elenco usato.

## Elaborazione

- **Chiamate**: Tavola 1 ISTAT (chiamate da utenti per provincia di provenienza e trimestre), abbinata alle province ISTAT 2024 per nome. In `index.html` si sommano i 4 trimestri IV 2023 – III 2024; la media «al giorno» divide per 366.
- **Tasso** = chiamate ÷ popolazione al 1.1.2024 × 100.000.
- **Centri**: ogni centro è assegnato alla provincia con il codice ISTAT del suo comune (per la Sardegna con una corrispondenza fatta a mano).
- **Classi di colore**: `index.html` usa 5 classi a quantili per la coropletica e soglie fisse per i lollipop; `timeline.html` usa soglie fisse su tutti i trimestri, così i colori sono confrontabili nel tempo. I lollipop hanno dimensione proporzionale al tasso e compressa (potenza 3) per i numeri assoluti.
- La copia locale di `lolli_chart.js` incorporata nelle pagine differisce dall'originale di ixmaps-flat solo per l'assenza del segno «+» e del nome della provincia sotto il valore.

## Dati e fonti

- ISTAT, *Il numero di pubblica utilità 1522 — dati provinciali trimestrali 2013 – III 2024* (dati del Dipartimento per le Pari Opportunità).
- Popolazione ISTAT al 1.1.2024 (SDMX).
- Elenco dei centri: [1522.eu](https://www.1522.eu/centri-antiviolenza/mappa.html), georeferenziato nel progetto [piersoft/centri-antiviolenza](https://github.com/piersoft/centri-antiviolenza).
- Confini provinciali 2024: [gjrichter/geo](https://github.com/gjrichter/geo); fondo ArcGIS Topo (Esri); motore [ixmaps-gl](https://github.com/gjrichter/ixmaps-gl).

`prov_1522.csv` raccoglie per provincia i valori dei 12 mesi (chiamate, media al giorno, centri, popolazione, tasso) e i totali annui 2013 – 2023; non contiene la serie trimestrale né il totale nazionale, che sono incorporati in `timeline.html`. `scripts/` contiene gli script usati per l'elaborazione (a scopo documentale: leggono file scaricati a mano, non sono pensati per girare da soli).

> In caso di pericolo immediato: **112**. Il **1522** è gratuito, attivo 24 ore su 24, anche in chat su [1522.eu](https://www.1522.eu/).
