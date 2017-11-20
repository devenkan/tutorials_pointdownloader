import urllib.request
# Download the file from `url` and save it locally under `file_name`:
a=input("\n enter the tutorials you want to read \n")

print(a+"/"+a)




url="http://tutorialspoint.com/"+a+"/"+a+"_tutorial.pdf"
print(url)
file_name=a+".pdf"


if(urllib.request.urlretrieve(url, file_name)):
	print("sucess recieved")
else:
	print("try again or file name is incorrect")	
