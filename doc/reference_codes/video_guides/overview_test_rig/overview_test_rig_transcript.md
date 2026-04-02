# Overview Test Rig.mp4 Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## 00:00:01 - 00:05:00

Buongiorno, questo è un video che fornisce una panoramica del test rig e vi parlerò delle informazioni generali sullo stesso. Vi illustrerò i suoi limiti e il file dove poterlo trovare. Successivamente daremo uno sguardo in TwinCAT per capire perché sono stati cambiati alcuni elementi dopo che il test rig è stato studiato solo con il lato carico. Infine, parleremo dei metodi implementati per il test rig completo. Prima di guardare questo video vi consiglio di vedere i video di Monari se non li avete ancora visti; parlano in generale di come è stato realizzato il programma in TwinCAT, quindi alcune cose le prenderò per scontate. Il test rig attualmente è composto da un motor side, un zero shaft e un load side, come si può vedere dalla figura. Per questo motivo vengono cambiati diversi limiti: a sinistra si vede il limite entro cui il servomotore potrebbe…

## 00:05:00 - 00:09:55

Il servomotore lato carico dovrebbe controllare la velocità del sistema; il test rig non va in risonanza, quindi non si sa perché. Immagino sia dovuto all’interazione dei poli all’interno del servomotore lato carico che generano coppie e eccitano la risonanza. Questa è una tesi, ma troviamo riscontri sul fatto che il sistema entra in risonanza sempre tra 1150 e 1250 rpm, comandato dal servomotore lato motore. Sottolineo: quando il servomotore lato carico è attivo, se viene disabilitato non si verifica la risonanza in quell’intervallo di velocità; quindi bisogna stare attenti a questo intervallo e a non superarlo.

## 00:09:55 - 00:14:52

Non sono più quelle che il sistema, solo con il servomeccanismo lato motore, aveva: le accelerazioni di default quando c'era solo il servomeccanismo sul carico o sul motore. In pratica, senza il giunto, l'accelerazione era gestita esclusivamente da quella parte. Quindi, rientrando sull'immagine, questo giunto non era presente; c’era soltanto la sezione che controllava quel segmento. Senza il giunto, le accelerazioni di default erano circa 4000 radianti al secondo quadro. Ora queste accelerazioni sono impossibili da sostenere e generano vibrazioni sull’albero lento. Per ridurre l’accelerazione e la decelerazione a velocità elevate, se dopo tre secondi il sistema non si è ancora fermato, viene attivato un check oscillante: a 500 rpm si disabilitano direttamente i motori.

## 00:14:52 - 00:19:47

Il motivo principale è che il relutore è un sistema che può essere utilizzato per effettuare un riscaldamento iniziale con la velocità del motore leggermente più lenta, e solo successivamente avviare il metodo di funzionamento normale. Si può modificare il metodo aggiungendo una discretizzazione ulteriore: se la temperatura è inferiore a 30 o 25 gradi, si utilizza questa velocità ridotta. Un suggerimento per il futuro. L'altro metodo è invece realizzato per lo scarico dell'albero lento; quando si fa girare il sistema test rig in modalità manuale, il sistema impone una velocità specifica. Questa velocità avvia la rotazione, e una volta che il motore si ferma, essendo il lato carico (per definizione), l’albero rimane sotto tensione, ovvero lo slow shaft. Per evitare che questo rimanga in tensione, poiché l'albero lento non dovrebbe rimanere bloccato...

## 00:19:47 - 00:24:42

Si disabilita la coppia e il sistema presenta un rilascio meccanico della molla; se questa situazione è chiara, posso procedere. A volte la load non funziona correttamente, ovvero si stalla: lo stallo è probabilmente dovuto al fatto che lo scarico della coppia avviene su un punto in cui è presente un dente. In questo caso il movimento fa sì che la coppia cerchi di spostare l’albero lento a zero; il riduttore quindi supera il dente e si carica positivamente, il PID riporta la coppia a zero, il riduttore si rimuove, supera nuovamente il dente e si ricarica negativamente. Se ciò accade, basta intervenire sul metodo di scarico: impostare manualmente il valore count precision uguale al non precision oppure abbassarlo; in pratica si può regolare questo parametro. Se si vuole modificare la situazione, il consiglio è di evitare di alterare troppo le impostazioni per mantenere stabile il comportamento del sistema.

