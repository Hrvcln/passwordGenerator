import hashlib
import sys
import getpass
import string

letters = string.ascii_letters + string.digits + '!#$%&()*+-:;<=>?@[]{}'
letters_size = len(letters)

graine = sys.argv[1].encode('utf-8')
taille = int(sys.argv[2])

passphrase = getpass.getpass('Passphrase : ').encode('utf-8')

m = hashlib.new('sha256')
m.update(graine)
m.update(passphrase)
digest = m.hexdigest()

mdp = ''

for i in range(taille):
    val = int(digest[2*i] + digest[2*i+1],16)
    val = int((val*(letters_size-1)) / 0xff)
    mdp += letters[val]

print(mdp)

