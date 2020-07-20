
import matplotlib.pyplot as plt
import base64
import requests

# mount your drive and change location as desired
dir = '/content/drive/My Drive/temp/'

fname = "temp.txt" # name of the file with image links from Fatkun Batch (One example file in the repo)
with open(fname, 'r') as file:
    data = file.read()
data = data.split("\n")
print(len(data))
for i in range(len(data)):
  print(i)
  filename = dir + 'image'+ str(i) +'.jpg' 
  if data[i].find("https")!= -1:
    image = data[i][10:-3]
    with open(filename,'wb') as f:
      f.write(requests.get(image).content)
  else:
    image = data[i][33:-3]
    imgdata = base64.b64decode(image)
    with open(filename, 'wb') as f:
      f.write(imgdata)
