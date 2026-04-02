# FB_ADRC_and_PID.mp4 Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## Source Reference

- Canonical source video: [fb_adrc_and_pid.mp4](../../../../reference/video_guides/source_bundle/fb_adrc_and_pid.mp4)
- Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## 00:00:00 - 00:04:59

Buongiorno a tutti, in questo video vi parlerò della function block della DRC. La function block è realizzata per effettuare un controllo. Come si può vedere, questa è la function block dell'albero, proprio ADRC di grado 3; infatti la DRC è di grado 3. Ovviamente presumo che sia già stato visto l'altro video riguardo la DRC o che si abbia familiarità con essa. Questo video implica quindi una conoscenza della DRC: spiegherò come è strutturato il function block, senza addentrarmi nella composizione interna della DRC stessa. Il function block è di grado 3. In realtà, la DRC propriamente sarebbe di grado 2, il controllore di grado 2 e l'ESO di grado 3. Inoltre è stata inserita anche la TPG, che è stata implementata tramite le variabili...

## 00:04:59 - 00:09:57

È una variabile che è presente anche sulla DRC; omega cl sarebbe un omega, l'ho definita come omega close loop, ovvero la omega del controllore. Perché? Per far sì che il sistema sia implementato in maniera più semplice possibile, è stata utilizzata una DRC lineare, a differenza della DRC di Han, che è non lineare e utilizza diverse equazioni e funzioni non lineari. In questo caso abbiamo voluto implementare il sistema tramite una funzione il più lineare possibile: quindi prendere la DRC più semplice. Il saturation limit è il limite di saturazione in modo da non dare valori troppo alti; è una misura cautelativa che ho visto anche nel paper che utilizzavano, e proprio si applica all'uscita del controllore, prima del plant.

## 00:09:57 - 00:14:57

Metti in true la variabile, poi quella variabile non controlla più il function block ma ti permette solo di ottenere la risposta in output. In questo caso, nel backoff del controllore ADRC, in realtà non serve perché, ad esempio, se metti execute su un MC Velocity e premi Execute True, il servomotore raggiunge la velocità impostata; prima però verifica che sia arrivato alla velocità desiderata. Se poi riponi Execute su False, il motore continuerà a muoversi finché non raggiunge la velocità predefinita. Non ti dice quando è stato realizzato l’evento, quindi non avrai in output le variabili error_done o velocity, né altre variabili presenti all’interno del function block. In questo modo si ottiene una panoramica generale del funzionamento del backoff nel function block.

## 00:14:57 - 00:19:56

Realizzata proprio da Han nel suo paper, l'obiettivo è che le derivate non amplifichino il rumore ad alta frequenza né gli errori di alta frequenza. L'ASO (Adaptive State Observer) è un sistema ancora non mostrato perché mi ero concentrato prima sul TPG; ripeto: il TPG sono tutte formule di Han, mentre l'ASO è un osservatore realizzato tramite metodi simili. Le formule sono inserite qui e si può vedere chiaramente che si tratta di un modello di terzo ordine, poiché abbiamo tre uscite (z1, z2, z3) che fungono anche da input. Come nel caso del TPG, z1, z2, z3 sono impostati al loro valore precedente, dato che il sistema è discreto e deve utilizzare il valore del ciclo precedente. Successivamente viene utilizzata la variabile z (che rappresenta lo stato discreto), e infine vengono impiegate le costanti l1, l2, l3.

## 00:19:56 - 00:24:21

Il sistema in questione è non lineare, ma la sua risposta non si comporta come previsto; invece, reagisce solo quando si avvicina alla saturazione. C'è quindi una richiesta di reset che imposta tutte le variabili a zero. L'output segnala quando il reset viene effettivamente eseguito, ovvero quando tutte le reference sono impostate su 1. Se si vuole attivare la richiesta di reset, non è necessario mantenere `execute` a true; può essere anche false, e di conseguenza `stop` può essere false. La richiesta di reset può essere fatta in qualsiasi momento, anche quando il sistema è sotto controllo. Non credo di aver aggiunto altro: possiamo verificare la struttura, che consiste in variabili...
