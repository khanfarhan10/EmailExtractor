"""
python EmailExtractor.py
"""

import re
import os


def load_txt_as_str(txt_filepath):
    with open(txt_filepath, 'r') as fh:
        string = fh.read()
    return string


def NumberofDigits(num):
    d = 0
    for c in num:
        if c.isdigit():
            d = d+1
    return d


def FilterValidPhoneNums(nums):
    new_nums = []
    for each in nums:
        digi = NumberofDigits(each)
        if (digi >= 10):
            new_nums.append(str.strip(each))

    return new_nums


def EmailExtract(txt):
    ValidatedAtDotEmailRegex = r"([a-z0-9\.\-+_]+(?:@|\[at\])[a-z0-9\.\-+_]+(?:(?:\.|\[dot\])[a-z]+)+)"
    emailMatch = re.findall(ValidatedAtDotEmailRegex, txt)
    return emailMatch


def PhoneExtract(txt):
    PhoneRegex = '[\+]*[\s]*[0-9]+[\s]*[\(]*[\s]*[0-9]+[\s]*[\)]*[\s]*[\s|0-9]+'
    phoneMatch = re.findall(PhoneRegex, txt)
    # phoneMatch  # FilterValidPhoneNums(phoneMatch)
    FilteredPhoneMatch = FilterValidPhoneNums(phoneMatch)
    return FilteredPhoneMatch


def solve(string):
    """
    Emails :
    client@server.com
    client[at]server[dot]com
    client@server[dot]com
    client[at]server.com

    non-capturing group: (?:s|season)
    OrigEmailRegex = '(\S+(@|\[at\])\S+(\.|\[dot\])\S+)'
    GeneralEmailRegex = '(\S+(?:@|\[at\])\S+(?:\.|\[dot\])\S+)'
    ValidatedEmailRegex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    """
    ValidatedAtDotEmailRegex = r"[a-z0-9\.\-+_]+(?:@|\[at\])[a-z0-9\.\-+_]+(?:\.|\[dot\])[a-z]+"
    EmailRegex = ValidatedAtDotEmailRegex

    """
    Phone Numbers :
    https://grokonez.com/python/python-regular-expression-to-extract-phone-number-example
    +xx(country code) num
    
    
    PhoneRegex = '[\+\(]?[1-9][0-9 .\-\(\)]]{9,}[0-9]'
    PhoneRegex = r'''(
    ...    [(]?(\d{3})?[)]? # area code
    ...    (\s|-|\.)? # separator
    ...    (\d{3}) # first 3 digits
    ...    (\s|-|\.) # separator
    ...    (\d{4}) # last 4 digits
    ...    (\s|,) # separator
    ...    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension)'''
    
    maybe + Sign maybe spaces or ( maybe numbers maybe spaces or ) the maybe spaces and nums
    +60 (0)3 2723 7900</p> +6 (03) 8924 8000
    9663508766
    """

    PhoneRegex = '[\+]*[\s]*[0-9]+[\s]*[\(]*[\s]*[0-9]+[\s]*[\)]*[\s]*[\s|0-9]+'
    emailMatch = re.findall(EmailRegex, string)
    phoneMatch = re.findall(PhoneRegex, string)
    # phoneMatch  # FilterValidPhoneNums(phoneMatch)
    FilteredPhoneMatch = FilterValidPhoneNums(phoneMatch)
    return emailMatch, FilteredPhoneMatch


if __name__ == '__main__':
    ROOT_DIR = os.getcwd()
    FilePath = os.path.join(ROOT_DIR, "Data", "SampleJargon.txt")
    txt = load_txt_as_str(FilePath)
    print("File Loaded.")
    print("File Contents :")
    print(txt)
    print("Analyzing :")
    emailMatch, phoneMatch = EmailExtract(txt), PhoneExtract(txt)
    print("Emails:")
    for email in emailMatch:
        print(email)
    print("Phone Numbers:")
    for ph in phoneMatch:
        print(ph)