## 00:24:45 - 00:29:42

Questo riguarda il test rig, che si verifica quando il sistema va in errore. Mi sono accorto, ad esempio, che il sistema entra in errore se è a rotazione e, ripeto, si preme il pulsante rosso. Il pulsante rosso deve essere premuto solo quando il sistema è recuperabile. Perché? Perché attualmente la safety aggiunta al sistema è una safety torque off: una volta premuto il pulsante rosso viene tolta la coppia ai due drive. Di conseguenza, il sistema si ferma tramite l'inerzia del proprio movimento e non si ha, come in altri casi, la possibilità di rinforzare il sistema. Quindi, se il sistema gira a velocità elevate e si preme il pulsante rosso, il sistema si arresta grazie alla sua inerzia; tuttavia, fermandosi con l'inerzia, il carico rimane elevato, poiché la velocità è doppia rispetto al motore, e naturalmente una copia...

## 00:29:45 - 00:34:41

Vi mostro un attimo Indraworld, in particolare quello del lato K motore. Si riconosce che uno è il lato motore e l'altro il lato carico da Indadrive 1 default. Il default è il lato motore EtherCAT 1008; proprio da questa dicitura si capisce che si tratta del lato motore. Il lato carico, invece, lo mostro subito: ha Axis 1 EtherCAT 1007. Dopo riprendo un attimo la spiegazione per chiarire meglio. Una volta che il sistema va in errore, si può vedere che l'AB DRIVE READY diventa rosso, indicando che è avvenuto un errore. Per resettare gli errori basta premere questo pulsante all'interno di Indadrive, così si puliscono gli errori nel software. All'interno di TwinCAT invece bisogna premere RESET ERROR; il reset non va fatto una sola volta, ma più volte, perché la prima pressione serve a resettare gli errori dell'albero di controllo.

## 00:34:41 - 00:39:40

È bene abilitare entrambi i motori per: 1) aggiornare Indadrive; 2) far conoscere a TwinCAT la modalità di operazione, perché si può vedere in questo caso che la modalità attualmente è sconosciuta. Perciò inizialmente eravamo passati da Config a Run. Vi faccio vedere una mini prova, così giusto che ci troviamo in questo elemento. Mostro anche che la luce è arancione; quindi abilito il motore con Power On, andando su P Main → Power On → True. Si dovrebbe sentire il relay come un interruttore e la luce diventa verde. Qui si vede la luce verde. Una volta che la luce è verde, mostro anche i due drive: sono passati in AB. Premendo il pulsante rosso, si vede subito che lo STO è attivo. In questo caso infatti siamo andati in errore. Lui non mi dà errore, ovviamente, perché? Perché il sistema no...

## 00:39:40 - 00:42:07

Vado a fare il terzo reset. Vedete infatti che parte subito lo stato ready? È importante quindi essere pronti a disabilitare il sistema una volta che questo, di cui viene resettato l'errore. Ok, ci sono domande a riguardo? No. L'ultima cosa che volevo far vedere è che si possono appunto riconoscere, come ho definito prima, i due servomotori, ovvero le due finestre di Indadrive, tramite default: quella del lato motore (axis 1) e quella del lato carico. Inoltre, per quanto riguarda l'ID del device, quindi lettercat 1008 e lettercat 1007, questi sono scritti, se non mi sbaglio, all'interno della function block del motore; se si va in quel blocco si può vedere che l'ADS port è 1007. In questo caso infatti ho cliccato P-test rig FB load 1007 e P-test rig FB motor 1008, per cui 1007 corrisponde al lato carico e 1008 al lato motore. Se non ci sono ulteriori domande...
