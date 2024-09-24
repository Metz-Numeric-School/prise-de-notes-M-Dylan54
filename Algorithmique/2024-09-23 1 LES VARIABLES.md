## Python : 

**Variable** = nom/valeur

## Affectation/Déclaration :

**Prénom = "John" ->** déclaration/affectation/initialisation
         **"John" = chaîne de  charactères**


## Exemples de noms de variables : 

**dateJour** = "23-09-2024" 
**AnnéeNaissance** = "2000"

## Conventions de nommage :

**Historiquement :**
**camelCase**
**PascalCase** 

**Propre à Python :**
***snake_case***

**Gardé pour les noms de fichiers ou d'url :**
***kebab-case***

## Types de données :

**Entiers naturels** (integer/int) *nombres ronds*
**Decimaux** (float) *à* *virgule*
**Chaines de charactères** (string/str) *toujours entre ""*
**Booléen** (Boolean/Bool) *True/False*

## Les opérations :

### Entiers :

* `(+) addition`
* `(-) soustraction`
* `(*) multiplication`
* `(//) division entière`
* `(**) puissance`

### String :

* `(+) concatenation`

*ex : "Salut" (+) "ça va" = "Salut ça va"

* `(*) multiplication sur PYTHON uniquement`

*ex : "A" *4 = "AAAA"

### Bool :

* and = ET
* or = OU
* not = NON


### Algèbre de Boole :

| a   | b   | a ET b |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 0      |
| 1   | 0   | 0      |
| 1   | 1   | 1      |


| a   | b   | a OU b |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |


| a   | NON a |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

a = c+1 =7
b = a+b = 10
c = a-b+1 = -2
a = b = 10
c = bx2 =20
b = 10

---

a = 7
b = 5
c = 2
a = bxc
c = a + a
b = cx3 -c
a = a + b + c
c = a - b + c

a = 70
b = 40
c = 50

---


### Opérateurs de comparaison :

***a = = b*** : si a est **STRICTEMENT** **égal** à b
***a ! = b*** : si a est **DIFFERENT** DE b
***a > b*** : si a est **STRICTEMENT** **supérieur** à b
***a < b*** : si a est **STRICTEMENT** **inférieur** à b
***a < = b*** : si a est **inférieur** ou **égal** à b
***a > = b*** : si a est **supérieur** ou **égal** à b

if condition : instruction
indentation : entrée + tab

**exemple 1 :**

`light = 1`
	`if light = = 1 :`
		`print ("J'ouvre les volets")`

**exemple 2 :**

`firstname = input ("Votre nom")`
`if firstname = = "John" :`
		`print ("Bonjour")`
`else :` 
		`print("Au revoir")`    


---

### Boucles :
 * **For** : *boucle comptée (utilisation d'une variable de comptage)*
	 ex: `for i in range(start, end)`
		 *instruction*
		`for i in range(0,5):`
			`print("Hello")`
		
(incrémentation) i=i+1
 end =5 **(La boucle s'arrête quand i = end et le end est exclu donc la boucle s'arrête à end -1)**
 * **While** (Tant que) : boucle conditionnelle*
 *Boucle tant que la condition "c" est vérifiée*

ex: 
`n=1`
`while n!=100`
	`print(n)`
	`n=n+1`


 
 


