from pycricbuzz import Cricbuzz
import  json
c=Cricbuzz()
#id=20790 india vs nz
#id=21259 eng vs wi
str=c.matches()
print(str)
print((json.dumps(str,indent=4,sort_keys=False)))
print(str[0]['status'])
#print(c.livescore('21259'))
