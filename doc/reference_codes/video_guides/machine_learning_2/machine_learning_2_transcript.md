# Machine_Learning_2.mp4 Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## Source Reference

* Canonical source video: [machine_learning_2.mp4](../../../../reference/video_guides/source_bundle/machine_learning_2.mp4)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## 00:00:01 - 00:04:56

Buongiorno a tutti, questo è il secondo video di Machine Learning. Prima di iniziare vi suggerisco di guardare il primo video, perché in questo episodio verranno scontate alcune cose già spiegate precedentemente e mi concentrerò direttamente sull’esperimento e sui dettagli che ho tralasciato nel primo. Qui trovi il report realizzato: se volete approfondire la correzione del transmission error con Machine Learning, potete consultarlo. Come detto nel video precedente, sono state create due task per comunicare tra loro; ciò è stato necessario a causa dei limiti di TwinCAT, che consentono solo una comunicazione molto veloce e quindi a basso tempo ciclo.

## 00:04:57 - 00:09:55

Dovrebbe essere 1,3253 microsecondi. Andando a considerare questo tempo, magari si ottiene una correzione migliore. Se invece si vuole concentrare soltanto sul ritardo di comunicazione tra le task, basta considerare da questo elemento in poi. Perché? Scusate, era questo. Perché? Perché da questo task si assegna la variabile che il task fast vuole inviare al task slow. Il task slow, però, la riceve soltanto all'inizio del task successivo. Perché? Perché in entrambi i programmi è stato inserito l'input-output task begin. Quindi lo scambio degli input e output avviene all'inizio del task, e non appena si può. Per cui, una volta che viene concluso il calcolo, si aspetta l'inizio del task successivo per inviarlo. All'inizio del task successivo il task fast lo invia e il task slow lo riceve. A questo punto lui inizia già il suo calcolo con il machine learning. Quindi, appunto qua ho scritto ...

## 00:09:56 - 00:14:54

Il caso 100 riguarda la macchina di stato; lo stato 100 permette di leggere il primo valore di coppia registrato dalla camma, ovvero dal file CSV, il primo valore di coppia della prima riga. Se questo valore è diverso da zero, si procede a caricare il sistema finché non si raggiunge tale valore. Una volta raggiunto, avviene un counter di precisione: vengono presi 10.000 punti in cui la coppia si trova intorno a quel range, e successivamente parte l’esperimento con il PID, realizzando così l’esperimento completo. Questa fase è fondamentale: è una fase di carico dell’albero, dove si arriva al valore desiderato e il primo valore viene scritto nel file CSV della coppia. L’esperimento prosegue da qui.

## 00:14:54 - 00:17:41

Per cui si potrebbe mantenere anche per tre cicli lo stesso valore, spengendo il valore del forward e attivando quello del backward. Questa potrebbe essere un'idea. Ritornando ai valori di input, questi tre sono i modelli di forward: uno per la fase, uno per l’ampiezza e uno per l’ampiezza della frequenza. La stessa cosa, immagino, avverrà per quelli di backward una volta aggiunti. Questa è una variabile proprio per decidere se scrivere i valori di output. È la variabile della temperatura, ovvero a quale temperatura vogliamo fare l’esperimento e realizzarlo. Questa è la gamma che si vuole importare. Come ho detto in precedenza, la gamma deve essere una tabella con quattro colonne; ve la mostro se la trovo. Tutto all’interno di questo qua. Non la trovo. La cerco subito. Scusate, ecco, ho trovato il file. Come si può vedere ...
