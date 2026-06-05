---
data: 2026-06-05
stato: bozza
---

# Affordance e signifier

Distinzione di Donald Norman tra ciò che un artefatto rende *possibile* e ciò che *comunica* su dove e come agire. È il contributo che l'edizione 2013 di *The Design of Everyday Things* aggiunge al capitolo iniziale — Norman la dichiara «the most important addition to the chapter» — e completa il vocabolario del ciclo di azione: i sette stadi descrivono il *processo* dell'interazione, affordance e signifier descrivono come l'artefatto la *invita*. Per il metodo è il criterio che governa lo strato output prima ancora che l'utente decida di agire: un nodo o una vista non sono corretti solo perché ben formati, lo sono se segnalano l'azione possibile a chi li legge.

Norman riprende *affordance* da J. J. Gibson e la piega a uso proprio: non una proprietà dell'oggetto ma una *relazione* tra oggetto e agente. È la sorgente di gran parte della confusione sul termine — «Many people find affordances difficult to understand because they are relationships, not properties». Il *signifier* è la parte che segnala, e Norman lo introduce nel 2013 perché la comunità del design aveva piegato "affordance" a indicare il *segnale* (l'icona da toccare su uno schermo), collassando due cose distinte: l'azione possibile e l'indicazione di dove compierla.

## Affordance: una relazione, non una proprietà

L'affordance è «the possibilities in the world for how an agent (a person, animal, or machine) can interact with something». Non vive nell'oggetto né nell'agente, ma nel loro accoppiamento: una superficie piatta a mezz'altezza *affords* l'appoggio per un essere umano adulto, non per un neonato. Le affordance esistono anche quando non sono percepibili — «Affordances exist even if they are not visible» — e per il design conta la loro *visibilità*: un'affordance percepita aiuta a capire quali azioni sono possibili senza bisogno di etichette o istruzioni.

Due casi limite chiariscono il concetto. L'*anti-affordance* impedisce un'azione (un muro che blocca la caduta nella tromba delle scale). La *perceived affordance* può essere falsa: una superficie può sembrare premibile senza esserlo — è un signifier ingannevole, talvolta accidentale, talvolta deliberato (i giochi vivono di questo).

## Signifier: dove e come agire

Il signifier è «any mark or sound, any perceivable indicator that communicates appropriate behavior to a person». La distinzione cardine, nelle parole di Norman: «Affordances determine what actions are possible. Signifiers communicate where the action should take place. We need both». L'affordance dice *cosa* è possibile; il signifier dice *dove e come* farlo.

I signifier possono essere deliberati (la scritta PUSH su una porta) o accidentali (il segnaposto in un libro segnala la propria posizione, ma anche — senza intenzione — quanto manca alla fine; un lettore lo usa per regolarsi). Per chi riceve il segnale la differenza non conta: «It doesn't matter whether the useful signal was deliberately placed or whether it is incidental». Ciò che un buon design deve garantire è la comunicazione di scopo, struttura e funzionamento dell'oggetto a chi lo usa: quello è il ruolo del signifier.

## Perché conta per il metodo

Un artefatto del metodo — un nodo `kb/`, un quadro, una vista di output — ha *affordance* (quali azioni rende possibili a chi lo legge) e ha bisogno di *signifier* (cosa dice al lettore dove e come agire). Gran parte del lavoro dello strato output, in particolare L2, è aggiunta di signifier: il termometro, lo schema, la raccomandazione accanto allo stato non creano nuove azioni possibili, segnalano quelle che già esistono. La provocazione registrata nel ciclo di azione — «se l'utente non agisce, la KB è mal progettata, non l'utente è pigro» — si affina qui: spesso non manca l'affordance (l'azione era possibile) ma il signifier (niente la segnalava).

Il dettaglio che fonda testualmente l'estensione del metodo è nella definizione stessa: l'agente che interagisce è «a person, animal, **or machine**». Norman nomina la macchina tra gli agenti. La KB ha quindi affordance e signifier per *due* agenti che la leggono — l'umano e l'LLM — e i due strati output ne sono la conseguenza: L1 porta i signifier di cui ha bisogno l'agente macchina (fatti strutturati, scadenze esplicite), L2 quelli di cui ha bisogno l'agente umano (vista leggibile a colpo d'occhio). Un nodo ben *segnalato* per l'umano può essere muto per la macchina, e viceversa. La distinzione affordance/signifier dà il criterio per progettare entrambi senza confonderli, ed è il completamento naturale delle quattro proprietà cardine già usate come criteri di qualità per L2.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition (Basic Books, 2013), Cap. 1 "The Psychopathology of Everyday Things", sezioni _Affordances_ e _Signifiers_. Il signifier è l'aggiunta dichiarata dell'edizione 2013 («Signifiers are the most important addition to the chapter»); l'affordance era già nella prima edizione (1988), dove Norman introdusse il termine nel mondo del design.
- Fonte grezza (i1): EPUB dell'edizione 2013 in `sources/`, manifest in `sources/README.md`.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [system-image](system-image.md)
- [visceral-behavioral-reflective](visceral-behavioral-reflective.md)
- [ponte](ponte.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [metodo-kb](metodo-kb.md)
