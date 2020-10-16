# multithreading-python
python project to display multithreading options and race conditions

## Wat is multithreading?  
Multithreading maakt het mogelijk om verschillende taken tegelijk uit te voeren. Een proces kan gebruik maken van meerdere `threads`. Elk proces bevat een eigen geheugensegment waar meerdere threads
toegang tot kunnen verschaffen. 
### Wanneer gebruik je meerdere threads?  
Als je meerdere taken hebt die tegelijkertijd uitgevoerd moeten / kunnen worden.
### Wat zijn drie veel voorkomende problemen bij mutithreaded applications? Waardoor ontstaan ze?  
Race conditions onstaant als beide threads dezelfde taak op hetzelfde moment uit willen voeren
### Hoe wordt het onderdeel genoemd waar objecten in het geheugen worden geplaatst? Hoe is dit verschillend in een multithreaded application?
The Stack is tijdens het uitvoeren van een code block verantwoordelijk voor het opslaan van pointers naar objecten in het geheugen
en het afdwingen van zichtbaarheid van variabelen (scope, public/private). Elke thread heeft zijn eigen stack.
### Hoe wordt het onderdeel genoemd waar methoden worden uitgevoerd en primitive types in het geheugen worden geplaatst? Hoe is dit verschillend in een multithreaded application?
The Heap, hier worden de objecten opgeslagen. The Stack heeft alleen een pointer / verwijzing naar de objecten in The Heap. Alle threads
delen dezelfde heap
### Wat is in dit kader een racing condition? Hoe zou je dit kunnen voorkomen? 
Een race condition kan voorkomen worden op meerdere manieren, een hiervan is bijvoorbeeld een lock. Een lock is een soort gangpas,
een enkele thread kan de lock hebben en als een andere thread de lock wilt hebben, moet deze wachten totdat deze vrijgegeven is.

#### Bronnen
https://techacademy.id.nl/blog/wat-is-multithreading-en-wat-heb-je-er-aan/
https://stackoverflow.com/questions/1665419/do-threads-have-a-distinct-heap
https://realpython.com/intro-to-python-threading/