in bar.py use flush    if ,common the line   the data will dont actual write ?
2 the PAGESIZE is 4kB  ,does thas mean the bar memory must large than 4KB? 
        # Flush current page for immediate update.
        page_offset = offset & (~(PAGESIZE - 1) & 0xffffffff)
        self.__map.flush(page_offset, PAGESIZE)
        # TODO: check return value, only for >=Python3.8
