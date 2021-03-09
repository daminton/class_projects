dictionary = {
  1:'first', 
  2:'second',
  3:'third',
  4:'fourth',
  5:'fifth',
  6:'sixth',
  7:'seventh',
  8:'eighth',
  9:'ninth',
  10:'tenth',
  11:'eleventh',
  12:'twelfth'}

day = int(input('Enter day of Christmas: '))

present_list = ['And a partrige in a pear tree', 'Two turtle doves','Three french hens','Four calling birds', 'FIVE GOOOOOLDEN RIIIINGS', 'Six geese a-layin','Seven swans a-swimming','Eight maids a-milking','Nine ladies dancing','Ten lords a-leaping','Eleven pipers piping','Twelve drummers drumming']

print('On the', dictionary[day],'day of christmas my true love gave to me: ' )

item_recieved = present_list[day-1::-1]

if day == 1:
  print('A partiridge in a pear tree')
else:
  for i in item_recieved:
    print(i)

#list[start:stop:step]