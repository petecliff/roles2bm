import configparser
import sys
import getopt
from datetime import datetime

inputFilename = ''
outputFilename = ''
outputFormat = 'netscape'
urlTemplate = 'https://signin.aws.amazon.com/switchrole?account={}&roleName={}&displayName={}'

def notSet(value):
    return len(value) == 0

opts, args = getopt.getopt(sys.argv[1:], "i:o:f:")
for opt, arg in opts:
    if opt == '-i':
        inputFilename = arg
    elif opt == '-o':
        outputFilename = arg
    elif opt == '-f':
        outputFormat = arg

if notSet(inputFilename) or notSet(outputFilename):
    print('\nUsage: {} inputfile outputfile\n'.format(sys.argv[0]))
    sys.exit()

extendRolesConfig = configparser.ConfigParser()
extendRolesConfig.read(inputFilename)

bookmarkFpo = open(outputFilename, "w")
bookmarkFpo.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <Title>Bookmarks</Title>
    <H1>Bookmarks</H1>
    <DL>\n""")

addmod = int(datetime.timestamp(datetime.now()))

bookmarkFpo.write('<DT><H3 FOLDED ADD_DATE="{}">AWS Role Switcher Import</H3>\n<DL><p>'.format(addmod));
for section in extendRolesConfig.sections():
    roleConfig = extendRolesConfig[section]
    url = urlTemplate.format(roleConfig['aws_account_id'], roleConfig['role_name'], roleConfig['role_name'])
    bookmarkFpo.write('<DT><A HREF="{}" ADD_DATE="{}" LAST_MODIFIED="{}">{}</A>\n'.format(url, addmod, addmod, roleConfig['role_name']))

bookmarkFpo.write('</DL><p></DL>\n')

bookmarkFpo.flush()
bookmarkFpo.close()

print("Done")