Nodes in the Map: 
names(str), score(float), good/bad(boolean) 


Weights: 

positive connection: 
First degree connection: 1/(the current positive connections) 

Second degree connection: 0.1/(the current positive connections)

negative connections: 
first degree: -1 
second degree: -0.1 

Temporal separation: each year 90% - disabled

Companies and people: treated equally

Parsing: 
1. court cases (JSON)
2. IAPD (XML)
3. Barred Brokers (CSV)
4. NY Corporations (CSV)

