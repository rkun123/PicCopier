# Pic Copier
---
## Overview
This is a script written in Python.  
You can copy picture from Camera automatically.

## Description
Copy files even aren't "hoge.jpg".   
Check timestamp of EXIF or of OS and if datefile don't exist, it make new one.
It doesn't work custom folder format yet...

## Usage
### Requirements
- Python 3.5.7
- pillow 3.3.1
- (pip 8.1.2 or later)

### Run
```
> cd {YourStoringFolder}/PicCopier
> python app.js {Path of folder copy from} {Path of folder copy into}
```
### Formats
Foldername `yyyymmdd`

## Licence
```
The MIT License (MIT)

Copyright (c) 2017 rkun123

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```