# getters and setters

class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def new_value(self):
      return self._value
    
  @new_value.setter
  def new_value(self, new_value):
      self._value = new_value

obj = MyClass(10)
print(obj.new_value)
obj.new_value = 67
print(obj.new_value)
obj.show()
