# FB_ADRC_and_PID.mp4 Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## 00:00:00 - 00:04:55

Buongiorno a tutti, in questo video vi parla della function block della GRC. La function block della GRC ha una function block realizzata per effettuare un controllo come si può vedere questa function block dall'albero, proprio a GRC, in fatti la GRC è di grado 3. Ovviamente io doppio scontato che magari si è stato realizzato, è stato già visto l'altro video riguarda di rc o comunque sia conoscenza della GRC. Questo video implica un'osservazione della GRC, perchè ovviamente dirò come è strutturato e non mi è dentro e l'ho per quanto riguarda proprio come è così tutto la GRC, ma dirò solo come è strutturato il function block. Quindi, il function block è di grado 3, per cui in questo caso i realità ad rc, propriomente sarebbe di grado due controllo di semplice di grado, due po' il resto è di grado 3. Inoventa stanza di tangati PG, a tip PG è stata inserita tramite le var ...

## 00:04:55 - 00:09:50

M'egnava vedere l'innettario, bizzarro, una variabile che anche sull'adirare presente, omega c' è definito, io ho definito un omega closed loop, ovvero sarebbe la omega del controllore, perché questo per farlo evitare il sistema non è una cosa semplice possibile, è stato utilizzato una diari lineare, per cui non è comunque di anno, che è una diari non lineare, perché lui utilizza diverse equazioni, diverse funzioni che non sono lineari, in questo caso non abbiamo l'ulto in preventare il sistema tramite una funzione lineare più semplice, quindi prenderebbe possibile la diari più semplice. Se tu resti un limite, la se è il limite di situazione, ma in realtà le che non andiamo a dare valori troppo alti, è una misura quotilativa che ho visto anche dal paper che mi zanno e poi la papio si da all'uscita.

## 00:09:50 - 00:14:32

Se è falsa, vuoi dire che il sistema è disabilitato? Per l'asse che registra solo valori di true, la variabile non controlla più la funzione lock, ma ti permette solo di ottenere la risposta; in questo caso, qui, del controllo agli estremi, reale neanche, perché ad esempio se metti x, chute sull'avaria su una funzione lock della velocità, quindi un MC, ci si trova, se non va derrato, sul tuo lì di x, chute true, l'ultiporta lo servomotore, ma prima fa quello che riva, prima che arrivi, a velocità del servomotore, tu ripigine x, chute false, lui continua sempre, il servo, quindi arrivando al stato inizialmente definito, solo che non ti dice, ma non è stata realizzata, ovvero non avrà in uscita le varie ability error.

## 00:14:32 - 00:19:30

Ci vedete che si chiamano i due memorizzatori, quindi i tipi G e gli stessi, questo perché perchè prima e tutto ci sono quali PG, quindi in monotono e avere un volume, che sono quelli che permettono al punto di calcolare l'errore e l'esposizione a riferimento. Questi PG sono una tipologia di riferimento, fatti diremo, realizzati da lui stesso nel suo paper. Fino a che le derivate non amplifichino il rumore ad alta frequenza né l'errore ad alta frequenza. L'altro invece è un sistema che non ho visto, perché prima era un tipo G molto comune, che sono ripetuti, i tipi G sono tutti le formule di Handa. L'altro invece è un osservatore, realizzato sempre, in questo caso, le formule sono inserite qui. Sì, poi vediamo bene che è un grande toro, perché tra le uscite ci sarebbe una azza a duezz.

## 00:19:30 - 00:24:21

Ma l'imprato, questo è utile solo, ed diciamo, è solo per tautilazioni, di ovvero scusami, tautilativo, un elemento sottanto cautilativo, se l'esperimento, valenziuturazione, va bene, fermare l'esperimento, perché non è un'esperimento buono, ma soprattutto non tenendo in considerazione o per vari studiarlo, perchâ ti può permetre di comprendere di franti cose, però è un sistema che comunque è tu sentato a smorzare, per cui un sistema non più lineare, ma dato che non si vuole dato che lui non sarebbe un po' non in quel modo, ma si comporta in quel modo, soltanto, a caso della sua situazione. Facciamo anche essere esatto, un vero dove l'angono posso tuttere variabilizzare, e qua c'è un'autputte che è un'al, che appunto quando il recetto viene realizzato, vero quando non sia in visi. Quando tuttere l'era e franze vengono poste vero, quindi suoi in domandare la richiesta, si vuole mettere la ...
