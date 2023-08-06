# Buzon - ZipFly

ZipFly is a zip archive generator based on zipfile.py.
It was created by Buzon.io to generate very large ZIP archives for immediate sending out to clients, or for writing large ZIP archives without memory inflation.

# Requirements
Python 3.5+

# Install
    pip3 install zipfly

# Basic usage, compress on-the-fly during writes
Basic use case is compressing on the fly. Some data will be buffered by the zipfile deflater, but memory inflation is going to be very constrained. Data will be written to destination at fairly regular intervals.

`ZipFly` default attributes:

- <b>paths:</b> [ ] <br/>
- <b>mode:</b> w <br/>
- <b>chunksize:</b> (bytes) 16384 <br/>
- <b>compression:</b> Stored <br/>
- <b>allowZip64:</b> True <br/>
- <b>compresslevel:</b> None <br/>
- <b>storesize:</b> (bytes) 0 <br/>


<br/>

`paths` required keys:
<pre>
- @key (filesystem) <b>'fs'</b> -> path from your disk <br />
- @key (name) <b>'n'</b> -> final name in zip file
</pre>

```python
    import zipfly
    
    paths = [ 
        {
            'fs': 'home/user/Videos/jupiter.mp4', 
            'n': 'movies/jupiter.mp4', 
        },       
        {
            'fs': 'home/user/Documents/mercury.mp4', 
            'n': 'movies/mercury.mp4', 
        },          
    ]

    zfly = zipfly.ZipFly( paths = paths )

    with open("test.zip", "wb") as f:
        for i in zfly.generator():
            f.write(i)


```

## Examples


### Create a ZIP file with size estimation.
Use the `PredictionSize` to compute the correct size of the resulting archive.

```python
    import zipfly
    
    ss = 92896201 # (file.mp4 + background.jpg) size in bytes
    
    zfly = zipfly.ZipFly( paths=paths, storesize=ss )

    print ( zfly.buffer_prediction_size() )
    # 92896795

```


### Django - Streaming multiple files in a zip
The easiest is to use the Django' built-in streaming feature:

```python
    
    from django.http import StreamingHttpResponse
    import zipfly

    zfly = zipfly.ZipFly( mode='w', paths=paths )
    
    z =  zfly.generator()
    print (z)
    # <generator object generator at 0x7f85aad60b13>

    response = StreamingHttpResponse(
        z, content_type='application/octet-stream'
    )          

    return response 
```

### Streaming a large file
Efficient way to read a single very large binary file in python

```python
    import zipfly

    file_location = '/home/user/Documents/file-100-GB.csv'

    go_to_streaming = zipfly.from_one_file(file_location)
    
    print (go_to_streaming)
    # <generator object from_one_file at 0x7f85aad34a50>
    
```

# License
This library was created by Buzon.io and is released under the MIT. Copyright 2019 Grow HQ, Inc.