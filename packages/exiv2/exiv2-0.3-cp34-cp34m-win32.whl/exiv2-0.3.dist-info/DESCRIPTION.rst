=================
What is it?
=================

Low-level wrapper for exiv2 for python >= 3.3 that pip-installs on Windows.

* only works on Windows. 
* only supports Iptc for now. Exif and Xmp are on their  way.
* straight-up exposure of the C++ methods. Feel free to write more pythonic classes on top.

How do I set it up?
-------------------------------

* pip install exiv2

Example
-------------------------------

::

    import exiv2

    def example1():
        image = exiv2.ImageFactory.open(r"c:\test\test.jpg")
        image.readMetadata()
        ipc_data = image.iptcData()
        for datum in ipc_data:
            print(datum.key(), datum.value().toString())
        ipc_data[b'Iptc.Application2.Subject'] = b'subject'
        image.writeMetadata()

    def example2():
        with open(r"c:\test\test.jpg", "rb") as f:
            imdata = f.read()
        im = exiv2.ImageFactory.open(imdata)
        im.readMetadata()               

        new_iptc_data = exiv2.IptcData()    
        new_iptc_data[b"Iptc.Application2.Caption"] = b'Hi Mom!'
        im.setIptcData(new_iptc_data)
        im.clearExifData()
        im.clearXmpData()
        im.writeMetadata()

        io = im.io()
        size = io.size()
        buffer = io.read(size)
        with open(r"c:\test\out.jpg", "wb") as f:
            f.write(buffer)

    if __name__ == '__main__':
        example1()
        example2()



