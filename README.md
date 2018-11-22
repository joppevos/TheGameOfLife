
![giphy](https://user-images.githubusercontent.com/44348300/48576623-51c12e80-e915-11e8-8f4a-613e813a631f.gif)
# The Game Of Life
A non-optimized version of the game of life. An evolution game determined by the first planted seed.
"The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway"

## Starting in Cinema4D
To get started in Cinema 4D, you have to extract numpy in `{cinemaversion}/library/python/packages/{osx/win64}.`
copy the complete content of c4d.py inside the script editor and run. 

check out the video below by clicking the image.
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/44348300/48920945-5731f200-ee9c-11e8-9899-4b5bde1d0c44.png
)](https://www.youtube.com/watch?v=4DkYb_OAxb8)


## Starting in matplotlib
To get started just fork or copy the `life.py` content.
You will need the modules Numpy and Matplotlib
pip install them both this way.


`pip install matplotlib numpy`

In the dictionary seeds you can find all the names of the containing seeds.
Place the seed in the universe by calling the name. 
example: `strseed = 'pentadecathlon'`
K
parameters to set:
- set the size `n = 100` for the grid size. (go easy on the size)
- set the interval `interval=500` in milliseconds between each generation. 

If you keep the seed empty. A random grid like the image below will be generated.
![giphy 1](https://user-images.githubusercontent.com/44348300/48577331-36572300-e917-11e8-8278-78e55e0bf4ef.gif)

