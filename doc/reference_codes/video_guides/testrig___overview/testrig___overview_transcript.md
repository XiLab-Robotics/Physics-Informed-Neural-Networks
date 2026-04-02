# TestRig - Overview.mp4 Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## 00:00:01 - 00:05:00

Buongiorno, questo è un video che fornisce una panoramica del test rig e vi parlerò delle informazioni generali sullo stesso: i suoi limiti, il file dove poterlo trovare. Successivamente daremo uno sguardo a TwinCAT per capire perché sono stati cambiati alcuni elementi dopo che il test rig è stato studiato solo con il lato carico. Infine illustrerò i metodi implementati per il test rig completo. Prima di guardare questo video vi consiglio di vedere i video di Monari, se non li avete ancora visti: parlano in generale di come è stato realizzato il programma in TwinCAT e quindi alcune cose le prenderò per scontate. Il test rig attualmente è composto da un motor side, un zero shaft e un load side, come si può vedere dalla figura; per questo motivo vengono cambiati diversi limiti, ad esempio a sinistra si vede il limite entro cui il servomotore potrebbe…

## 00:05:00 - 00:09:58

Il servomotore, lato carico, dovrebbe mantenere la velocità impostata; se questa velocità viene applicata al servomotore e al lato carico, il sistema controlla la velocità. Il test rig non entra in risonanza, quindi il motivo è incerto: si ipotizza che l’interazione dei poli all’interno del servomotore e del lato carico generi coppie che eccitano la risonanza. Questa è una tesi, ma esistono riscontri sul fatto che il sistema entra in risonanza sempre tra 1150 e 1250 rpm, intervallo comandato dal servomotore. Si sottolinea che quando il servomotore lato carico è attivo, il sistema va in risonanza; se invece è disabilitato, non si verifica risonanza in quell’intervallo. Pertanto, bisogna prestare particolare attenzione a questo intervallo di velocità.

## 00:09:58 - 00:14:53

Il servomeccanismo lato motore presentava le accelerazioni e decelerazioni di default quando c'era solo il servomeccanismo lato carico, ovvero senza la presenza del giunto. Rientrando sull'immagine, questo giunto non era presente; quindi si controllava soltanto questa parte. Senza il giunto, le accelerazioni di default (circa 4000 radianti al secondo) non erano presenti. Tali accelerazioni impossibili da sostenere generavano vibrazioni sull'albero lento, rallentando l'accelerazione e la decelerazione. Se si raggiungevano alte velocità, il sistema, dopo circa 3 secondi, non si fermava; quindi avviava il check oscillation. A 500 rpm, il sistema tendeva a rilassarsi, riducendo le vibrazioni.

## 00:14:53 - 00:19:45

Il sistema del riduttore lato carico gira a 1900 rpm quando è a 17 gradi; non è molto più basso di 1000 rpm, quindi è molto urbano. È soprattutto consigliabile farlo girare per tanto tempo con la velocità a una temperatura dell’olio così bassa: si suggerisce sempre un mini riscaldamento iniziale con il sistema che gira a una velocità leggermente più lenta e solo successivamente avviare il metodo. In alternativa, se si preferisce, è possibile modificare il metodo aggiungendo un'ulteriore discretizzazione: se la temperatura è al di sotto di 30‑25 °C, utilizzare questa velocità. Questo è un suggerimento per il futuro. Quest'altro metodo è realizzato per lo scarico dell’albero lento; ovvero, se si decide di far girare il sistema test rig in modalità manuale, il sistema impone una velocità iniziale. Una volta che la rotazione si ferma, essendo il lato carico, proprio per definizione, il carico rimane stabile.

## 00:19:45 - 00:24:44

