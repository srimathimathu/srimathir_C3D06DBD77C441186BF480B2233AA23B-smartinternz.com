def linearsearchproduct(productlist ,targetproduct):
 indices=[]

#searching list 1 sequentially
 for index,product in enumerate(productlist):
  if product == targetproduct:
   indices.append(index)

 return indices

#example usage
products = ["shoes","boots","loafur","shoes","sandel","shoes"]
target = "shoes"
target = 'apple'
result = linearsearchproduct(products,target)
print(result)