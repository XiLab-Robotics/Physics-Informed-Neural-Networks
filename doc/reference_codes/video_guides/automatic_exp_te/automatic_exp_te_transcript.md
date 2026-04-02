# Automatic_Exp_TE.mp4 Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## Source Reference

- Canonical source video: [automatic_exp_te.mp4](../../../../reference/video_guides/source_bundle/automatic_exp_te.mp4)
- Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## 00:00:00 - 00:04:59

Buongiorno a tutti, oggi vi parlerò dell’esperimento automatizzato per testare il transmission error a diverse velocità, temperature e coppie. Questo esperimento è stato automatizzato perché si era consapevoli che il test rig in quel caso era stabile; tuttavia è importante che l’utente rimanga in attesa poiché non c’è un monitoring della sicurezza, quindi deve osservare gli esperimenti. Non è necessario che l’utente rimanga a guardare gli scope ma deve rimanere in ascolto del test rig, potendo fare altro, così da essere pronto all’intervento nel caso percepisca rumori o altre anomalie. In questo caso è stato realizzato appunto un sistema di avvio automatico dell’esperimento attraverso le sezioni: la prima sezione crea la matrice che poi verrà assegnata volta per volta all’esperimento. L’assegnazione del valore…

## 00:05:00 - 00:10:00

Perciò fate attenzione a questa possibilità: andando a modificare qui, non viene cambiata la parte di calcolo, ovvero la dimensione dei vettori. La dimensione dei vettori rimane comunque 17 per sua dichiarazione, anche se in realtà sulla dichiarazione sopra l'hai modificata ponendo 3. Quindi fate molta attenzione a questo punto. In passato andavo sempre a cliccare su Config e modificare direttamente le variabili dal codice, poi scaricavo nuovamente il progetto. Se si vuole essere più precisi, questa è una metodologia molto manuale; altrimenti si potrebbe intervenire a livello di codice interno (non so attualmente come), ma si potrebbe pensare a una cosa del genere. Comunque, in questo modo...

## 00:10:00 - 00:14:56

Tanto tempo per raffreddarsi, inoltre l’altra condizione è se l’esperimento è stato fatto o no. Infatti ho aggiunto l’ultima colonna della matrice come booleano, ovvero 0 e 1 dove 0 corrisponde a esperimento non fatto e 1 a esperimento fatto. Questa metodologia di ciclo if ci permette di effettuare diversi esperimenti in diverse casistiche: la prima casistica è ad esempio fare un esperimento al 25 °C; il sistema si riscalda fino a 28 °C, a quel punto gli esperimenti al 25 °C non possiamo più farli perché è troppo caldo per il riduttore. Ma possiamo fare quelli da 30 °C: una volta fatto l’esperimento a 30 °C la velocità è talmente bassa che il riduttore si raffredda, e quindi scendiamo sotto i 26 °C.

## 00:14:56 - 00:16:33

Le tre variabili vengono assegnate automaticamente direttamente dal codice: la prima colonna della matrice corrisponde alla velocità, la seconda alla coppia e la terza alla temperatura. Vengono quindi assegnate direttamente qui. Suggerisco che gli esperimenti siano stati realizzati sempre con queste quattro variabili; non è chiaro se si tratti di un PID ottimale. Non lo so sinceramente, ma sappiamo che il sistema è stabile con queste configurazioni. Il filtro è stato tolto perché a basse velocità portava la risonanza al sistema: aggiungendo il filtro si accentuava la risonanza e, inoltre, non si studia il sistema con un dettaglio sufficiente. Ponendo un filtro si escludono proprio i dati filtrati, e dato che questo filtro non aggiunge sicurezza ma anzi a volte può peggiorare le prestazioni, è stato rimosso.
