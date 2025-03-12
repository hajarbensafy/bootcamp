class Cat:
 def __init__(self, cat_name, cat_age):
  self.name =cat_name
  self.age=cat_age

  cat1 =cat("emma",3)
  cat2 =cat("cesar",5)
  cat3 =cat("morice",9)

  def find_oldest_cat(*cat):
   oldest_cat =max(cats,key=lambda cat:cat_age)
   return oldest_cat
  
   oldest_cat = find_oldest_cat(cat1,cat2,cat3)

   print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")