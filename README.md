
  
## Wat is multithreading? 
Multithreading maakt het mogelijk om verschillende taken tegelijk uit te voeren. Een proces kan gebruik maken van meerdere `threads`. Elk proces bevat een eigen geheugensegment waar meerdere threads toegang tot kunnen verschaffen.  
### Wanneer gebruik je meerdere threads? 
Meerdere threads gebruik je als er meerdere taken zijn die parallel uitgevoerd moeten / kunnen worden. Zo kunnen de threads afzonderlijk van elkaar data bij elkaar verzamelen en er iets mee doen.
## Wat zijn drie veel voorkomende problemen bij mutithreaded applications? Waardoor ontstaan ze? 
Er zijn meerdere veel-voorkomende problemen bij multithreaded applicaties, denk hierbij aan memory-interference, race conditions (als 2 of meerdere threads dezelfde data benaderen en aan willen passen) en deadlocks (als 2 of meerdere processen elkaar in de weg zitten). Daarnaast wordt de complexiteit van de applicatie ook nog groter waardoor het debuggen ingewikkelder wordt. 

Bij race conditions doen 2 of meer threads hetzelfde object in het geheugen lezen en schrijven, waardoor er een onverwacht resultaat kan optreden. Door de complexiteit binnen een multithreaded applicatie wordt het lastig debuggen, want bijv een race condition geeft je een onverwacht resultaat maar geen foutmelding. Als je dan moet zoeken, kun je een behoorlijke investering aan tijd verwachten.  
## Hoe wordt het onderdeel genoemd waar objecten in het geheugen worden geplaatst? Hoe is dit verschillend in een multithreaded application? 
Objecten worden in The Heap geplaatst, waarbij de Stack een pointer heeft naar het object in het geheugen. In een multithreaded applicatie is hier geen verschil, alle threads hebben toegang tot de objecten in The Heap.  
## Hoe wordt het onderdeel genoemd waar methoden worden uitgevoerd en primitive types in het geheugen worden geplaatst? Hoe is dit verschillend in een multithreaded application? 
Methoden en primitive typen worden geplaatst in The Stack. The Stack heeft pointers naar objecten in het geheugen die zich bevinden in The Heap. In een multithreaded applicatie heeft iedere thread zijn eigen stack. In The Stack worden elementen middels een **Last In First Out** (LIFO) volgorde verwerkt, vergelijkbaar met een stapel borden: je pakt de bovenste, als er een nieuw bord bij komt gaat die ook weer als eerste weg.  
## Wat is in dit kader een racing condition? Hoe zou je dit kunnen voorkomen?
 Een race condition doet zich voor als 2 of meer threads hetzelfde object in het geheugen tegelijkertijd willen lezen en bewerken. Een race condition kan voorkomen worden op meerdere manieren, een hiervan is bijvoorbeeld een lock. Een lock is een soort gangpas, een enkele thread kan de lock hebben en als een andere thread de lock wilt hebben, moet deze wachten totdat deze vrijgegeven is. Er moet wel op gelet worden dat een thread de lock vrijgeeft voor een volgend proces, anders kom je uit op een zogeheten deadlock.
    
## Bronnen
 https://techacademy.id.nl/blog/wat-is-multithreading-en-wat-heb-je-er-aan/    
https://stackoverflow.com/questions/1665419/do-threads-have-a-distinct-heap    
https://realpython.com/intro-to-python-thr    
https://dzone.com/articles/top-15-java-multithreading-concurrency-interview-q    
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_synchronizing_threads.htm