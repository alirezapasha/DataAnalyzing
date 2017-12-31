import csv
def creatingCode(merchant_link, hermosaz_link, product_title, original_price,sale_price):
	

	output_code = "<p style=\"text-align: center;\"><a href=\""
	output_code += merchant_link 
	output_code += "\" target=\"_blank\" rel=\"noopener\"><img class=\"wp-image-15135 size-medium\" src=\""
	output_code += hermosaz_link
	output_code += "\" alt=\""
	output_code += product_title
	output_code +=" | Hermosaz\" width=\"240\" height=\"300\" /></a>"
	output_code +="<h3 style=\"font-family: montserrat; font-size: medium; text-align: center;\">"
	output_code +=product_title
	output_code +="</h3><div style=\"text-align: center; font-family: montserrat; font-size: x-large;\">"

	if (sale_price!=""):
		output_code +="<del><span style=\"color: red;\">Orig: $"
		output_code +=original_price
		output_code += "</span></del>Now: $"
		output_code +=sale_price
		output_code +="</div>"
	else:
		output_code +="$"
		output_code +=original_price
		output_code +="</div>"
	
	return output_code

with open ('/home/alireza/Desktop/1/2.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		try:
			print creatingCode(row[0],row[1],row[2],row[3],row[4])
		except:
			print creatingCode(row[0],row[1],row[2],row[3],"")
		print "Next Product"
		print "Next Product"
		print "Next Product"
		print "Next Product"
		print "Next Product"


#print creatingCode("https://www.charlotterusse.com/floral-floral-mesh-bodysuit/302494170.html?dwvar_302494170_color=008&cgid=#q=Floral&sz=30&start=44","http://hermosaz.com/wp-content/uploads/2017/12/florals3.jpg","Floral Floral Mesh Bodysuit","23.99","18.00")