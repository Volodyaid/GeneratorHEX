# GeneratorHEX
GeneratorHEX is a program for subsequent code generation in hexadecimal format  
GeneratorHEX - программа для последовательной генерации чисел в hex формате.  
Её можно использовать для получения последовательных энтропий мнемонических  
сид фраз.  

Запускается в консоли Linux командой:  

./GeneratorHEX 262348096919201814893479671364124123574 add (sub)  

число приведено для примера, программа далее его переводит в c55e67d37fc26e0a13bd03717d1fa1b6  
и последовательно 100000000 раз прибавляет число 1 (если вместо add написать sub -  
программа будет производить вычитания)  

Во время работы программы вы будете видеть, с какой скоростью генерируются хэши  
и сколько интераций произошло.  

100000000 итераций выбрано мною как наиболее часто применяемое при создании различных баз,  
как по времени, так и по используемому дисковому пространству.  
.........................................  
GeneratorHEX is a program for sequential generation of numbers in hex format.  
It can be used to obtain sequential entropies of mnemonic  
seed phrases.  

It is launched in the Linux console with the command:  

./GeneratorHEX 262348096919201814893479671364124123574 add (sub)  

the number is given as an example, the program then translates it to c55e67d37fc26e0a13bd03717d1fa1b6  
and sequentially adds the number 1 100,000,000 times (if you write a sub instead of add  
, the program will make subtractions)  

While the program is running, you will see how fast the hashes are generated  
and how many iterations have happened.  

I chose 100,000,000 iterations as the most frequently used when creating various databases,  
both in terms of time and disk space used.  

..........................................    

GeneratorHEX_V2 - в этой версии вы сами решате, какое количество итераций  
необходимо выполнить.  

Запускается командой:  
./GeneratorHEX 262348096919201814893479671364124123574 add 100000  

В этом примере будет выполнено 100000 сложений.  

.........................................  

GeneratorHEX_V2 - in this version, you decide for yourself how many iterations  
you need to perform.  

It is started by the command:  
./GeneratorHEX 262348096919201814893479671364124123574 add 100000  

In this example, 100,000 additions will be performed  

