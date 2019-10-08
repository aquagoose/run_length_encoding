# run_length_encoding
**A Run Length Encoding compressor and decompressor written by Ollie Robinson**
## Commands
**run_length_encoding supports 2 different commands.**
### compress(text)
Fairly simple. All you need to do is write compress(TEXT_HERE) and the text (*string*) you want to compress goes in the brackets.<br />
*This command needs to be assigned to a variable or used in the print() command*<br />
E.G. print(compress("Hello!")
### decompress(text, mode)
The first bit is the same as compress(text). Enter a string you want to decompress in the first variable. <br />
*MODE*: Mode has one of two options: 1 or 2.<br />
MODE 1: a "99-character limit" mode. This mode works with numbers, however only allows up to 99 characters. E.G. "99a" would work but "100a" would not. YOU MUST ALSO enter 2 numbers every time. "1a" would not work but "01a" would.<br />
MODE 2: Allows infinite characters E.G. "1457a" however does not work with numbers so "14578" (to print 1457 8's) would not work.
