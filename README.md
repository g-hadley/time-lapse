# Time-lapse
Time-lapse project using OpenCV

I wrote this program to make it easier for myself to create time-lapse videos without using video editing software or other 3rd party applications. 

### Configuration:
The filetype and codec of the output video may need to be adjusted depending on your OS. The speed of the time-lapse is also adjustable. 

```python
__speed__ = 6                   # Selects every nth frame for the timelapse
__fileExtention__ = ".avi"      # Output filetype
__codec__ = "DIVX"              # Output codec
```

[Windows filetypes](https://support.microsoft.com/en-us/help/3078080/file-formats-supported-by-the-movies-tv-app-in-windows-10)

[Mac filetypes](https://www.lakehorn.com/products/video-file-list/#:~:text=Supported%20File%20Formats)

[Codecs](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html#:~:text=FourCC%20is%20a%204-byte%20code)
