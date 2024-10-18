# Домашнее задание по дисциплине «финишные и абразивные методы обработки»
Домашнее задание предусматривает рассчитать и проанализировать составляющие высоты неровностей профиля шероховатости для заданных условий наружного продольного точения заготовки из конструкционной стали. 
### Рекомендована последовательность этапов расчета: 
- кинематической составляющей
- составляющей высоты неровностей, вызванной пластическим оттеснением материала заготовки
- параметров срезаемого слоя, угла схода стружки, радиальной составляющей силы для несвободного косоугольного резания
- составляющей высоты неровностей от колебаний инструмента в радиальном направлении
- суммарной составляющей неровностей профиля с учетом влияния скорости и износа инструмента.

### На основную форму вывести: 
1. Исходные данные в соответствии с вариантом
2. Результаты расчета
3. Графики зависимостей **h<sub>1</sub>**, **h<sub>2</sub>**, **h<sub>3</sub>**, **R<sub>z</sub> = f(s)** в диапазоне подач **s = 0,08-0,6 мм/об**.

>_Расчетный алгоритм реализован в виде программы на языке программирования Python._
# Вариант 2
### Исходные данные:

| Марка материала | R<sub>zi</sub> | R<sub>zb</sub> | λ | φ | φ<sub>1</sub> | γ | r | ρ | h<sub>z</sub> | v | t | s |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Д16 | 20 | 0.6 | 7 | 30 | 10 | 20 | 0.4 | 0.01 | 0.2 | 350 | 1 | 0.2 |


>_Принять задний угол **α = 7 град**, жесткость технологической системы в радиальном направлении составляет **j = 25 Н/мкм**_
