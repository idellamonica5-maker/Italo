# Introduzione

SymPy è una libreria Python per la matematica simbolica che consente di manipolare espressioni algebriche, risolvere equazioni e fare calcoli analitici in modo esatto. Per questo task è richiesto di implementare alcune funzioni utilizzando la libreria SymPy.

# Istruzioni

- Esegui il fork di questo progetto e assicurati che il tuo repository sia pubblico. Quindi, importa il progetto nel tuo IDE (es. PyCharm).
- Non puoi cambiare la firma delle funzioni fornite (nel file `task.py`) né rinominarle.
- Non puoi interagire con i tuoi colleghi: lavora individualmente e fai del tuo meglio.
- Le funzionalità da implementare sono descritte tramite un insieme di sub-task.
- Implementa le funzioni una alla volta, seguendo rigorosamente l’ordine fornito dai sub-task. Non leggere in anticipo le sub-task successive.
- Un sub-task può considerarsi completato quando sei sicuro che la funzionalità richiesta sia stata implementata correttamente.
- Ogni volta che completi un sub-task, esegui il commit e il push del codice.
- Al termine del compito, assicurati di aver eseguito il push di tutto il progetto sul repository.

# Sub-task

Ricordati di leggere e implementare i sub-task uno alla volta, seguendo l’ordine fornito. Non passare al sub-task successivo finché quello corrente non è stato completato. Implementa le funzionalità richieste lavorando nel file `task.py`.

---

## Sub-task 1 – Calcolare una Derivata

La derivata di una funzione è una misura di quanto rapidamente il valore della funzione cambia rispetto alla variazione della sua variabile indipendente.

### Requisito

Implementa la funzione:

```python
calcola_derivata(espressione: str, variabile: str) -> sympy.Expr
````

Questa funzione riceve l’espressione matematica sotto forma di stringa e restituisce la derivata come oggetto di tipo espressione SymPy.

### Esempi

```python
Input: expression = "x**3", variable = "x"
Output: 3*x**2
```

```python
Input: expression = "sin(x)", variable = "x"
Output: cos(x)
```

```python
Input: expression = "x**2 + y**2", variable = "y"
Output: 2*y
```

---

## Sub-task 2 – Calcolare un Integrale Definito

L’integrale definito permette di calcolare l’area sottesa da una funzione in un intervallo specifico.

### Requisito

Implementa la funzione:

```python
calcola_integrale_definito(
    espressione: str,
    variabile: str,
    estremo_inf: float,
    estremo_sup: float
) -> sympy.Expr
```

Questa funzione riceve in input l’espressione da integrare, la variabile di integrazione e gli estremi inferiore e superiore dell’intervallo. Deve restituire il valore dell’integrale definito calcolato su tale intervallo.

### Esempi

```python
Input: espressione = "x", variabile = "x", estremo_inf = 0.0, estremo_sup = 1.0
Output: 0.5
```

```python
Input: espressione = "x**2", variabile = "x", estremo_inf = 0.0, estremo_sup = 3.0
Output: 9.0
```

---

## Sub-task 3 – Calcolare un Limite

Il limite di una funzione è il valore a cui essa tende quando la sua variabile indipendente si avvicina a un certo punto.

### Requisito

Implementa la funzione:

```python
calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr
```

Questa funzione riceve in input l’espressione matematica, la variabile rispetto a cui calcolare il limite e il punto a cui tale variabile tende. Deve restituire il valore del limite della funzione in quel punto.

### Esempi

```python
Input: espressione = "sin(x)/x", variabile = "x", punto = "0"
Output: 1
```

```python
Input: espressione = "1/x", variabile = "x", punto = "oo"
Output: 0
```

```python
Input: espressione = "(x**2 - 1)/(x - 1)", variabile = "x", punto = "1"
Output: 2
```

---

## Sub-task 4 – Calcolare una Serie di Taylor

La serie di Taylor consente di approssimare una funzione mediante un polinomio costruito a partire dalle sue derivate in un punto.

### Requisito

Implementa la funzione:

```python
calcola_polinomio_taylor(
    espressione: str,
    variabile: str,
    punto: float,
    ordine: int
) -> sympy.Expr
```

Questa funzione riceve in input l’espressione della funzione, la variabile indipendente, il punto di espansione e l’ordine del polinomio da calcolare. Deve restituire il polinomio di Taylor troncato fino all’ordine specificato, escludendo il termine di resto, indicato con “O grande”.

La “O grande” indica tutti i termini di ordine superiore che non vengono scritti esplicitamente nel polinomio di Taylor, perché diventano sempre meno importanti vicino al punto di espansione.

Ad esempio, scrivere:

```text
e^x = 1 + x + x^2/2 + O(x^3)
```

significa che stiamo trascurando termini come:

```text
x^3/6, x^4/24, ...
```

il cui contributo è dell’ordine di `x^3` o superiore.

### Esempi

```python
Input: espressione = "exp(x)", variabile = "x", punto = 0.0, ordine = 4
Output: x**3/6 + x**2/2 + x + 1
```

```python
Input: espressione = "sin(x)", variabile = "x", punto = 0.0, ordine = 4
Output: -x**3/6 + x
```

```python
Input: espressione = "cos(x)", variabile = "x", punto = 0.0, ordine = 3
Output: 1 - x**2/2
```

---

## Sub-task 5 – Risolvere un Sistema Lineare

Un sistema lineare è un insieme di equazioni lineari che condividono le stesse variabili e devono essere soddisfatte simultaneamente.

### Requisito

Implementa la funzione:

```python
risolvi_sistema_lineare(
    eq1: str,
    eq2: str,
    var1: str,
    var2: str
) -> Dict[sympy.Symbol, sympy.Expr]
```

Questa funzione deve risolvere un sistema composto da due equazioni lineari in due incognite.

In SymPy, le espressioni fornite vengono interpretate come uguali a zero (ad esempio, `x + y - 3` equivale a `x + y - 3 = 0`).

La funzione riceve in input la prima equazione del sistema, la seconda equazione e i nomi delle due variabili incognite.

Deve restituire un dizionario in cui le chiavi sono i simboli delle variabili e i valori sono le soluzioni calcolate del sistema.

### Esempi

```python
Input: eq1 = "x + y - 3", eq2 = "x - y - 1", var1 = "x", var2 = "y"
Output: {x: 2, y: 1}
```

```python
Input: eq1 = "2*x + y - 5", eq2 = "x + 3*y - 5", var1 = "x", var2 = "y"
Output: {x: 2, y: 1}
```

```python
Input: eq1 = "x - 2*y", eq2 = "x + y - 3", var1 = "x", var2 = "y"
Output: {x: 2, y: 1}
```