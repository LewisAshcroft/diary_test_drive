class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_position = 0



    def format(self):
        return f"{self.title}: {self.contents}"



    def count_words(self):
        text = self.format()
        list = text.split()
        return len(list)

    def reading_time(self, wpm):
        word_count = self.count_words()
        minutes = word_count / wpm
        return f"The Reading Time is {minutes:.2f} minutes"
        

    
    def reading_chunk(self, wpm, minutes):
        max_words = wpm * minutes
        full_text = self.format()
        words = full_text.split()

        # If we've already read all the words, reset the read position
        if self.read_position >= len(words):
            self.read_position = 0  # Reset for the next read
            return ""  # Return empty string if everything has been read

        # Get the next chunk of words to read
        chunk = words[self.read_position:self.read_position + max_words]
        self.read_position += len(chunk)  # Update read position

        # Return the joined chunk
        return ' '.join(chunk)