Per cui, quando il sistema entra in errore, la coppia si disabilita e il meccanismo rilascia la molla che è in tensione. Ok, ho capito. Se questa spiegazione è chiara posso andare avanti. A volte capita che la load non funzioni bene, ovvero si stalla; ciò avviene probabilmente perché lo scarico della coppia si trova su un punto di tensione. In questo caso si verifica un movimento in cui la coppia cerca di spostare l'albero del riduttore verso zero: il riduttore supera il dente e quindi si carica positivamente. Il PID riportando la coppia a zero, il riduttore si rimuove, supera nuovamente il dente e si ricarica in negativo. Se ciò accade basta intervenire sul metodo dello scarico: andare manualmente ad impostare countPrecision uguale a numPrecision oppure abbassarlo. In realtà, se si vuole modificare questo parametro...

## 00:24:46 - 00:29:42

Questo per quanto riguarda il test rig: l'ultima cosa che volevo aggiungere è quando va in errore. Mi sono accorto, ad esempio, che il sistema va in errore se è in rotazione... E, rotazione, e, ripeto, si preme il pulsante rosso, il pulsante rosso, lo sottolineo: viene premuto soltanto in caso in cui il sistema è irrecuperabile. Perché questo? Perché attualmente la safety aggiunta al sistema è una safety che è un torque off. Ovvero che, una volta premuto il pulsante rosso, viene tolta la coppia ai due drive. Quindi non... Diciamo, il sistema si ferma tramite l'inerzia del sistema stesso. E non si ha, come in altri casi, ad esempio, non si ha che se premo il pulsante rosso il sistema si va a fermare in maniera controllata. Quindi, se il sistema, ad esempio, gira a velocità elevate, premendo il pulsante rosso, il sistema si ferma con la sua inerzia.

## 00:29:45 - 00:34:44

Vi mostro un attimo IndraWorks, in particolare quello relativo al lato motore. Si riconosce che uno è il lato motore e l'altro il lato carico da IndraDrive; il default è il lato motore EtherCAT 1008, come si vede dalla dicitura qui sopra. Il lato carico, invece, lo mostro subito: ha AXIS 1 EtherCAT 1007. Riprendo un attimo questa cosa per spiegarla meglio. Quando il sistema va in errore, la luce B Drive Ready diventa rossa, indicando che c'è stato un problema. Per resettare gli errori basta premere questo pulsante all'interno di IndraDrive; così si puliscono gli errori nel software. All'interno di TwinCAT invece bisogna premere Reset Error. Il tasto Reset Error non va premuto una sola volta, ma più volte: la prima pressione serve a resettare gli errori iniziali e le successive per completare il reset.

## 00:34:44 - 00:39:44

Per aggiornare Indadrive, dobbiamo far conoscere a TwinCAT la modalità di operazione. In questo caso si può vedere che la modalità attualmente è sconosciuta; perciò inizialmente eravamo passati da config a run. Vi mostro una breve demo: nella schermata principale, la luce è arancione quando il motore è abilitato con power on. Una volta premuto il pulsante di avvio, si dovrebbe sentire il relay e la luce diventa verde. Quando la luce è verde, i due drive sono passati in modalità A e B; premiamo il pulsante per verificare che entrambi siano attivi.

## 00:39:44 - 00:42:06

Il ready è importante, quindi bisogna essere pronti a disabilitare il sistema una volta che questo viene disabilitato; in quel momento l'errore viene resettato. Ok, ci sono domande a riguardo? Un’ultima cosa che volevo far vedere: si possono riconoscere come ho definito prima i due servomotori, ovvero le due finestre di INDA drive tramite default, che è quella del lato motore e Axis 1, che è quella del lato carico. Inoltre, per quanto riguarda l’ID del device, quindi Lettercat 1008 e Lettercat 1007, questi sono scritti correttamente; se non vado errato qua no sono scritti. All’interno della function block del motore si può vedere che l'ADS port è 1700; in questo caso infatti ho cliccato Pitastrig FB Load 1700 e Pitastrig FB Motor 1800, per cui 1700 è il lato carico e 1800 è il lato motore. Se non ci sono ulteriori domande posso concludere. Per quanto riguarda l'ADS port...
