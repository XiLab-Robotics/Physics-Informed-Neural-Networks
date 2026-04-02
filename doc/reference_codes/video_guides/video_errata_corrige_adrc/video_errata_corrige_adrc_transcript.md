# Video_Errata_Corrige_ADRC.mkv Transcript

This transcript is the canonical cleaned Italian transcript for the video.

## Source Reference

- Canonical source video: [video_errata_corrige_adrc.mkv](../../../../reference/video_guides/source_bundle/video_errata_corrige_adrc.mkv)
- Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## 00:00:00 - 00:04:20

Mi scuso per l’errore nella presentazione precedente riguardo al video della DRC. In questo nuovo video mostro la simulazione in TwinCAT, corretta dopo aver collegato correttamente i componenti. Ora vediamo come il sistema segue l’andamento della rampa impostata su Simulink: ho inserito un valore di 500 e preparato la rampa; si osserva che il modello risponde seguendo l’andamento previsto, con un piccolo offset che abbiamo notato anche nel comportamento reale del sistema. Questo offset è probabilmente dovuto a una configurazione errata nella parte di implementazione. Per correggerlo, ho ripristinato la configurazione e ho verificato che il TPG (Test Program Generator) fosse impostato correttamente; questo dovrebbe risolvere l’anomalia. Dopo aver effettuato le modifiche, ho osservato se c’era un cambiamento significativo: sembra che il ritardo tra TC-COM e l'elemento di controllo sia la causa principale del delay percepito. È importante considerare questa comunicazione per ottimizzare le prestazioni. Successivamente, ho testato nuovamente la simulazione con i parametri 500, 82, 80, 500, 8 e 5; il modello mantiene comunque un certo ritardo, probabilmente dovuto a una latenza di comunicazione. Nonostante ciò, il sistema risponde in modo soddisfacente. Per verificare la corrispondenza tra simulazione e hardware reale, ho confrontato le variabili ottenute da Simulink con quelle misurate sul TestRig reale. Le variabili sono identiche: 8, 5, 1, 10, 1. Ho confermato che i valori coincidono, quindi la simulazione in TwinCAT è coerente con il comportamento del test rig. Infine, ho impostato le variabili su True per osservare il comportamento del sistema; si nota un’oscillazione di risonanza, ma il modello risponde come previsto. Con questo video, concludo la presentazione e vi auguro buon proseguimento nello studio di TwinCAT, Beckhoff, TestRig e machine learning.
