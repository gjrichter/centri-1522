# Chiamate al 1522 e centri antiviolenza

Due mappe interattive (ixmaps-gl) sulle chiamate al numero antiviolenza e stalking **1522** per provincia e sui **430 centri antiviolenza** dell'elenco ufficiale.

- **`index.html`** — un anno (ottobre 2023 – settembre 2024): coropletica e lollipop, a scelta in numeri assoluti o ogni 100.000 abitanti.
- **`timeline.html`** — i 47 trimestri 2013 – III 2024, con cursore, play e velocità.

Entrambe: interruttori per coropletica, lollipop e centri; pulsante *Orbita* (inclina e ruota la vista); tooltip con curva trimestrale.

## Cosa mostrano (e cosa no)

- Sono **chiamate al 1522, non quelle ricevute dai singoli centri**: quel dato non è pubblicato. Il 1522 orienta verso i centri.
- Chiamate da utenti per provincia di provenienza; esclusi i casi con provincia non disponibile. Sono chiamate, non persone.
- Il tasso usa la popolazione ISTAT al 1° gennaio 2024 per tutti gli anni: per i trimestri più vecchi è un'approssimazione.
- Dal 2023 la serie ISTAT ha una discontinuità (cambio di archiviazione): il confronto con gli anni precedenti va fatto con cautela.
- Province del 2024; Olbia-Tempio è accorpata a Sassari. Caltanissetta non ha centri nell'elenco usato.

## Dati e fonti

- ISTAT, *Il numero di pubblica utilità 1522 — dati provinciali trimestrali 2013 – III 2024* (Dipartimento per le Pari Opportunità).
- Popolazione ISTAT al 1.1.2024 (SDMX).
- Elenco dei centri: [1522.eu](https://www.1522.eu/centri-antiviolenza/mappa.html), georeferenziato nel progetto [piersoft/centri-antiviolenza](https://github.com/piersoft/centri-antiviolenza).
- Confini provinciali 2024: [gjrichter/geo](https://github.com/gjrichter/geo); fondo ArcGIS Topo (Esri); motore [ixmaps-gl](https://github.com/gjrichter/ixmaps-gl).

`prov_1522.csv` raccoglie i valori per provincia. `scripts/` contiene gli script usati per elaborarli (a scopo documentale: leggono file scaricati a mano, non sono pensati per girare da soli).

> In caso di pericolo immediato: **112**. Il **1522** è gratuito, attivo 24 ore su 24, anche in chat su [1522.eu](https://www.1522.eu/).
