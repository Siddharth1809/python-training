import re

# basic of raw_string
# print('\tTab')
# print(r'\tTab')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
123*555*1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a sentence and then bring it to an end'
# search literal character

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)  # returns span with start and end index with match='abc'

# span indexes are useful because it allows us to use string slicing functionality as below
print(text_to_search[1:4])

pattern_url = re.compile(r'coreyms.com')
matches_url = pattern_url.finditer(text_to_search)
for match_url in matches_url:
    print(match_url)

print(text_to_search[127:138])

# pattern_phone_no = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# matches_url_phone_no = pattern_phone_no.finditer(text_to_search)

# with open('data.txt', 'r',encoding='utf-8') as data_file:
#    contents = data_file.read()
#    pattern_phone_no = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')      # to get phone numbers started with 8 or 9
#    matches_url_phone_no = pattern_phone_no.finditer(contents)
#    for match_url_phone_no in matches_url_phone_no:
#        print(match_url_phone_no)


pattern_url_all = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches_url_all = pattern_url_all.finditer(urls)
for match_url_all in matches_url_all:
    print(match_url_all.group())
    print(match_url_all.group(1))
    print(match_url_all.group(2))
    print(match_url_all.group(3))

subbed_url = pattern_url_all.sub(r'\2\3', urls)

print("Subbed_url:", subbed_url)
