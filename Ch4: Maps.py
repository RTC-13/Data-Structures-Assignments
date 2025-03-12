
class Phonebook:

  def __init__(self):
    self.data = {}
  
  def add(self, name, number):
    self.data.update({name: number})
  
  def search(self, name):
    if name in self.data:
      return self.data[name]
    else:
      return None
    
  def delete(self, name):
    if self.search(name):
      del self.data[name]

  def __str__(self):
    return self.data
  

if __name__ == "__main__":
  book = Phonebook()
  book.add("Robert", 9292470857)
  book.add("Roberts", 92924708572)
  print(book.__str__())
  
  search = book.search("John")
  print("Search result: ", search)

  book.delete("Robert")
  print(book.__str__())

  book.add("Roberts", 92924208572)
  print(book.__str__())

