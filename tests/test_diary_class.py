from lib.diary_class import *

def test_init_():
    de = DiaryEntry("Title","Contents")
    result = de.title
    assert result == "Title"
    result2 = de.contents
    assert result2 == "Contents"

def test_format():
    de = DiaryEntry("Title", "Contents")
    result = de.format()
    assert result == "Title: Contents"

def test_count_words():
    de = DiaryEntry("Title", "Contents")
    result = de.count_words()
    assert result == 2

def test_reading_time():
    de = DiaryEntry("Title", "Contents")
    result = de.reading_time(200)
    assert result == "The Reading Time is 0.01 minutes"

def test_reading_chunk():
    de = DiaryEntry("Title", "This is the content of the diary entry.")
    
    # First call, expect to read the entire entry
    result = de.reading_chunk(200, 1)
    assert result == "Title: This is the content of the diary entry."

    # Second call, should return an empty string since all content has been read
    result2 = de.reading_chunk(200, 1)
    assert result2 == ""


