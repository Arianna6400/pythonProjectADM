# 🍻 Progetto Software per la Gestione di un Pub

## 📖 Descrizione

Questo progetto è un sistema informativo per la gestione di un pub. Il software è stato sviluppato come progetto per il corso di Ingegneria del Software presso l'Università Politecnica delle Marche, Anno Accademico 2020/2021.

Il sistema consente di gestire vari aspetti della gestione del pub, tra cui:

* 🔐 Login e autenticazione per amministratori e clienti
* 📅 Gestione delle prenotazioni
* 📜 Gestione del menu
* 🏬 Gestione del magazzino
* 👥 Gestione dei dipendenti
* 📝 Gestione delle ordinazioni

La documentazione relativa alla fase di progettazione è visualizzabile qui: [Documentazione progetto](https://github.com/Arianna6400/pythonProjectADM/blob/master/Documentazione%20progetto.pdf)

## ⚙️ Funzionalità

### 🔐 Login

**Amministratore**: Accesso tramite username "Admin" e password "666".

**Cliente**: Accesso tramite nome della prenotazione e numero del tavolo.

### 📅 Prenotazioni

* Aggiunta di nuove prenotazioni con dettagli quali nome cliente, numero di telefono, numero di persone, data e orario.
* Visualizzazione delle prenotazioni giornaliere tramite un calendario.
* Cancellazione delle prenotazioni.

### 📜 Menu

* Visualizzazione del menu completo.
* Aggiunta, modifica e eliminazione di elementi del menu (nome, prezzo, ingredienti e quantità).

### 🏬 Magazzino

* Visualizzazione della lista degli ingredienti disponibili con relative quantità.
* Aggiunta di nuovi ingredienti o modifica di quelli esistenti.
* Cancellazione degli ingredienti.

### 👥 Dipendenti

* Visualizzazione della lista completa dei dipendenti con dettagli anagrafici.
* Aggiunta di nuovi dipendenti.
* Cancellazione dei dipendenti esistenti.

### 📝 Ordinazioni

* Visualizzazione delle ordinazioni effettuate dai clienti.
* Aggiunta di nuovi ordini da parte dei clienti.
* Conferma e invio degli ordini all'amministratore.
* Eliminazione delle ordinazioni.

## 🛠️ Installazione e utilizzo

Per utilizzare l'applicazione è necessario seguire i seguenti passaggi:

1. Clonare la repository ed entrare nella directory:

```bash
git clone https://github.com/Arianna6400/pythonProjectADM
cd pythonProjectADM
```

2. Per eseguire l'applicazione, è necessario aver installato [PyQt5](https://pypi.org/project/PyQt5/), un set completo di binding Python per Qt v5. Essendo l'intera interfaccia grafica sviluppata grazie a Qt, è fondamentale avere tale componente installata. Per avere PyQt installato, è sufficiente eseguire il comando:

```bash
pip install PyQt5
```
> La seguente applicazione è stata sviluppata con versione di Python 3.9.5. Potrebbe non funzionare con versioni più recenti.

3. Una volta posizionati all'interno della directory principale, è possibile eseguire l'applicazione, avviando l'interfaccia principale, attraverso il comando:

```bash
python3 main.py
```

## 🧪 Test 

I test sono stati sviluppati con il framework [PyUnit](https://wiki.python.org/moin/PyUnit). Per eseguire i test, si può utilizzare il seguente comando:

```bash
python -m unittest discover -s tests
```

## ✨ Autori

|Nome | GitHub |
|-----------|--------|
| 👩 `Agresta Arianna` | [Click here](https://github.com/Arianna6400) |
| 👨 `Balducci Davide` | [Click here](https://github.com/Davide-Balducci) |
| 👨 `Xu Marco` | [Click here](https://github.com/Marco-Xu) |
