class p:
    def __init__(self, instruction):
        self.instruction = instruction

class body:
    def __init__(self, segment,  instruction = ''):
        self.instruction = instruction
        self.segment = segment


class MyFile:
    def __init__(self, segment):
        self.segment = segment
    def __str__(self):
        return f'''<html>
<body>
{self.segment.instruction}
<p>
{self.segment.segment.instruction}
</p>
</body>
</html>'''

sentence = p(instruction = 'This is some body text')
my_file2 = body(instruction = 'This is the body', segment = sentence)
my_file1 = MyFile(segment = my_file2)
print(my_file1)
