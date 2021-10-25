# Выделение на изображениях здоровой и поврежденной части листа

В _test хранится база изображений листьев, всего 12 изображений.
В output хранится вывод работы программы. Выводом является изображение, в котором сравниваются различные фильтры для уменьшения шума. А так же используется watersрed с фильтрами и без для выделения здоровой и повреждённой части листа.

Первое столбец - изображение без фильтров и определение здоровой и повреждённой части листа. Второй столбец - изображение с применением фильтра Non-Local Means. Третий столбец - изображение с применением фильтра Bilateral Filter.

Из всех данных в отчете приведены самые интересные варианты выводы программы.

cv2.bilateralFilter()
<ul>
<li>d: 25</li>
<li>sigmaColor: 50</li>
<li>sigmaSpace: 50</li>
</ul>

cv2.fastNlMeansDenoisingColored()
<ul>
<li>src: img</li>
<li>dst: None</li>
<li>h: 80</li>
<li>templateWindowSize: 7</li>
<li>searchWindowSize: 21</li>
</ul>

![Element: вывод 1]("https://github.com/MoskvinSA/Image_processing/tree/master/Lab2/output/1.jpg")

![Element: вывод 2]("https://github.com/MoskvinSA/Image_processing/tree/master/Lab2/output/6.jpg")

![Element: вывод 3]("https://github.com/MoskvinSA/Image_processing/tree/master/Lab2/output/11.jpg")
