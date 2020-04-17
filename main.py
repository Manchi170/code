# def Determinisation():
#     FilePath = input ('Saisir le chemin de votre fichier : ')
#     if(FilePath):
#         FileName = input('Saisir le nom de votre fichier sans extension: ')
#         print (FileName)
#         file = open(FilePath + FileName + ".descr", "r")
#         if(file):
#             for line in file:
#                 line=file.readline()
#                 print(line)
#                 if line.startswith('0') || line.startswith('1') || line.startswith('2'):
#                     for elt in line:
#                         if 

automate = dict()
automate["T"] = dict()

def parser(lines):

  for line in lines:
    if line.startswith("V"):
      parseStates(line, "V")
      print("Entrée:", automate["V"])

    if line.startswith("O"):
      parseStates(line, "O")
      print("sortie:", automate["O"])

    if line.startswith("E"):
      parseStates(line,"E")
      print("Nombre d'états:", automate["E"])
    
    if line.startswith("I"):
      parseStates(line,"I")
      print("Etats initiaux:", automate["I"])
    
    if line.startswith("F"):
      parseFS(line)
      print("\nEtats acceptants:", automate["F"])

    if line.startswith("T"):
      stateTransition(line)
    
def parseStates(line, char):
  automate[char] = line.split(" ")[1]

def parseFS(line):
  automate["F"] = "-".join(line.split(" ")[1:-1])

def stateTransition(line):
  content = line.split(" ")
  automate["T"][content[1] + content[3]] = content[2].replace("'", "") 

def getData(filename):
    parser(filename.readlines())
    print("\nTransitions:", automate["T"])

#filename = input('Saisir le chemin vers votre fichier: ')
#filename = "AS.descr"
FilePath = input ('Saisir le chemin de votre fichier : ')
if(FilePath):
  fileName = input('Saisir le nom de votre fichier sans extension: ')
  file = open(FilePath + fileName + ".descr", "r")
print(getData(file));
transitions = automate["T"]

### ---

stop = False
for i in range(int(automate["E"])):
  res = []
  for j in range(int(automate["E"])):
    t = str(i) + str(j)
    if t in transitions.keys():
      if transitions[t] not in res:
         res.append(transitions[t])
      else:
        stop = True 
    if stop:
      print("Oh la, l'automate est non deterministique")
      break
  if stop:
    break

if not stop:
  print("L'automate est deterministique")


