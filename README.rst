=======
vec2img
=======

convert OpenCV samples file to images

------------
Installation
------------

    $ pip install vec2img

-----
Usage
-----

    $ vec2img samples.vec -o images -w 24 -h 24 -e png

----
Help
----

    $ vec2img --help
    usage: vec2img -o OUT [-w WIDTH] [-h HEIGHT] [-e EXT] [--version] [--help] vec
    
    convert OpenCV samples file to images
    
    positional arguments:
      vec                   vec file
    
    optional arguments:
      -o OUT, --out OUT     output path (default: None)
      -w WIDTH, --width WIDTH
                            image width (default: 24)
      -h HEIGHT, --height HEIGHT
                            image height (default: 24)
      -e EXT, --ext EXT     image extension (default: png)
      --version             show program's version number and exit
      --help                show this help message and exit
